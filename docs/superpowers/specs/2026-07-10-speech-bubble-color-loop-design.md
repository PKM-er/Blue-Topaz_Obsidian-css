# Speech Bubble Color Engine Design

## Goal

Render `- [0]` through `- [9]` as a continuous, theme-aware speech-bubble color loop without changing ordinary or alternative checkbox states.

## Color engine

- Keep one shared engine next to the speech-bubble component styles.
- Derive the starting hue from `--accent-h`, with `350` as a defensive fallback.
- Divide the hue wheel into ten equal 36-degree steps.
- Generate ten solid OKLCH tones and mix them with the current theme surface.
- Keep light- and dark-mode chroma, lightness, mix weight, text color, and surface color as mode-specific variables.
- Map each numbered bubble from its tone to the next tone, closing the ring with `9 -> 0`.

The Monochrome scheme sets chroma to zero and varies tone lightness in a closed dark-to-light-to-dark sequence. This preserves a visible ten-state loop without introducing color into a monochrome palette.

## Component scope

Geometry and background rules apply only to:

- `li.task-list-item` elements whose `data-task` is `0` through `9`.
- `.HyperMD-task-line` elements whose `data-task` is `0` through `9`.

Checkbox inputs and all other task states remain untouched. The CodeMirror spacing override uses the same numeric-state restriction.

Bubble indentation, padding, gap, radius, and gradient angle are internal custom properties with defaults matching the existing appearance. They remain overrideable without adding more Style Settings controls.

## Validation

1. Run static assertions before and after implementation to prove the original failures and the corrected scope.
2. Confirm the ten mappings form exactly `0 -> 1 -> ... -> 9 -> 0`.
3. Confirm the shared engine uses 36-degree hue steps and no speech variables remain under inline-code selectors.
4. In Obsidian, verify reading and live-preview modes in light and dark mode for the default palette and every named palette.
5. Confirm ordinary and alternative checkbox states keep their original spacing and styling.
6. Keep the alternative-checkbox snippet enabled while verifying rounded bubble geometry.
7. Inspect the Monochrome result visually and tune only the gray lightness range if necessary.

## PR hygiene

- Keep repository documentation portable and free of contributor-specific vault paths.
- Do not commit local reference snippets or vault deployment files.
- Describe the Style Settings toggle with literal Obsidian syntax: `- [0]` through `- [9]`.
