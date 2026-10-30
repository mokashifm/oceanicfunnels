#!/bin/bash
# finish_reel.sh <work_dir> <out_name>
W=$1; NAME=$2; D=/home/claude/oceanicfunnels/ads/med-spas/reels
rm -rf $W/of; mkdir -p $W/of
T=$(python3 -c "import json;print(json.load(open('$W/timing.json'))['TOTAL'])")
node $D/overlay_frames.js $W/overlay.html $W/of $T 30
python3 -I $D/music.py $W/music.wav $T
ST=($(python3 -c "import json;print(' '.join(str(int(x*1000)) for x in json.load(open('$W/timing.json'))['vost']))"))
IN=""; F=""; L=""; n=${#ST[@]}
for i in $(seq 0 $((n-1))); do IN="$IN -i $W/vo$i.wav"; F="$F[$((i+1)):a]aresample=44100,pan=stereo|c0=c0|c1=c0,adelay=${ST[$i]}|${ST[$i]},volume=1.6[v$i];"; L="$L[v$i]"; done
F="$F${L}amix=inputs=$n:normalize=0[vo];[0:a]volume=0.22[m];[m][vo]amix=inputs=2:normalize=0,alimiter=limit=0.95[aout]"
ffmpeg -y -loglevel error -i $W/music.wav $IN -filter_complex "$F" -map "[aout]" -t $T $W/audio.wav
ffmpeg -y -loglevel error -i $W/base.mp4 -framerate 30 -i $W/of/o%04d.png -i $W/audio.wav -filter_complex "[0:v][1:v]overlay=format=auto,format=yuv420p[v]" -map "[v]" -map 2:a -c:v libx264 -preset veryfast -crf 19 -c:a aac -b:a 160k -t $T -movflags +faststart $W/$NAME.mp4
mkdir -p $D/out; cp $W/$NAME.mp4 $D/out/
echo "DONE $NAME $(ffprobe -v error -show_entries format=duration -of csv=p=0 $W/$NAME.mp4)"
