import re

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix: Replace all scheme tweaks blocks with improved values
old_pattern = re.compile(
    r'(  /\*Bases - tweaks\*/\n'
    r'  --bases-table-stripe-color: hsla\(var\(--accent-h\), var\(--accent-s\), var\(--accent-l\), 0\.08\);\n'
    r'  --bases-table-header-background: var\(--background-secondary-alt\);\n'
    r'  --bases-table-row-background-hover: hsla\(var\(--accent-h\), var\(--accent-s\), var\(--accent-l\), 0\.18\);\n'
    r'  --bases-table-header-color: var\(--text-accent\);)'
)

count = 0
def replacer(m):
    global count
    count += 1
    return (
        '  /*Bases - tweaks*/\n'
        '  --bases-table-stripe-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.08);\n'
        '  --bases-table-header-background: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.12);\n'
        '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.18);\n'
        '  --bases-table-header-color: var(--text-accent);\n'
        '  --table-border-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.22);'
    )

content = old_pattern.sub(replacer, content)
print(f'Replaced {count} scheme tweaks blocks')

# Also fix global theme-light's bases header background
# Currently it has --bases-table-header-background: var(--background-secondary)
# Change to hsla accent
old_global_header = (
    '  --bases-table-header-color: var(--text-normal);\n'
    '  --bases-table-header-background: var(--background-secondary);\n'
    '  --bases-table-header-background-hover: var(--background-modifier-hover);'
)
new_global_header = (
    '  --bases-table-header-color: var(--text-accent);\n'
    '  --bases-table-header-background: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.10);\n'
    '  --bases-table-header-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.18);'
)
content = content.replace(old_global_header, new_global_header, 2)
print('Replaced global header backgrounds')

# Also add --table-border-color to global blocks
old_global_table_slot = (
    '  --bases-table-header-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.18);\n'
    '  --bases-table-border-color: var(--background-modifier-border);\n'
    '  --bases-table-column-border-width: 0px;'
)
new_global_table_slot = (
    '  --bases-table-header-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.18);\n'
    '  --table-border-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.20);\n'
    '  --bases-table-border-color: var(--background-modifier-border);\n'
    '  --bases-table-column-border-width: 0px;'
)
count2 = content.count(old_global_table_slot)
content = content.replace(old_global_table_slot, new_global_table_slot)
print(f'Added table-border-color to {count2} global blocks')

# Fix Autumn: keep its unique tweaks but add --table-border-color
# Find Autumn's tweaks block
autumn_tweak = (
    '  /*Bases - autumn tweaks*/\n'
    '  --bases-table-border-color: #bfb9a0;\n'
    '  --table-border-color: #c5b896;'
)
# Already has --table-border-color, so no change needed

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print('Done')