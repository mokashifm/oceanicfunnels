# Original royalty-free music bed: soft pad chords + plucks + light hats. Usage: music.py out.wav seconds
import sys, numpy as np, soundfile as sf
out, dur = sys.argv[1], float(sys.argv[2]); sr = 44100; bpm = 96; beat = 60 / bpm
n = int(sr * dur); t = np.arange(n) / sr; mix = np.zeros((n, 2))
def note(f): return 440 * 2 ** ((f - 69) / 12)
prog = [[57, 60, 64, 69], [53, 57, 60, 65], [48, 52, 55, 64], [55, 59, 62, 67]]  # Am F C G
bar = beat * 4
def env(L, a, r):
    e = np.ones(L); A = min(int(a * sr), L // 2); R = min(int(r * sr), L // 2)
    e[:A] = np.linspace(0, 1, A); e[-R:] *= np.linspace(1, 0, R); return e
i = 0; pos = 0.0
while pos < dur:
    ch = prog[i % 4]; L = min(int(bar * sr), n - int(pos * sr)); s = int(pos * sr)
    tt = np.arange(L) / sr; pad = np.zeros(L)
    for m in ch:
        f = note(m)
        pad += 0.5 * np.sin(2 * np.pi * f * tt) + 0.18 * np.sin(2 * np.pi * f * 2.003 * tt) + 0.25 * np.sin(2 * np.pi * f * 0.999 * tt)
    pad *= env(L, 0.6, 0.6) * 0.035
    mix[s:s + L, 0] += pad; mix[s:s + L, 1] += pad * 0.95
    for k in range(8):  # pluck arpeggio on 8ths
        ps = s + int(k * beat / 2 * sr)
        if ps >= n: break
        PL = min(int(0.5 * sr), n - ps); pt = np.arange(PL) / sr
        f = note(ch[[0, 2, 1, 3, 2, 1, 3, 2][k]] + 12)
        pl = (np.sin(2 * np.pi * f * pt) + 0.3 * np.sin(4 * np.pi * f * pt)) * np.exp(-pt * 7) * 0.05
        pan = 0.35 + 0.3 * (k % 2)
        mix[ps:ps + PL, 0] += pl * (1 - pan); mix[ps:ps + PL, 1] += pl * pan
    for k in range(4):  # kick-ish soft pulse + hat
        ps = s + int(k * beat * sr)
        if ps >= n: break
        KL = min(int(0.25 * sr), n - ps); kt = np.arange(KL) / sr
        kick = np.sin(2 * np.pi * (60 + 60 * np.exp(-kt * 30)) * kt) * np.exp(-kt * 12) * 0.12
        mix[ps:ps + KL] += kick[:, None]
        hs = ps + int(beat / 2 * sr)
        if hs < n:
            HL = min(int(0.05 * sr), n - hs); hat = np.random.randn(HL) * np.exp(-np.arange(HL) / sr * 120) * 0.02
            mix[hs:hs + HL] += hat[:, None]
    pos += bar; i += 1
fade = int(2 * sr); mix[-fade:] *= np.linspace(1, 0, fade)[:, None]; mix[:int(.5*sr)] *= np.linspace(0, 1, int(.5*sr))[:, None]
mix /= np.max(np.abs(mix)) + 1e-9; mix *= 0.8
sf.write(out, mix, sr); print("music", dur)
