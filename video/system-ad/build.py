import subprocess, os, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
os.makedirs('seg', exist_ok=True); os.makedirs('ov', exist_ok=True)
F_B = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'
F_M = '/usr/share/fonts/opentype/inter/Inter-Medium.otf'
F_SB = '/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS)]

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print(r.stderr[-1500:]); raise SystemExit(1)

UP = f'scale={W}:{H}:flags=lanczos,unsplit=0' if False else f'scale={W}:{H}:flags=lanczos,unsharp=5:5:0.6'

# segment: (name, clip, clip_start, clip_end, out_dur, extra_vf)
SEGS = [
    ('a', 's1_net',     0.0, 5.04, 3.4, ''),
    ('b', 's2_panels',  0.0, 5.04, 6.7, ''),
    ('c', 's3_plumber', 0.4, 5.04, 4.3, ''),
    ('d', 's4_sofa',    0.0, 5.04, 5.2, ''),
    ('e', 's5_medspa',  0.6, 5.04, 3.7, ''),
    ('f', 's6_orb',     1.6, 5.04, 3.1, ''),
    ('g', 's1_net',     0.0, 5.04, 3.1, ',boxblur=18:2,eq=brightness=-0.12'),
    ('h', 's7_point',   0.0, 5.04, 6.4, ''),
]
for name, clip, a, b, dur, extra in (SEGS if not os.path.exists('seg/base.mp4') else []):
    span = b - a
    speed = span / dur  # <1 slows down
    out = f'seg/{name}.mp4'
    vf = (f'trim={a}:{b},setpts=(PTS-STARTPTS)/{speed},fps={FPS},{UP}{extra},'
          f'trim=duration={dur},setpts=PTS-STARTPTS,'
          f'fade=t=in:st=0:d=0.25,fade=t=out:st={dur-0.25}:d=0.25')
    if name == 'a': vf = vf.replace('fade=t=in:st=0:d=0.25', 'fade=t=in:st=0:d=0.5')
    run(['ffmpeg', '-y', '-v', 'error', '-i', f'clips/{clip}.mp4', '-vf', vf, '-an', *ENC, 'seg/tmp.mp4'])
    os.replace('seg/tmp.mp4', out)

with open('seg/list.txt', 'w') as f:
    for s in SEGS: f.write(f"file '{s[0]}.mp4'\n")
if not os.path.exists('seg/base.mp4'): run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', 'seg/list.txt', '-c', 'copy', 'seg/base.mp4'])

# ---------- overlays ----------
def canvas(): return Image.new('RGBA', (W, H), (0, 0, 0, 0))

def caption(text, path):
    im = canvas(); d = ImageDraw.Draw(im); f = ImageFont.truetype(F_B, 64)
    words = text.split(); lines = []; cur = ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) > 880 and cur: lines.append(cur); cur = w
        else: cur = t
    lines.append(cur)
    y = 1440 - (len(lines) - 1) * 40
    sh = canvas(); sd = ImageDraw.Draw(sh)
    for i, l in enumerate(lines):
        x = (W - d.textlength(l, font=f)) / 2
        sd.text((x, y + i * 80), l, font=f, fill=(0, 0, 0, 200))
    sh = sh.filter(ImageFilter.GaussianBlur(10))
    im = Image.alpha_composite(sh, im); d = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        x = (W - d.textlength(l, font=f)) / 2
        d.text((x, y + i * 80), l, font=f, fill=(255, 255, 255, 255))
    im.save(path)

def bubble(path):
    im = canvas(); d = ImageDraw.Draw(im)
    x0, y0, w = 110, 1230, 860
    head = ImageFont.truetype(F_SB, 30); body = ImageFont.truetype(F_M, 44)
    txt = ["Hi Sarah! Thursday at 10 works.", "I've booked you in and sent", "you a reminder. ✓"]
    h = 70 + len(txt) * 60 + 40
    glow = canvas(); gd = ImageDraw.Draw(glow)
    gd.rounded_rectangle([x0 - 6, y0 - 6, x0 + w + 6, y0 + h + 6], 46, fill=(61, 227, 200, 120))
    glow = glow.filter(ImageFilter.GaussianBlur(26)); im = Image.alpha_composite(im, glow); d = ImageDraw.Draw(im)
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], 40, fill=(10, 24, 26, 235), outline=(61, 227, 200, 255), width=3)
    d.ellipse([x0 + 34, y0 + 30, x0 + 58, y0 + 54], fill=(61, 227, 200, 255))
    d.text((x0 + 72, y0 + 26), 'Oceanic AI agent  ·  now', font=head, fill=(157, 176, 173, 255))
    for i, t in enumerate(txt):
        d.text((x0 + 34, y0 + 82 + i * 60), t, font=body, fill=(255, 255, 255, 255))
    im.save(path)

def dash(path):
    im = canvas()
    shot = Image.open('../../site/assets/img/os-reporting.webp').convert('RGBA')
    sw = 1000; sh_ = int(shot.height * sw / shot.width); shot = shot.resize((sw, sh_), Image.LANCZOS)
    x0, y0 = (W - sw) // 2, (H - sh_) // 2 - 120
    glow = canvas(); gd = ImageDraw.Draw(glow)
    gd.rounded_rectangle([x0 - 10, y0 - 10, x0 + sw + 10, y0 + sh_ + 10], 34, fill=(61, 227, 200, 150))
    glow = glow.filter(ImageFilter.GaussianBlur(40)); im = Image.alpha_composite(im, glow)
    m = Image.new('L', shot.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, sw, sh_], 24, fill=255)
    im.paste(shot, (x0, y0), m)
    ImageDraw.Draw(im).rounded_rectangle([x0, y0, x0 + sw, y0 + sh_], 24, outline=(61, 227, 200, 200), width=3)
    im.save(path)

def endcard(path_logo, path_tag):
    im = canvas(); lg = Image.open('logo.png').convert('RGBA')
    lw = 760; lg = lg.resize((lw, int(lg.height * lw / lg.width)), Image.LANCZOS)
    im.paste(lg, ((W - lw) // 2, 1160), lg); im.save(path_logo)
    t = canvas(); d = ImageDraw.Draw(t); f = ImageFont.truetype(F_M, 46)
    s = 'The system behind growing businesses.'
    d.text(((W - d.textlength(s, font=f)) / 2, 1350), s, font=f, fill=(200, 222, 218, 255)); t.save(path_tag)

T = json.load(open('ad_timing.json'))
caps = []
for a, b, t in T:
    if t.startswith('AGENT:') or t.startswith('Oceanic Funnels.') or t.startswith('The system'): continue
    caps.append((a, b, t))
for i, (a, b, t) in enumerate(caps):
    caption(t, f'ov/c{i}.png')
bubble('ov/bubble.png'); dash('ov/dash.png'); endcard('ov/logo.png', 'ov/tag.png')

# timed overlays: (png, start, end, fade)
OV = []
for i, (a, b, t) in enumerate(caps):
    nxt = caps[i + 1][0] if i + 1 < len(caps) else b + 0.3
    OV.append((f'ov/c{i}.png', a - 0.05, min(b + 0.35, nxt - 0.02), 0.12))
OV += [('ov/bubble.png', 14.5, 19.5, 0.3), ('ov/dash.png', 26.45, 29.45, 0.35),
       ('ov/logo.png', 29.9, 35.8, 0.6), ('ov/tag.png', 31.1, 35.8, 0.5)]
inputs = ['-i', 'seg/base.mp4']
for p, *_ in OV: inputs += ['-loop', '1', '-t', '36', '-i', p]
fc = []; last = '0:v'
for k, (p, s, e, fd) in enumerate(OV, 1):
    fc.append(f'[{k}:v]format=rgba,fade=t=in:st={s}:d={fd}:alpha=1,fade=t=out:st={e-fd}:d={fd}:alpha=1[o{k}]')
    fc.append(f'[{last}][o{k}]overlay=0:0:enable=\'between(t,{s},{e})\'[v{k}]'); last = f'v{k}'
run(['ffmpeg', '-y', '-v', 'error', *inputs, '-filter_complex', ';'.join(fc), '-map', f'[{last}]', *ENC, 'seg/tmp.mp4'])
os.replace('seg/tmp.mp4', 'seg/video.mp4')

# ---------- audio ----------
run(['ffmpeg', '-y', '-v', 'error', '-i', 'ad_vo.wav', '-i', 'ad_music2.wav', '-filter_complex',
     '[1:a]volume=0.32,afade=t=in:d=0.6,afade=t=out:st=34:d=2[m];[0:a]asplit[v1][v2];[m][v2]sidechaincompress=threshold=0.04:ratio=6:attack=20:release=400[md];'
     '[v1][md]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5[a]', '-map', '[a]', '-ar', '48000', 'seg/audio.wav'])
run(['ffmpeg', '-y', '-v', 'error', '-i', 'seg/video.mp4', '-i', 'seg/audio.wav', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
     '-shortest', 'seg/tmp.mp4'])
os.replace('seg/tmp.mp4', 'oceanic-system-ad-v2.mp4')
print('done')
