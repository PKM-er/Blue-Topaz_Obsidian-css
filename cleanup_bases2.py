import re

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Match only scheme-specific tweaks blocks (not the global /*Bases*/ block)
tweak_pattern = re.compile(
    r'/\*Bases[^*]+tweak[^*]*\*/\n(?:  --(?:bases-table-|table-)[^;]+;\n?)+',
    re.DOTALL
)

namemap = {
    'avocado': 'avocado', 'monochrome': 'monochrome', 'pink': 'pink',
    'topaz-nord': 'nord', 'flamingo': 'flamingo', 'honey-milk': 'honey',
    'chocolate': 'chocolate', 'lilac': 'lilac', 'lillimon': 'lillimon',
    'simplicity': 'simplicity', 'autumn': 'autumn',
}

def find_scheme_name(ctx):
    for key, short in namemap.items():
        if key in ctx.lower():
            return short
    return None

def has_var(ctx, var_prefix):
    return f'--{var_prefix}' in ctx

result_parts = []
last_end = 0

for m in tweak_pattern.finditer(content):
    span_start = m.start()
    span_end = m.end()
    
    # Context: up to 3000 chars before to find selector name
    ctx = content[max(0, span_start-3000):span_start]
    block_text = m.group(0)
    
    # Determine scheme
    scheme_name = find_scheme_name(ctx)
    is_dark = '.theme-dark' in ctx
    
    # New comment
    if scheme_name:
        new_comment = f'/*Bases - {scheme_name} tweak*/'
    else:
        new_comment = '/*Bases tweak*/'
    
    block_text = re.sub(r'/\*Bases[^*]+\*/', new_comment, block_text, count=1)
    
    # Process lines
    lines = block_text.split('\n')
    new_lines = []
    header_color_found = False
    
    for line in lines:
        stripped = line.strip()
        # Remove duplicates matching global values
        if stripped == '--bases-table-header-background: var(--background-secondary-alt);':
            continue
        if stripped == '--bases-table-group-background: transparent;':
            continue
        if stripped.startswith('--bases-table-header-color:'):
            header_color_found = True
            if not is_dark:
                new_lines.append(line)  # keep for light mode
            # For dark, we'll add low-color below
            continue
        if stripped.startswith('--bases-table-stripe-color:') and is_dark:
            # In dark schemes, stripe can use same accent hsla as global
            # Only remove if exactly matches global dark value
            if 'hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.08)' in stripped:
                continue
        new_lines.append(line)
    
    # Dark mode header-color
    if is_dark and not header_color_found:
        # Check if scheme defines --low-color
        has_low = has_var(content[max(0, span_start-4000):span_start], 'low-color')
        color = 'var(--low-color)' if has_low else 'var(--text-accent)'
        new_lines.append(f'  --bases-table-header-color: {color};')
    elif is_dark and header_color_found:
        has_low = has_var(content[max(0, span_start-4000):span_start], 'low-color')
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