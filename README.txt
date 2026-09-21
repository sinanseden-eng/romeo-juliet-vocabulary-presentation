# Romeo & Juliet Association Deck Photo Bundle

This bundle contains the PowerPoint photos extracted and prepared for the `Association Deck` flashcards of the GitHub presentation.

## Contents
- `assets/flashcards/` → extracted photos from the PowerPoint
- `flashcard_image_map.json` → chosen image mapping for each word
- `flashcard_image_map.js` → JavaScript object to paste into `index.html`
- `association_deck_front_replacement.txt` → the new front-face code for the flashcards
- `patch_index_for_flashcards.py` → an automated patch script for `index.html`
- `contact_sheet_reference.jpg` → quick visual overview of the extracted images

## What this changes
Only the `Association Deck` flashcards are affected.
- The flashcard FRONT will show the PowerPoint photo(s)
- The flashcard BACK remains unchanged
- The Lexicon / Duel / Act 1 Lines tabs are untouched

## How to use
1. Download or open your current repository.
2. Copy the `assets/flashcards` folder into the repository root so the final path becomes:
   `your-repo/assets/flashcards/...`
3. Put your current `index.html` beside the patch script.
4. Run:
   `python patch_index_for_flashcards.py`
5. Replace the old `index.html` with the patched one (the script creates `index.patched.html`).
6. Preview locally or push to GitHub.

## Notes
- One website card (`foe`) and one card (`adversity`) were split from a single PowerPoint slide, so the most suitable images were assigned manually.
- `vain` had only one clearly useful image, so that flashcard uses one photo.
