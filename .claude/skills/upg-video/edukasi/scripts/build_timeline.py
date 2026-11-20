#!/usr/bin/env python3
"""Bangun src/timeline.js (jalur EDUKASI DOKTER) dari edit.json + work/transkrip.json.

Pemakaian: python3 build_timeline.py <folder-proyek>

edit.json (lihat edukasi/contoh-edit.json):
  cuts    : [{clip, in, out, fx, fy, scale, flash}]   potongan take berurutan (detik di klip asli)
  replace : {"salah": "benar"}                         koreksi ejaan transkrip (huruf kecil)
  hl      : ["tenang", "aman"]                         kata yang disorot (kotak oranye) di mana pun muncul
  titles / stickers / zooms / cards / sfx / nametag / end / music / logo
Waktu event boleh berupa angka (detik video hasil) atau JANGKAR:
  "c3:tenang"       -> awal kata 'tenang' (kemunculan pertama) di potongan ke-3 (mulai 0)
  "c3:tenang#2"     -> kemunculan ke-2
  "c3:tenang>"      -> AKHIR kata itu
  "c3@1.5"          -> 1,5 dtk setelah potongan ke-3 mulai;  "c3@end" -> akhir potongan
  "...+0.2" / "...-0.3" -> geser
  "end"             -> akhir potongan terakhir (awal end card)
SFX otomatis (sfx_auto, default true): pop tiap stiker, whoosh kartu masuk/keluar, ding item checklist,
ketik tiap bubble chat, swish judul/pill, sparkle burst. SFX manual di "sfx" ditambahkan di atasnya.
"""
import json, re, sys
from pathlib import Path

P = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else sys.exit(__doc__)
E = json.loads((P / "edit.json").read_text())
T = json.loads((P / "work" / "transkrip.json").read_text())
REP = {k.lower(): v for k, v in E.get("replace", {}).items()}
HL = {h.lower() for h in E.get("hl", [])}
KEEP = set(E.get("keep_case", ["UPG", "drg.", "Firdha"]))

def norm(w):
    return re.sub(r"[^\w\-]", "", w.lower())

# ---------- potongan & kata ----------
cuts, words_by_cut, t0 = [], [], 0.0
for i, c in enumerate(E["cuts"]):
    dur = round(c["out"] - c["in"], 3)
    cuts.append({"clip": c["clip"], "in": c["in"], "dur": dur, "start": round(t0, 3),
                 "fx": c.get("fx", 540), "fy": c.get("fy", 700), "tx": c.get("tx", 540), "ty": c.get("ty", 780),
                 "scale": c.get("scale", 1.0), "flash": c.get("flash", i > 0)})
    ws = []
    for seg in T[c["clip"]]:
        for w, a, b in seg["w"]:
            w = w.strip()
            if not w:
                continue
            if w.startswith("-") and ws:            # "berbeda" "-beda" -> "berbeda-beda"
                ws[-1]["raw"] += w; ws[-1]["b"] = b; continue
            ws.append({"raw": w, "a": a, "b": b})
    # kata dipakai bila tumpang-tindih dengan potongan (awal kata pertama dari Whisper sering terlalu dini)
    ws = [w for w in ws if w["b"] > c["in"] + 0.12 and w["a"] < c["out"] - 0.12]
    for w in ws:
        w["at"] = round(t0 + max(0, w["a"] - c["in"]), 3)
        w["end"] = round(t0 + min(dur, w["b"] - c["in"]), 3)
        key = norm(w["raw"])
        txt = REP.get(key, None)
        punct = re.sub(r"[\w\-]", "", w["raw"])
        base = txt if txt is not None else re.sub(r"[^\w\-]", "", w["raw"])
        w["key"] = norm(base)
        w["text"] = base if base in KEEP else base.lower()
        w["text"] += "?" if "?" in punct else ("!" if "!" in punct else "")
        w["brk"] = bool(re.search(r"[,.!?;]", punct))
    ws = [w for w in ws if w["key"]]                  # replace ke "" = buang kata (mis. hasil transkrip terpecah)
    words_by_cut.append(ws)
    t0 += dur
cuts_end = round(t0, 3)

# ---------- jangkar waktu ----------
def resolve(v):
    if isinstance(v, (int, float)):
        return float(v)
    m = re.fullmatch(r"\s*(.+?)\s*([+-]\s*[\d.]+)?\s*", str(v))
    base, off = m.group(1), float(m.group(2).replace(" ", "")) if m.group(2) else 0.0
    if base == "end":
        return round(cuts_end + off, 3)
    m2 = re.fullmatch(r"c(\d+)@(end|[\d.]+)", base)
    if m2:
        c = cuts[int(m2.group(1))]
        return round(c["start"] + (c["dur"] if m2.group(2) == "end" else float(m2.group(2))) + off, 3)
    m3 = re.fullmatch(r"c(\d+):([^#>]+)(?:#(\d+))?(>)?", base)
    if not m3:
        sys.exit(f"Jangkar tidak dikenal: {v}")
    ci, word, nth, tail = int(m3.group(1)), norm(m3.group(2)), int(m3.group(3) or 1), m3.group(4)
    hits = [w for w in words_by_cut[ci] if w["key"] == word or norm(w["raw"]) == word]
    if len(hits) < nth:
        sys.exit(f"Kata '{word}' (ke-{nth}) tidak ada di potongan c{ci}: {[w['key'] for w in words_by_cut[ci]]}")
    return round((hits[nth - 1]["end"] if tail else hits[nth - 1]["at"]) + off, 3)

TIME_KEYS = {"at", "from", "to", "strikeAt"}
def walk(o):
    if isinstance(o, list):
        return [walk(x) for x in o]
    if isinstance(o, dict):
        return {k: (resolve(v) if k in TIME_KEYS else walk(v)) for k, v in o.items()}
    return o

# ---------- caption: grup 1–3 kata ----------
captions = []
for ws in words_by_cut:
    grp = []
    def flush(nxt=None):
        if grp:
            to = min(nxt if nxt else grp[-1]["end"] + 0.35, grp[-1]["end"] + 0.6)
            captions.append({"from": grp[0]["at"], "to": round(to, 3),
                             "words": [{"text": g["text"], "at": g["at"], **({"hl": True} if g["key"] in HL else {})} for g in grp]})
    for i, w in enumerate(ws):
        if grp and (len(grp) >= 3 or sum(len(g["text"]) for g in grp) + len(w["text"]) > 20 or w["at"] - grp[-1]["end"] > 0.35
                    or w["key"] in HL or grp[-1]["key"] in HL):
            flush(w["at"]); grp = []
        grp.append(w)
        if w["brk"]:
            flush(ws[i + 1]["at"] if i + 1 < len(ws) else None); grp = []
    flush()

titles = walk(E.get("titles", []))
stickers = walk(E.get("stickers", []))
zooms = walk(E.get("zooms", []))
cards = walk(E.get("cards", []))
nametag = walk(E.get("nametag")) if E.get("nametag") else None
sfx = walk(E.get("sfx", []))

if E.get("sfx_auto", True):
    for s in stickers:
        sfx.append({"at": s["at"], "file": "sparkle.mp3" if s.get("kind") == "burst" else "pop.mp3", "vol": 0.45})
    for k in titles:
        sfx.append({"at": k["from"], "file": "swish.mp3", "vol": 0.4})
        if k.get("strikeAt") is not None:
            sfx.append({"at": k["strikeAt"], "file": "scratch.mp3", "vol": 0.45})
    for c in cards:
        sfx.append({"at": c["from"] - 0.15, "file": "whoosh.mp3", "vol": 0.5})
        sfx.append({"at": c["to"] - 0.1, "file": "whoosh.mp3", "vol": 0.35})
        for it in c.get("items", []):
            sfx.append({"at": it["at"] + 0.25, "file": "ding.mp3", "vol": 0.4})
        for b in c.get("bubbles", []):
            sfx.append({"at": b["at"] - 0.5, "file": "typing.mp3", "vol": 0.3, "len": 0.6})
            sfx.append({"at": b["at"], "file": "message.mp3", "vol": 0.4})
        for l in c.get("lines", []):
            sfx.append({"at": l["at"], "file": "pop.mp3", "vol": 0.4})
    for z in zooms:
        if z.get("mode") != "slow":
            sfx.append({"at": z["from"] - 0.05, "file": "zoom.mp3", "vol": 0.3})
    if nametag:
        sfx.append({"at": nametag["from"], "file": "click.mp3", "vol": 0.35})
    sfx.append({"at": cuts_end, "file": "whoosh.mp3", "vol": 0.5})
sfx.sort(key=lambda s: s["at"])

end = E.get("end", {"sec": 3.0, "line1": "Jangan takut ke dokter gigi", "line2": ""})
out = f"""// DIBUAT OTOMATIS oleh edukasi/scripts/build_timeline.py dari edit.json — jangan diedit manual.
export const CUTS = {json.dumps(cuts, ensure_ascii=False)};
export const CAPTIONS = {json.dumps(captions, ensure_ascii=False)};
export const TITLES = {json.dumps(titles, ensure_ascii=False)};
export const STICKERS = {json.dumps(stickers, ensure_ascii=False)};
export const ZOOMS = {json.dumps(zooms, ensure_ascii=False)};
export const CARDS = {json.dumps(cards, ensure_ascii=False)};
export const NAMETAG = {json.dumps(nametag, ensure_ascii=False)};
export const SFX = {json.dumps(sfx, ensure_ascii=False)};
export const MUSIC = {json.dumps(E.get("music"), ensure_ascii=False)};
export const LOGO = {json.dumps(E.get("logo", True))};
export const END = {json.dumps(end, ensure_ascii=False)};
export const cutsEnd = {cuts_end};
export const totalSec = () => cutsEnd + END.sec;
"""
(P / "src" / "timeline.js").write_text(out)
print(f"timeline.js: {len(cuts)} potongan, {cuts_end:.1f} dtk + end card {end['sec']} dtk = {cuts_end + end['sec']:.1f} dtk; "
      f"{len(captions)} grup caption, {len(sfx)} SFX")
missing = sorted({s['file'] for s in sfx} - {f.name for f in (P / 'public' / 'sfx').glob('*')}) if (P / 'public' / 'sfx').exists() else sorted({s['file'] for s in sfx})
if missing:
    print("SFX belum ada di public/sfx/:", ", ".join(missing))
# daftar kata per potongan (untuk memilih jangkar)
(P / "work" / "kata-per-potongan.txt").write_text("\n".join(
    f"c{i} [{c['start']:.2f}-{c['start'] + c['dur']:.2f}] " + " ".join(f"{w['key']}@{w['at']:.2f}" for w in ws)
    for i, (c, ws) in enumerate(zip(cuts, words_by_cut))))
