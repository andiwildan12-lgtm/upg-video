#!/usr/bin/env bash
# Cek kualitas otomatis file MP4 sebelum dikirim.  Pakai: qc.sh video.mp4 <durasi_target_detik> [detik_kartu_penutup]
F="$1"; DUR="$2"; CARD="${3:-0}"; EXP=$(awk -v d="$DUR" 'BEGIN{printf "%d", d*30+0.5}')
ok(){ echo "  [OK]   $*"; }; warn(){ echo "  [CEK]  $*"; W=1; }; W=0
echo "== QC: $F"
read -r VC W_ H_ FPS <<<"$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate -of csv=p=0 "$F" | tr ',' ' ')"
AC=$(ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of csv=p=0 "$F")
CD=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$F")
NF=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 "$F")
[[ "$VC" == h264 && "$AC" == aac ]] && ok "codec $VC + $AC" || warn "codec $VC + $AC (harus h264 + aac)"
[[ "$W_"x"$H_" == 1080x1920 ]] && ok "resolusi ${W_}x${H_}" || warn "resolusi ${W_}x${H_}"
[[ "$FPS" == 30/1 ]] && ok "fps $FPS (CFR)" || warn "fps $FPS"
awk -v c="$CD" -v d="$DUR" 'BEGIN{exit !((c-d)<0.05 && (d-c)<0.05)}' && ok "durasi $CD dtk (target $DUR)" || warn "durasi $CD dtk, target $DUR"
[[ "$NF" == "$EXP" ]] && ok "jumlah frame $NF" || warn "jumlah frame $NF, target $EXP"
BL=$(ffmpeg -v info -i "$F" -vf blackdetect=d=0.1:pix_th=0.05 -an -f null - 2>&1 | grep -o 'black_start:[0-9.]* black_end:[0-9.]*')
[[ -z "$BL" ]] && ok "tanpa frame hitam" || warn "frame hitam: $BL"
FR=$(ffmpeg -v info -i "$F" -vf freezedetect=n=-60dB:d=1.5 -an -f null - 2>&1 | grep -o 'freeze_start: [0-9.]*' | awk '{print $2}')
BAD=""; for s in $FR; do awk -v s="$s" -v c="$CARD" 'BEGIN{exit !(c>0 && s>=c-0.6)}' || BAD="$BAD $s"; done
[[ -z "$BAD" ]] && ok "tanpa frame beku tak disengaja (kartu penutup diabaikan)" || warn "frame beku mulai di:$BAD dtk"
SI=$(ffmpeg -v info -i "$F" -af silencedetect=noise=-50dB:d=0.5 -vn -f null - 2>&1 | grep -o 'silence_start: [0-9.]*' | awk '{print $2}' | tr '\n' ' ')
[[ -z "$SI" ]] && ok "tanpa hening mati" || warn "hening mati mulai di: $SI"
MX=$(ffmpeg -v info -i "$F" -af volumedetect -vn -f null - 2>&1 | grep -o 'max_volume: [-0-9.]*' | awk '{print $2}')
LU=$(ffmpeg -v info -i "$F" -af ebur128 -vn -f null - 2>&1 | grep -A1 'Integrated' | grep -o 'I: *[-0-9.]*' | awk '{print $2}')
awk -v m="$MX" 'BEGIN{exit !(m<-0.5)}' && ok "puncak $MX dB (aman dari clipping)" || warn "puncak $MX dB (risiko clipping)"
awk -v l="$LU" 'BEGIN{exit !(l>-18 && l<-13)}' && ok "loudness $LU LUFS" || warn "loudness $LU LUFS (target ±-16)"
mkdir -p qc_frames; ffmpeg -v error -y -sseof -0.1 -i "$F" -frames:v 1 qc_frames/last.jpg
[[ $W == 0 ]] && echo "== HASIL: LULUS" || echo "== HASIL: ADA YANG PERLU DICEK"
