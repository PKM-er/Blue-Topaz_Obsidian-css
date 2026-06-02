import re

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'r', encoding='utf-8') as f:
    content = f.read()

# For each scheme-specific tweak block, determine if it's dark mode.
# We'll look at the block after the tweak (within same selector scope) to find .theme-dark

# Find all tweaks blocks again
pattern = re.compile(
    r'(/\*Bases[^*]+tweak\*/\n(?:  --[^;]+;\n?)+)',
    re.DOTALL
)

def is_block_dark(content, block_start, block_end):
    """Check if the parent selector includes .theme-dark"""
    # Look backwards up to 2000 chars for .theme-dark
    ctx = content[max(0, block_start-2000):block_start]
    # Also check forward for the closing } and see if .theme-dark was the selector
    fwd = content[block_end:block_end+3000]
    # Look for .theme-dark in surrounding area
    if '.theme-dark' in ctx:
        return True
    if '.theme-dark' in fwd[:500]:
        return True
    return False

def scheme_has_low_color(content, block_start):
    ctx = content[max(0, block_start-5000):block_start]
    return '--low-color' in ctx

result_parts = []
last_end = 0

for m in pattern.finditer(content):
    span_start = m.start()
    span_end = m.end()
    block_text = m.group(0)
    
    is_dark = is_block_dark(content, span_start, span_end)
    has_low = scheme_has_low_color(content, span_start)
    
    if not is_dark:
        result_parts.append(content[last_end:span_end])
        last_end = span_end
        continue
    
    # For dark blocks: replace header-color line
    lines = block_text.split('\n')
    new_lines = []
    header_replaced = False
    
    for line in lines:
        if line.strip().startswith('--bases-table-header-color:'):
            color = 'var(--low-color)' if has_low else 'var(--text-accent)'
            new_lines.append(f'  --bases-table-header-color: {color};')
            header_replaced = True
        else:
            new_lines.append(line)
    
    if not header_replaced:
        color = 'var(--low-color)' if has_low else 'var(--text-accent)'
        new_lines.append(f'  --bases-table-header-color: {color};')
    
    result_parts.append(content[last_end:span_start])
    result_parts.append('\n'.join(new_lines))
    last_end = span_end

result_parts.append(content[last_end:])
output = ''.join(result_parts)

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'w', encoding='utf-8', newline='\n') as f:
    f.write(output)

print('Done')