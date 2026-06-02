import re

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Only fix --bases-table-header-background to transparent (NOT affecting Autumn's var(--bg-color2))

# Global blocks: hsla(accent, 0.10) → transparent
old_global = '--bases-table-header-background: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.10);'
new_global = '--bases-table-header-background: transparent;'
c1 = content.count(old_global)
content = content.replace(old_global, new_global)
print(f'Global blocks: {c1}')

# Scheme tweaks: hsla(accent, 0.12) → transparent
old_scheme = '--bases-table-header-background: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.12);'
new_scheme = '--bases-table-header-background: transparent;'
c2 = content.count(old_scheme)
content = content.replace(old_scheme, new_scheme)
print(f'Scheme tweaks: {c2}')

# Verify Autumn still has var(--bg-color2)
assert '--bases-table-header-background: var(--bg-color2);' in content, 'Autumn value missing!'
print('Autumn var(--bg-color2) preserved')

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

# Also fix obsidian.css (it has the same --bases-table-header-background values)
print('\n--- obsidian.css ---')
with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\obsidian.css', 'r', encoding='utf-8') as f:
    oc = f.read()
# In obsidian.css the scheme tweaks might use different patterns
# Just replace any hsla(accent, 0.10) header backgrounds
oc = oc.replace(old_global, new_global)
oc = oc.replace(old_scheme, new_scheme)
with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\obsidian.css', 'w', encoding='utf-8', newline='\n') as f:
    f.write(oc)
print('obsidian.css done')
print('All done')