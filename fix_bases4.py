import re

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Global blocks - change --bases-table-header-background to transparent
old_global = (
    '  --bases-table-header-color: var(--text-accent);\n'
    '  --bases-table-header-background: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.10);'
)
new_global = (
    '  --bases-table-header-color: var(--text-accent);\n'
    '  --bases-table-header-background: transparent;'
)
count = content.count(old_global)
content = content.replace(old_global, new_global)
print(f'Fixed {count} global header backgrounds')

# Fix 2: Scheme tweaks blocks - change to transparent
old_scheme = (
    '  --bases-table-header-background: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.12);\n'
    '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.18);'
)
new_scheme = (
    '  --bases-table-header-background: transparent;\n'
    '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.18);'
)
count2 = content.count(old_scheme)
content = content.replace(old_scheme, new_scheme)
print(f'Fixed {count2} scheme header backgrounds')

# Fix 3: Ensure .bases-group-heading has transparent background explicitly
old_group = '.bases-group-heading {\n  font-weight: 600;\n  font-size: 0.9em;\n  color: var(--text-normal);\n  padding: 6px 0;\n  border-bottom: 1px solid var(--bases-table-border-color);\n  margin-bottom: 8px;\n  display: flex;\n  align-items: center;\n  gap: 6px;\n}'
new_group = '.bases-group-heading {\n  font-weight: 600;\n  font-size: 0.9em;\n  color: var(--text-normal);\n  padding: 6px 0;\n  border-bottom: 1px solid var(--bases-table-border-color);\n  margin-bottom: 8px;\n  display: flex;\n  align-items: center;\n  gap: 6px;\n  background: transparent;\n}'
content = content.replace(old_group, new_group)
print('Added transparent bg to .bases-group-heading')

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print('Done')