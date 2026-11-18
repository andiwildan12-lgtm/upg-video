#!/usr/bin/env bash
# Saat sesi mulai: ambil skill dari repo saudara (ruma-video) supaya skill Ruma & UPG saling terlihat.
# Skill repo ini sendiri sudah dimuat Claude Code; yang disalin hanya skill repo saudara ke ~/.claude/skills.
SIB=ruma-video
OWNER=andiwildan12-lgtm
DST="$HOME/.claude/skills"
SRC=""
for d in "${CLAUDE_PROJECT_DIR:-.}/../$SIB" "/home/user/$SIB"; do
  [ -d "$d/.claude/skills" ] && { SRC="$d"; break; }
done
if [ -z "$SRC" ]; then
  CACHE="$HOME/.cache/skill-repo/$SIB"
  if [ -d "$CACHE/.git" ]; then
    timeout 60 git -C "$CACHE" pull -q --ff-only >/dev/null 2>&1 || true
  else
    mkdir -p "$(dirname "$CACHE")"
    timeout 120 git clone -q --depth 1 --filter=blob:limit=2m "https://github.com/$OWNER/$SIB" "$CACHE" >/dev/null 2>&1 || true
  fi
  [ -d "$CACHE/.claude/skills" ] && SRC="$CACHE"
fi
if [ -n "$SRC" ]; then
  mkdir -p "$DST"
  cp -r "$SRC/.claude/skills/." "$DST/" 2>/dev/null || true
  echo "Skill repo $SIB disinkronkan ke $DST: $(ls "$SRC/.claude/skills" | tr '\n' ' ')"
else
  echo "Skill repo $SIB tidak terjangkau. Tambahkan repo $SIB ke sesi/environment agar skillnya ikut terbaca."
fi
exit 0
