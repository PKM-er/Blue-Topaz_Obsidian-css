import re

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'r', encoding='utf-8') as f:
    content = f.read()

# === Fix 1: Replace all scheme tweaks blocks (hex-based) with accent-based ===
# Pattern matches: /*Bases - tweaks*/ \n ... three hex-based variables
pattern = re.compile(
    r'(  /\*Bases - tweaks\*/\n'
    r'  --bases-table-border-color: (#[a-f0-9]+);\n'
    r'  --bases-table-header-background: (#[a-f0-9]+);\n'
    r'  --bases-table-row-background-hover: (#[a-f0-9]+);)'
)

count = 0
def replacer(m):
    global count
    count += 1
    return (
        '  /*Bases - tweaks*/\n'
        '  --bases-table-stripe-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.08);\n'
        '  --bases-table-header-background: var(--background-secondary-alt);\n'
        '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.18);\n'
        '  --bases-table-header-color: var(--text-accent);'
    )

content = pattern.sub(replacer, content)
print(f'Replaced {count} scheme tweaks blocks')

# === Fix 2: Global .theme-dark and .theme-light bases variables ===
# In .theme-dark block (first occurrence): replace hover with accent-based
# In .theme-light block (second occurrence): same

# Pattern for hover in global blocks
old_hover = '  --bases-table-row-background-hover: var(--background-modifier-hover);'
new_hover = '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.15);'

# Replace both occurrences
content = content.replace(old_hover, new_hover, 2)
assert 'var(--background-modifier-hover)' not in [l for l in content.split('\n') if '--bases-table-row-background-hover' in l], 'Still has old hover values'
print('Replaced global hover values')

# Add --bases-table-stripe-color before hover in global blocks
old_stripe_slot = (
    '  --bases-table-row-border-width: 1px;\n'
    '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.15);'
)
new_stripe_slot = (
    '  --bases-table-row-border-width: 1px;\n'
    '  --bases-table-stripe-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.06);\n'
    '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.15);'
)
content = content.replace(old_stripe_slot, new_stripe_slot, 2)
print('Added stripe color to global blocks')

# === Fix 3: Add !important to hover rules ===
old_hover_rule = (
    '.bases-tr:hover,\n'
    '.bases-tbody .bases-tr:nth-child(even):hover {\n'
    '  background: var(--bases-table-row-background-hover);\n'
    '}'
)
new_hover_rule = (
    '.bases-tr:hover,\n'
    '.bases-tbody .bases-tr:nth-child(even):hover {\n'
    '  background: var(--bases-table-row-background-hover) !important;\n'
    '}'
)
if old_hover_rule in content:
    content = content.replace(old_hover_rule, new_hover_rule)
    print('Added !important to hover rules')
else:
    print('Hover rule not found')

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print('Done')