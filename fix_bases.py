import re

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'r', encoding='utf-8') as f:
    content = f.read()

# === Fix 1: Make .bases-tr:hover stronger with !important ===
old_hover = '.bases-tr:hover,\n.bases-tbody .bases-tr:nth-child(even):hover {\n  background: var(--bases-table-row-background-hover);\n}'
new_hover = '.bases-tr:hover,\n.bases-tbody .bases-tr:nth-child(even):hover {\n  background: var(--bases-table-row-background-hover) !important;\n}'
assert old_hover in content, 'Cannot find hover block'
content = content.replace(old_hover, new_hover)

# === Fix 2: Improve global .theme-light and .theme-dark bases variables ===
# .theme-light block: replace --bases-table-row-background-hover and add --bases-table-stripe-color
old_light_bases = (
    '  --bases-table-border-color: var(--background-modifier-border);\n'
    '  --bases-table-column-border-width: 0px;\n'
    '  --bases-table-row-border-width: 1px;\n'
    '  --bases-table-row-background-hover: var(--background-modifier-hover);\n'
    '  --bases-table-row-height: 32px;\n'
    '  --bases-table-text-size: var(--font-text-size);\n'
    '  --bases-table-cell-background-active: var(--text-accent-hover);\n'
    '  --bases-table-cell-shadow-active: 0 0 0 1px var(--interactive-accent);\n'
    '}'
)
new_light_bases = (
    '  --bases-table-border-color: var(--background-modifier-border);\n'
    '  --bases-table-column-border-width: 0px;\n'
    '  --bases-table-row-border-width: 1px;\n'
    '  --bases-table-stripe-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.06);\n'
    '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.15);\n'
    '  --bases-table-row-height: 32px;\n'
    '  --bases-table-text-size: var(--font-text-size);\n'
    '  --bases-table-cell-background-active: var(--text-accent-hover);\n'
    '  --bases-table-cell-shadow-active: 0 0 0 1px var(--interactive-accent);\n'
    '}'
)
assert old_light_bases in content, 'Cannot find light bases block'
content = content.replace(old_light_bases, new_light_bases)

# .theme-dark block: same fix
old_dark_bases = (
    '  --bases-table-border-color: var(--background-modifier-border);\n'
    '  --bases-table-column-border-width: 0px;\n'
    '  --bases-table-row-border-width: 1px;\n'
    '  --bases-table-row-background-hover: var(--background-modifier-hover);\n'
    '  --bases-table-row-height: 32px;\n'
    '  --bases-table-text-size: var(--font-text-size);\n'
    '  --bases-table-cell-background-active: var(--text-accent-hover);\n'
    '  --bases-table-cell-shadow-active: 0 0 0 1px var(--interactive-accent);\n'
    '}'
)
# Find the second occurrence (in .theme-dark block)
first = content.find(old_dark_bases)
assert first != -1, 'Cannot find dark bases block (first)'
second = content.find(old_dark_bases, first + 1)
assert second != -1, 'Cannot find dark bases block (second)'

new_dark_bases = (
    '  --bases-table-border-color: var(--background-modifier-border);\n'
    '  --bases-table-column-border-width: 0px;\n'
    '  --bases-table-row-border-width: 1px;\n'
    '  --bases-table-stripe-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.06);\n'
    '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.15);\n'
    '  --bases-table-row-height: 32px;\n'
    '  --bases-table-text-size: var(--font-text-size);\n'
    '  --bases-table-cell-background-active: var(--text-accent-hover);\n'
    '  --bases-table-cell-shadow-active: 0 0 0 1px var(--interactive-accent);\n'
    '}'
)
content = content[:second] + content[second:].replace(old_dark_bases, new_dark_bases, 1)

# === Fix 3: Rewrite scheme-specific bases tweaks to use theme accent colors ===
# The Python script earlier inserted blocks like:
#   /*Bases - color-base*/
#   ...
#   /*Bases - tweaks*/
#   --bases-table-border-color: #ededed;
#   --bases-table-header-background: #f1f1f1;
#   --bases-table-row-background-hover: #f6f6f6;

# We need to replace the /*Bases - tweaks*/ blocks with accent-based versions.

# Pattern to find scheme tweaks (the ones with hardcoded hex colors)
scheme_blocks = [
    'avocado-light', 'avocado-dark',
    'monochrome-dark', 'monochrome-light',
    'pink-light', 'pink-dark',
    'nord-light', 'nord-dark'
]

for name in scheme_blocks:
    # The tweaks block looks like:
    #   /*Bases - tweaks*/
    #   --bases-table-border-color: #xxxxxx;
    #   --bases-table-header-background: #xxxxxx;
    #   --bases-table-row-background-hover: #xxxxxx;
    
    # Find this pattern
    old_tweak = re.search(
        r'(\s*/\*Bases - tweaks\*/\s*\n\s*--bases-table-border-color:\s*#[a-f0-9]+;\s*\n\s*--bases-table-header-background:\s*#[a-f0-9]+;\s*\n\s*--bases-table-row-background-hover:\s*#[a-f0-9]+;)',
        content
    )
    
    if not old_tweak:
        print(f'{name}: tweak block not found')
        continue
    
    indent = '  '
    new_tweak = (
        f'{indent}/*Bases - tweaks*/\n'
        f'{indent}--bases-table-stripe-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.08);\n'
        f'{indent}--bases-table-header-background: var(--background-secondary-alt);\n'
        f'{indent}--bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.18);\n'
        f'{indent}--bases-table-header-color: var(--text-accent);'
    )
    
    content = content.replace(old_tweak.group(0), new_tweak, 1)
    print(f'{name}: replaced')

# === Fix 4: Update the Autumn tweaks block too (keep unique but enhance) ===
# Autumn already uses its custom colors, which is fine. But add --bases-table-stripe-color if missing.
# Skip for now - Autumn already has custom stripe color.

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print('Done')