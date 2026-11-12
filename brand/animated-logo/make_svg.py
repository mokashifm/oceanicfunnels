import math
D=2.4  # loop seconds
def wave(phase, n=64):
    pts=[]
    for i in range(n+1):
        x=10+80*i/n
        e=min(1,(x-10)/9,(90-x)/9); e=0.35+0.65*(e*e*(3-2*e))
        y=22-4.6*e*math.sin(2*math.pi*(x-10)/40 - phase)
        pts.append(f"{x:.2f} {y:.2f}")
    return "M"+" L".join(pts)
K=24
vals=";".join(wave(2*math.pi*k/K) for k in range(K+1))
def bar(x,y,w,c,delay):
    # breathe: widen 10% and back, staggered
    g=w*0.10
    kt="0;{a:.3f};{b:.3f};{c:.3f};1".format(a=delay/D,b=(delay+0.35)/D,c=(delay+0.7)/D)
    return f'''<rect x="{x}" y="{y}" width="{w}" height="10" rx="5" fill="{c}">
    <animate attributeName="width" dur="{D}s" repeatCount="indefinite" keyTimes="{kt}" values="{w};{w};{w+2*g:.2f};{w};{w}" calcMode="spline" keySplines="0 0 1 1;.4 0 .2 1;.4 0 .2 1;0 0 1 1"/>
    <animate attributeName="x" dur="{D}s" repeatCount="indefinite" keyTimes="{kt}" values="{x};{x};{x-g:.2f};{x};{x}" calcMode="spline" keySplines="0 0 1 1;.4 0 .2 1;.4 0 .2 1;0 0 1 1"/>
  </rect>'''
longwave=' '.join(['M-70 22']+['c6.7 -6 13.3 -6 20 0 c6.7 6 13.3 6 20 0']*6)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 104" width="400" height="416" role="img" aria-label="Oceanic Funnels animated logo">
  <defs><linearGradient id="ofg" x1="5" x2="95" y1="0" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".13" stop-color="#fff"/><stop offset=".87" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <mask id="ofw" maskUnits="userSpaceOnUse" x="0" y="0" width="100" height="40"><rect x="5" y="8" width="90" height="28" fill="url(#ofg)"/></mask></defs>
  <g mask="url(#ofw)"><path d="{longwave}" fill="none" stroke="#3DE3C8" stroke-width="9" stroke-linecap="round" stroke-linejoin="round">
    <animateTransform attributeName="transform" type="translate" dur="{D}s" repeatCount="indefinite" from="0 0" to="40 0"/>
  </path></g>
  {bar(18,38,64,"#5FC8E8",0.30)}
  {bar(29,56,42,"#F29A86",0.55)}
  <circle cx="50" cy="88" r="3.6" fill="#FF7657" opacity="0">
    <animate attributeName="cy" dur="{D}s" repeatCount="indefinite" keyTimes="0;0.45;0.75;1" values="79;79;100;100" calcMode="spline" keySplines="0 0 1 1;.5 0 .9 .6;0 0 1 1"/>
    <animate attributeName="opacity" dur="{D}s" repeatCount="indefinite" keyTimes="0;0.45;0.5;0.68;0.75;1" values="0;0;1;1;0;0"/>
  </circle>
  {bar(40,74,20,"#FF7657",0.80)}

</svg>'''
open('oceanic-logo-animated.svg','w').write(svg)
print(len(svg))
