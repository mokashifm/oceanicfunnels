# Voiceover for reel 2 (Kokoro TTS, local). Writes one wav per line + timings.json
import sys, json, soundfile as sf, numpy as np
from kokoro_onnx import Kokoro
model, out, voice = sys.argv[1], sys.argv[2], sys.argv[3]
LINES = [
 "It's nine fourteen on a Saturday night. Your med spa is closed.",
 "But the DMs, calls and website chats keep coming in.",
 "Now an A.I. receptionist answers every call,",
 "replies to every DM in seconds, and books the consultation with a deposit.",
 "Reminders go out by text and email, so clients actually show up.",
 "And your calendar keeps filling, without hiring a sales team.",
 "Oceanic Funnels builds this for your med spa in fourteen days. Book your free info call.",
]
k = Kokoro(model + "/kokoro-v1.0.onnx", model + "/voices-v1.0.bin")
T = []
for i, l in enumerate(LINES):
    s, sr = k.create(l, voice=voice, speed=1.02, lang="en-us")
    sf.write(f"{out}/vo{i}.wav", s, sr); T.append(round(len(s) / sr, 3))
json.dump({"lines": LINES, "dur": T, "sr": sr}, open(f"{out}/timings.json", "w"))
print(T, sum(T))
