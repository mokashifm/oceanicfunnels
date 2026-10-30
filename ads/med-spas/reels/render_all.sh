#!/bin/bash
S=/tmp/claude-0/-home-claude/4c56178f-3b6b-54ea-a8fd-72eb28719326/scratchpad/three; D=/home/claude/oceanicfunnels/ads/med-spas/reels
cd $S
for r in A-after-hours B-mid-treatment C-no-shows D-rebook; do
  O=out_$r; rm -rf $O/fr; mkdir -p $O/fr
  END=$(python3 -c "import json;print(json.load(open('$O/timing.json'))['END'])")
  node frames3d.js $r $O/fr frames $END 30
  python3 -I $D/music.py $O/music.wav $END
  ST=($(python3 -c "import json;print(' '.join(str(int(x*1000)) for x in json.load(open('$O/timing.json'))['st']))"))
  IN=""; F=""; L=""; n=${#ST[@]}
  for i in $(seq 0 $((n-1))); do IN="$IN -i $O/vo$i.wav"; F="$F[$((i+1)):a]aresample=44100,pan=stereo|c0=c0|c1=c0,adelay=${ST[$i]}|${ST[$i]},volume=1.6[v$i];"; L="$L[v$i]"; done
  F="$F${L}amix=inputs=$n:normalize=0[vo];[0:a]volume=0.22[m];[m][vo]amix=inputs=2:normalize=0,alimiter=limit=0.95[aout]"
  ffmpeg -y -loglevel error -i $O/music.wav $IN -filter_complex "$F" -map "[aout]" -t $END $O/audio.wav
  ffmpeg -y -loglevel error -framerate 30 -i $O/fr/f%04d.jpg -i $O/audio.wav -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -shortest -movflags +faststart $S/reel-$r.mp4
  echo "DONE $r $(ffprobe -v error -show_entries format=duration -of csv=p=0 $S/reel-$r.mp4)"
done
echo ALLDONE
