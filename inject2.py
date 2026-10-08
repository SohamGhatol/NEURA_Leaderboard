import sys
import re

js_file = './js/components/wormhole.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Remove 'export ' from functions
js_content = js_content.replace('export function', 'function')

html_file = 'leaderboard.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the module import script block with the inlined js
pattern = r'<script\s+type="module">\s*import\s*{\s*initWormhole\s*}\s*from\s*\'\./js/components/wormhole\.js\';\s*initWormhole\(\);\s*</script>'
inline_script = '<script>\n' + js_content + '\ninitWormhole();\n</script>'
html = re.sub(pattern, inline_script, html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print('Successfully injected JS')
