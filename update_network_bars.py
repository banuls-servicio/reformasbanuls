import glob
import re

files_webleads = glob.glob(r'c:\Users\edgvi\Documents\webleadsagent\*.html')
files_ventanas = glob.glob(r'C:\Users\edgvi\Documents\ventanasbanuls\*.html')

for fpath in files_webleads:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    # update network bar label and text
    c = re.sub(
        r'<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*0\.5rem;">\s*<span style="color:\s*#64748B;">Familia Bañuls Alcoy · Desde 1964:</span>',
        r'<div class="network-bar-label">\n        <span style="color: #64748B;">Familia Bañuls Alcoy · Desde 1964:</span>',
        c
    )
    c = re.sub(
        r'🪟 Ventanas &amp; Aislamiento Térmico \(ventanasbañuls\.com\)',
        r'🪟 Ventanas Bañuls',
        c
    )
    c = re.sub(
        r'🔨 Reformas &amp; Interiorismo \(reformasbañuls\.com\)',
        r'🔨 Reformas Bañuls',
        c
    )
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
print('Updated webleadsagent HTML files')

for fpath in files_ventanas:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(
        r'<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*0\.5rem;">\s*<span style="color:\s*#64748B;">Familia Bañuls Alcoy · Desde 1964:</span>',
        r'<div class="network-bar-label">\n        <span style="color: #64748B;">Familia Bañuls Alcoy · Desde 1964:</span>',
        c
    )
    c = re.sub(
        r'🪟 Ventanas &amp; Aislamiento Térmico \(ventanasbañuls\.com\)',
        r'🪟 Ventanas Bañuls',
        c
    )
    c = re.sub(
        r'🔨 Reformas &amp; Interiorismo \(reformasbañuls\.com\)',
        r'🔨 Reformas Bañuls',
        c
    )
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
print('Updated ventanasbanuls HTML files')
