# Speech Bubble 10-Color Loop Design

## Goal

Make all numbered speech bubbles form one continuous visual color loop. Each bubble starts at its own computed base color and ends at the next numbered bubble's base color.

## Scope

- Keep the ten `background` mappings as a strict closed loop.
- Convert `--bt-speech-8` and `--bt-speech-9` from nested gradients into real OKLCH base colors. Preserve colors 0–7 and derive 8 and 9 at `+320deg` and `+340deg` from the scheme hue.
- Preserve bubble geometry, checkbox hiding, and the Style Settings toggle.
- Enforce a 2px vertical margin on CodeMirror speech-bubble lines with enough specificity to override Obsidian's `margin: 0 !important` editor rule.
- Do not modify the two untracked CSS reference files in the repository root.

## Gradient mapping

| Bubble | Gradient |
| --- | --- |
| 0 | `--bt-speech-0` to `--bt-speech-1` |
| 1 | `--bt-speech-1` to `--bt-speech-2` |
| 2 | `--bt-speech-2` to `--bt-speech-3` |
| 3 | `--bt-speech-3` to `--bt-speech-4` |
| 4 | `--bt-speech-4` to `--bt-speech-5` |
| 5 | `--bt-speech-5` to `--bt-speech-6` |
| 6 | `--bt-speech-6` to `--bt-speech-7` |
| 7 | `--bt-speech-7` to `--bt-speech-8` |
| 8 | `--bt-speech-8` to `--bt-speech-9` |
| 9 | `--bt-speech-9` to `--bt-speech-0` |

All gradients remain horizontal (`90deg`) and use the current `!important` precedence.

## Validation

1. Inspect the ten CSS mappings to ensure the complete 0-to-9 ring is present exactly once.
2. Confirm that `--bt-speech-8` and `--bt-speech-9` resolve to solid colors in both light and dark engines, rather than nested gradients.
3. Confirm in Obsidian that bubbles 7–9 have non-empty computed backgrounds and adjacent bubble rectangles have a 2px gap.
4. Copy the updated `theme.css` to `E:\\Obsidian\\all-in-one\\.obsidian\\themes\\Blue Topaz Alternate` and compare the deployed file with the repository version.
5. Check repository status to ensure the existing untracked reference files remain untouched.
