#!/usr/bin/env python3
"""Pencatat ACC dan gerbang produksi UPG Motion.

Pemakaian:
  record <dir_proyek> --version V3 --message "<kutipan persis pesan Dir>" [--scope "..."]
      Mencatat ACC produksi untuk rancangan-V3.md (hash file ikut disimpan).
      HANYA dijalankan setelah Dir benar-benar mengirim pesan ACC produksi.
  check <dir_proyek>
      Exit 0 jika ACC sah dan rancangan tidak berubah sejak ACC; selain itu exit 1.
  status <dir_proyek>
      Menampilkan status ACC tanpa mengubah apa pun.
"""
import argparse, datetime, hashlib, json, pathlib, re, sys

PRODUCTION_WORDS = re.compile(r"\b(acc|setuju|approve|oke|ok|gas|lanjut|render)\b", re.I)


def sha256(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def fail(msg: str) -> None:
    print(f"DITOLAK: {msg}")
    sys.exit(1)


def cmd_record(a):
    d = pathlib.Path(a.project)
    ver = a.version.upper()
    if not re.fullmatch(r"V\d+", ver):
        fail("versi harus berbentuk V<angka>, mis. V3")
    draft = d / f"rancangan-{ver}.md"
    if not draft.is_file():
        fail(f"{draft} tidak ada; simpan rancangan final yang di-ACC lebih dulu")
    text = draft.read_text(encoding="utf-8")
    for section in ("Naskah narasi", "Storyboard"):
        if section.lower() not in text.lower():
            fail(f"rancangan {ver} belum lengkap (bagian '{section}' tidak ditemukan)")
    msg = a.message.strip()
    if not msg or not PRODUCTION_WORDS.search(msg):
        fail("pesan ACC kosong atau tidak berisi persetujuan; salin kutipan persis pesan Dir")
    rec = {
        "status": "ACC_PRODUKSI",
        "version": ver,
        "draft_file": draft.name,
        "draft_sha256": sha256(draft),
        "user_message": msg,
        "scope": a.scope or f"Produksi video sesuai rancangan {ver} (tidak termasuk unggah media sosial)",
        "recorded_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    }
    (d / "acc.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"ACC tercatat: {d.name} {ver}")


def load(d: pathlib.Path):
    f = d / "acc.json"
    if not f.is_file():
        fail(f"belum ada catatan ACC di {d} — tetap di mode diskusi/peninjauan")
    rec = json.loads(f.read_text(encoding="utf-8"))
    if rec.get("status") != "ACC_PRODUKSI":
        fail(f"status '{rec.get('status')}' bukan ACC produksi")
    if not rec.get("user_message", "").strip():
        fail("catatan ACC tidak memuat pesan Dir")
    draft = d / rec.get("draft_file", "")
    if not draft.is_file():
        fail(f"file rancangan {rec.get('draft_file')} hilang")
    if sha256(draft) != rec.get("draft_sha256"):
        fail(f"{draft.name} berubah setelah ACC — perlu ACC ulang untuk versi baru")
    return rec


def cmd_check(a):
    rec = load(pathlib.Path(a.project))
    print(f"OK: produksi {rec['version']} diizinkan. Lingkup: {rec['scope']}")


def cmd_status(a):
    d = pathlib.Path(a.project)
    f = d / "acc.json"
    if not f.is_file():
        print("Status: BELUM ACC (mode diskusi/peninjauan)")
        return
    print(f.read_text(encoding="utf-8"))
    try:
        load(d)
        print("Gerbang: LOLOS")
    except SystemExit:
        pass


p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
sp = p.add_subparsers(dest="cmd", required=True)
r = sp.add_parser("record"); r.add_argument("project"); r.add_argument("--version", required=True)
r.add_argument("--message", required=True); r.add_argument("--scope")
r.set_defaults(fn=cmd_record)
for name, fn in (("check", cmd_check), ("status", cmd_status)):
    s = sp.add_parser(name); s.add_argument("project"); s.set_defaults(fn=fn)
a = p.parse_args()
a.fn(a)
