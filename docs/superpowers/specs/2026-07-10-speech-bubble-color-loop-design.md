# Speech Bubble 10-Color Loop Design

## Goal

Make all numbered speech bubbles form one continuous visual color loop. Each bubble starts at its own computed base color and ends at the next numbered bubble's base color.

## Scope

- Change only the ten `background` gradient mappings in the speech-bubble CSS.
- Preserve the existing per-scheme OKLCH color variables, bubble geometry, spacing, checkbox hiding, and Style Settings toggle.
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
2. Confirm the only functional CSS change is to the mappings for bubbles 7, 8, and 9.
3. Copy the updated `theme.css` to `E:\\Obsidian\\all-in-one\\.obsidian\\themes\\Blue Topaz Alternate` and compare the deployed file with the repository version.
4. Check repository status to ensure the existing untracked reference files remain untouched.
