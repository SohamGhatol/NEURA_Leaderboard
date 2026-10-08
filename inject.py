import sys
import re

css_files = ['./styles/neura-core.css', './styles/neura-shell.css', './styles/neura-components.css']
css_content = ''
for f in css_files:
    with open(f, 'r', encoding='utf-8') as file:
        css_content += file.read() + '\n'

html_file = 'leaderboard.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the specific links with the styles
pattern = r'<link\s+rel="stylesheet"\s+href="\./styles/neura-[^"]+\.css\?v=3">\s*'
html = re.sub(pattern, '', html)

# Insert the styles right before <style>
html = html.replace('<style>', '<style>\n' + css_content + '\n', 1)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print('Successfully injected CSS')
