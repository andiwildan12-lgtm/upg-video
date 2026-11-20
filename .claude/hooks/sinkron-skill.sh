#!/usr/bin/env bash
# SessionStart: repo upg-video (UPG + GrowWith) dan ruma-video (Ruma + Dalam Gigi) terpisah.
# Skill bersama disimpan di KEDUA repo; hook ini hanya mengecek apakah salinannya masih identik.
ROOT="${CLAUDE_PROJECT_DIR:-$(pwd)}"
S="$ROOT/.claude/scripts/skill-bersama.sh"
[ -f "$S" ] || exit 0
OUT="$(timeout 150 bash "$S" cek 2>&1)"
echo "Cek skill bersama: $OUT"
echo "$OUT" | grep -q '^BEDA' && echo "PERHATIAN Claude: ada skill bersama yang beda antar-repo. Samakan dulu (tarik/kirim) sebelum bekerja, lalu commit + push kedua repo."
exit 0
