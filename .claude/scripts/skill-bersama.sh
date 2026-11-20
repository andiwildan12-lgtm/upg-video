#!/usr/bin/env bash
# Menjaga skill bersama (.claude/skill-bersama.txt) identik di repo upg-video dan ruma-video.
#   cek    : bandingkan dengan repo saudara, tunjukkan mana yang beda dan mana yang lebih baru
#   kirim  : salin skill bersama dari repo INI ke repo saudara, lalu commit di sana (push tetap manual)
#   tarik  : salin skill bersama dari repo saudara ke repo INI (tanpa commit)
#   zip    : buat dist/skill-<repo>-lengkap.zip + dist/skills/<nama>.zip (identitas + bersama)
set -u
MODE="${1:-cek}"
ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
NAMA="$(basename "$ROOT")"
case "$NAMA" in upg-video) SIB=ruma-video;; ruma-video) SIB=upg-video;; *) echo "Jalankan dari repo upg-video atau ruma-video"; exit 1;; esac
LIST="$ROOT/.claude/skill-bersama.txt"
SKILLS=$(grep -v '^#' "$LIST" | grep -v '^\s*$')

cari_sib() {
  for d in "$ROOT/../$SIB" "/home/user/$SIB"; do [ -d "$d/.claude/skills" ] && { echo "$d"; return; }; done
  local c="$HOME/.cache/skill-repo/$SIB"
  if [ -d "$c/.git" ]; then timeout 60 git -C "$c" pull -q --ff-only >/dev/null 2>&1 || true
  else mkdir -p "$(dirname "$c")"; timeout 120 git clone -q --depth 1 "https://github.com/andiwildan12-lgtm/$SIB" "$c" >/dev/null 2>&1 || true; fi
  [ -d "$c/.claude/skills" ] && echo "$c"
}
waktu() { local t; t=$(git -C "$1" log -1 --format=%ct -- ".claude/skills/$2" 2>/dev/null); echo "${t:-0}"; }

if [ "$MODE" = zip ]; then
  cd "$ROOT/.claude/skills" && mkdir -p "$ROOT/dist/skills"
  rm -f "$ROOT/dist/skill-$NAMA-lengkap.zip" "$ROOT"/dist/skills/*.zip
  zip -qr "$ROOT/dist/skill-$NAMA-lengkap.zip" . -x '*/node_modules/*' '*/__pycache__/*'
  for s in */; do s=${s%/}; zip -qr "$ROOT/dist/skills/$s.zip" "$s" -x '*/node_modules/*' '*/__pycache__/*'; done
  echo "Zip dibuat: dist/skill-$NAMA-lengkap.zip dan dist/skills/*.zip"; ls -1 "$ROOT/dist/skills"; exit 0
fi

S="$(cari_sib)"; [ -z "$S" ] && { echo "Repo $SIB tidak terjangkau (tambahkan ke sesi)."; exit 1; }
BEDA=0
for k in $SKILLS; do
  a="$ROOT/.claude/skills/$k"; b="$S/.claude/skills/$k"
  if [ "$MODE" = kirim ]; then
    [ -d "$a" ] || { echo "LEWAT $k: tidak ada di $NAMA"; continue; }
    rm -rf "$b"; cp -r "$a" "$b"; echo "kirim  $k -> $SIB"
  elif [ "$MODE" = tarik ]; then
    [ -d "$b" ] || { echo "LEWAT $k: tidak ada di $SIB"; continue; }
    rm -rf "$a"; cp -r "$b" "$a"; echo "tarik  $k <- $SIB"
  else
    if [ ! -d "$a" ] || [ ! -d "$b" ] || ! diff -rq -x __pycache__ -x node_modules "$a" "$b" >/dev/null 2>&1; then
      BEDA=1; ta=$(waktu "$ROOT" "$k"); tb=$(waktu "$S" "$k")
      if [ "$tb" -gt "$ta" ]; then baru="$SIB (jalankan: tarik)"; else baru="$NAMA (jalankan: kirim)"; fi
      echo "BEDA   $k  | lebih baru: $baru"
    fi
  fi
done
if [ "$MODE" = kirim ]; then
  cp "$LIST" "$S/.claude/skill-bersama.txt"; cp "$0" "$S/.claude/scripts/skill-bersama.sh" 2>/dev/null || true
  if git -C "$S" rev-parse >/dev/null 2>&1 && [ "$S" != "$HOME/.cache/skill-repo/$SIB" ]; then
    git -C "$S" add .claude/skills .claude/skill-bersama.txt .claude/scripts/skill-bersama.sh
    git -C "$S" diff --cached --quiet && echo "Repo $SIB sudah sama." || { git -C "$S" commit -q -m "Sinkron skill bersama dari $NAMA"; echo "Commit di $SIB dibuat. Push: git -C $S push"; }
  else echo "Salinan $SIB adalah cache: tambahkan repo $SIB ke sesi untuk commit + push."; fi
elif [ "$MODE" = cek ]; then
  if [ $BEDA = 0 ]; then echo "Skill bersama identik dengan $SIB."; fi
fi
exit 0
