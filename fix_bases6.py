import re

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix all --bases-table-stripe-color references to also set --bases-table-group-background
# This variable is used by Obsidian's .bases-table-group-summary-row with default: var(--background-primary-alt) = #e9e9e9

# 1. Global .theme-light / .theme-dark bases block
old_global = (
    '  --bases-table-stripe-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.06);\n'
    '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.15);\n'
    '  --bases-table-row-height: 32px;'
)
new_global = (
    '  --bases-table-stripe-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.06);\n'
    '  --bases-table-group-background: transparent;\n'
    '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.15);\n'
    '  --bases-table-row-height: 32px;'
)
c1 = content.count(old_global)
content = content.replace(old_global, new_global)
print(f'Global blocks: {c1}')

# 2. Scheme tweaks blocks (the ones with hsla accent values)
old_scheme = (
    '  --bases-table-stripe-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.08);\n'
    '  --bases-table-header-background: transparent;\n'
    '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.18);'
)
new_scheme = (
    '  --bases-table-stripe-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.08);\n'
    '  --bases-table-header-background: transparent;\n'
    '  --bases-table-group-background: transparent;\n'
    '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.18);'
)
c2 = content.count(old_scheme)
content = content.replace(old_scheme, new_scheme)
print(f'Scheme tweaks: {c2}')

# 3. Autumn light: add --bases-table-group-background
old_autumn_light = (
    '  /*Bases - autumn tweaks*/\n'
    '  --bases-table-border-color: #bfb9a0;\n'
    '  --table-border-color: #c5b896;\n'
    '  --bases-table-header-color: var(--deep-color);\n'
    '  --bases-table-header-background: var(--bg-color2);\n'
    '  --bases-table-row-background-hover: color-mix(in srgb, var(--color1) 80%, #aaa);\n'
    '  --bases-table-stripe-color: color-mix(in srgb, var(--color2) 20%, transparent);'
)
new_autumn_light = (
    '  /*Bases - autumn tweaks*/\n'
    '  --bases-table-border-color: #bfb9a0;\n'
    '  --table-border-color: #c5b896;\n'
    '  --bases-table-header-color: var(--deep-color);\n'
    '  --bases-table-header-background: var(--bg-color2);\n'
    '  --bases-table-group-background: transparent;\n'
    '  --bases-table-row-background-hover: color-mix(in srgb, var(--color1) 80%, #aaa);\n'
    '  --bases-table-stripe-color: color-mix(in srgb, var(--color2) 20%, transparent);'
)
c3 = content.count(old_autumn_light)
content = content.replace(old_autumn_light, new_autumn_light)
print(f'Autumn light: {c3}')

# 4. Autumn dark: add --bases-table-group-background (currently missing from this block)
old_autumn_dark = (
    '  /*Bases - autumn tweaks*/\n'
    '  --bases-table-header-background: #333333;\n'
    '  --bases-table-row-background-hover: #2a2a2a;\n'
)
new_autumn_dark = (
    '  /*Bases - autumn tweaks*/\n'
    '  --bases-table-header-background: #333333;\n'
    '  --bases-table-group-background: transparent;\n'
    '  --bases-table-row-background-hover: #2a2a2a;\n'
)
c4 = content.count(old_autumn_dark)
content = content.replace(old_autumn_dark, new_autumn_dark)
print(f'Autumn dark: {c4}')

assert '--bases-table-group-background' in content, 'Group background NOT added!'
print('Variable present in file')

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print('Done')