import glob
import re

def update_html_files(directory, project_name):
    html_files = glob.glob(f'{directory}/*.html')
    for fpath in html_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Add analytics.js if not present
        if 'js/analytics.js' not in content:
            content = content.replace('</head>', '  <script src="js/analytics.js" defer></script>\n</head>')

        # 2. Update footer legal links
        # Match pattern like <a href="#">Aviso Legal</a> or similar
        old_footer_links = re.search(r'<div style="display:\s*flex;\s*gap:\s*1\.5rem;">\s*<a href="#">Aviso Legal</a>[\s\S]*?</div>', content)
        if old_footer_links:
            new_footer_links = """<div style="display: flex; gap: 1.5rem; flex-wrap: wrap;">
          <a href="aviso-legal.html">Aviso Legal</a>
          <a href="politica-privacidad.html">Política de Privacidad</a>
          <a href="politica-cookies.html">Política de Cookies</a>
          <a href="#cookies-config" class="open-cookie-settings">Configurar Cookies</a>
        </div>"""
            content = content.replace(old_footer_links.group(0), new_footer_links)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'[{project_name}] Updated {fpath}')

update_html_files(r'c:\Users\edgvi\Documents\webleadsagent', 'Reformas Bañuls')
update_html_files(r'C:\Users\edgvi\Documents\ventanasbanuls', 'Ventanas Bañuls')
print('All HTML files updated with GA4 & Legal links!')
