from pathlib import Path
import re

src = Path('index.html')
if not src.exists():
    raise SystemExit('index.html not found. Put this script in the same folder as index.html and run again.')

html = src.read_text(encoding='utf-8')

image_map_js = Path('flashcard_image_map.js').read_text(encoding='utf-8').strip()
front_replacement_raw = Path('association_deck_front_replacement.txt').read_text(encoding='utf-8')

# 1) insert image map before AudioContext if not already present
if 'const flashcardImageMap =' not in html:
    marker = 'const AudioContext = window.AudioContext || window.webkitAudioContext;'
    if marker not in html:
        raise SystemExit('Could not find the AudioContext marker in index.html.')
    html = html.replace(marker, image_map_js + '\n\n    ' + marker)

# 2) add deckImages line after current item line
needle = 'const item = vocabularyData[currentDeckIndex];'
replace = needle + '\n      const deckImages = flashcardImageMap[item.id] || [];'
if 'const deckImages = flashcardImageMap[item.id] || [];' not in html:
    if needle not in html:
        raise SystemExit('Could not find `const item = vocabularyData[currentDeckIndex];` in renderFlashcard().')
    html = html.replace(needle, replace, 1)

# 3) replace FRONT FACE template
pattern = re.compile(r"""\n\s*// Populate FRONT FACE \(Pre-rotation\)\n\s*front\.innerHTML = `.*?`;\n\n\s*// Populate BACK FACE \(Pre-rotated so flipping displays normal text\)""", re.S)
replacement = '\n      // Populate FRONT FACE (Pre-rotation)\n      ' + front_replacement_raw + '\n\n      // Populate BACK FACE (Pre-rotated so flipping displays normal text)'
html_new, n = pattern.subn(replacement, html, count=1)
if n != 1:
    raise SystemExit('Could not replace the flashcard front template automatically. Please patch manually using association_deck_front_replacement.txt.')

out = Path('index.patched.html')
out.write_text(html_new, encoding='utf-8')
print('Done. Patched file written to', out)
