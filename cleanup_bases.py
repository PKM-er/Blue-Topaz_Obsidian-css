import re

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'r', encoding='utf-8') as f:
    content = f.read()

# All dark theme selectors and their display names
schemes = [
    ('autumn-topaz.theme-dark',       'Autumn 暗夜'),
    ('avocado-topaz.theme-dark',      'Avocado 暗夜'),
    ('monochrome-topaz.theme-dark',   'Monochrome 暗夜'),
    ('pink-topaz.theme-dark',         'Pink 暗夜'),
    ('topaz-nord.theme-dark',         'Nord 暗夜'),
    ('flamingo.theme-dark',           'Flamingo 暗夜'),
    ('honey-milk-topaz.theme-dark',   'Honey milk 暗夜'),
    ('chocolate-topaz.theme-dark',    'Chocolate 暗夜'),
    ('lilac.theme-dark',              'Lilac 暗夜'),
    ('lillimon-topaz.theme-dark',     'Lillimon 暗夜'),
    ('simplicity-topaz.theme-dark',   'Simplicity 暗夜'),
]

for sel, name in schemes:
    idx = content.find('body.color-scheme-options-' + sel)
    if idx == -1:
        print(f'{name}: NOT FOUND')
        continue
    
    # Find the Bases tweak block for this scheme
    # Pattern: /*Bases tweak*/ or /*Bases - xxx - tweak*/
    after_brace = content.find('{', idx)
    close_brace = content.find('}', after_brace)
    # But we need the correct close brace (nested)
    depth = 0
    close = after_brace
    for i in range(after_brace, len(content)):
        if content[i] == '{': depth += 1
        elif content[i] == '}':
            depth -= 1
            if depth == 0:
                close = i
                break
    
    block = content[after_brace:close]
    # Find the tweaks section within this block
    tweak_start = block.find('/*Bases')
    if tweak_start == -1:
        print(f'{name}: no Bases section')
        continue
    
    # Get current tweaks content up to the closing }
    tweak_end = close - after_brace
    tweak_block = block[tweak_start:tweak_end]
    
    # Standard dark tweaks:
    new_tweak = (
        f'  /*Bases - {name} - tweak*/\n'
        '  --bases-table-stripe-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.08);\n'
        '  --bases-table-header-background: var(--background-secondary-alt);\n'
        '  --bases-table-group-background: transparent;\n'
        '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.18);\n'
        '  --bases-table-header-color: var(--low-color);\n'
        '  --table-border-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.22);'
    )
    
    # Replace the tweaks block
    # Find the exact old tweaks in content
    old_tweak_pattern = re.compile(
        r'  /\*Bases[^*]*\*/\n(?:  --[^;\n]+;\n)*',
        re.MULTILINE
    )
    # Find it in the block at tweak_start position
    block_lines = block.split('\n')
    i = 0
    start_line = None
    for j, line in enumerate(block_lines):
        if line.strip().startswith('/*Bases'):
            start_line = j
        elif start_line is not None and line.strip().startswith('--'):
            continue
        elif start_line is not None:
            # End of tweaks block
            end_line = j
            break
    
    if start_line is None:
        print(f'{name}: cannot locate tweak')
        continue
    
    # Find end of tweaks (first non -- line or } line)
    for k in range(start_line + 1, len(block_lines)):
        line = block_lines[k].strip()
        if line.startswith('}') or (line and not line.startswith('--') and not line.startswith('/*')):
            end_line = k
            break
    
    old_lines = block_lines[start_line:end_line]
    old_text = '\n'.join(old_lines)
    
    # Replace in content
    pos = content.find(old_text, idx)
    if pos != -1:
        content = content[:pos] + new_tweak + content[pos + len(old_text):]
        print(f'{name}: updated')
    else:
        print(f'{name}: text not found in content')

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print('Done')