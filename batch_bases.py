import re

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'r', encoding='utf-8') as f:
    content = f.read()

def lerp_color(c1, c2, t):
    """Linear interpolation between two hex colors"""
    r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
    r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return f'#{r:02x}{g:02x}{b:02x}'

def compute_base_colors(bg_hex, is_dark):
    """Compute --color-base-00 to --color-base-100 from a background color"""
    if is_dark:
        end = '#dadada' if bg_hex < '#888888' else '#ffffff'
    else:
        end = '#202020'
    
    steps = [0.0, 0.02, 0.05, 0.10, 0.15, 0.20, 0.28, 0.40, 0.55, 0.72, 0.85, 1.0]
    names = ['00', '05', '10', '20', '25', '30', '35', '40', '50', '60', '70', '100']
    
    lines = []
    for name, t in zip(names, steps):
        color = lerp_color(bg_hex, end, t)
        lines.append(f'  --color-base-{name}: {color};')
    return '\n'.join(lines)

def compute_bases_tweaks(bg_hex, is_dark):
    """Compute bases tweaks based on background"""
    if is_dark:
        border = lerp_color(bg_hex, '#aaaaaa', 0.25)
        header_bg = lerp_color(bg_hex, '#ffffff', 0.08)
        hover_bg = lerp_color(bg_hex, '#ffffff', 0.05)
    else:
        border = lerp_color(bg_hex, '#888888', 0.15)
        header_bg = lerp_color(bg_hex, '#dddddd', 0.20)
        hover_bg = lerp_color(bg_hex, '#aaaaaa', 0.06)
    
    return (
        f'  /*Bases - tweaks*/\n'
        f'  --bases-table-border-color: {border};\n'
        f'  --bases-table-header-background: {header_bg};\n'
        f'  --bases-table-row-background-hover: {hover_bg};\n'
    )

# === Define scheme blocks to modify ===
# Each: (scheme_name, light_or_dark, start_selector_line_content_hint, unique_end_text)
# We'll use a simpler approach: find the block by looking for the selector,
# then find its closing }, then insert before the closing }

schemes = {
    'avocado-light': {
        'selector_start': 'body.color-scheme-options-avocado-topaz.theme-light',
        'bg_fallback': '#ffffff',
        'is_dark': False,
    },
    'avocado-dark': {
        'selector_start': 'body.color-scheme-options-avocado-topaz.theme-dark',
        'bg_fallback': '#181818',
        'is_dark': True,
    },
    'monochrome-dark': {
        'selector_start': 'body.color-scheme-options-monochrome-topaz.theme-dark',
        'bg_fallback': '#1e1e1e',
        'is_dark': True,
    },
    'monochrome-light': {
        'selector_start': 'body.color-scheme-options-monochrome-topaz.theme-light',
        'bg_fallback': '#ffffff',
        'is_dark': False,
    },
    'pink-light': {
        'selector_start': 'body.color-scheme-options-pink-topaz.theme-light',
        'bg_fallback': '#ffffff',
        'is_dark': False,
    },
    'pink-dark': {
        'selector_start': 'body.color-scheme-options-pink-topaz.theme-dark',
        'bg_fallback': '#0f0f0f',
        'is_dark': True,
    },
    'nord-light': {
        'selector_start': 'body.color-scheme-options-topaz-nord.theme-light',
        'bg_fallback': '#ECEFF4',
        'is_dark': False,
    },
    'nord-dark': {
        'selector_start': 'body.color-scheme-options-topaz-nord.theme-dark',
        'bg_fallback': '#2E3440',
        'is_dark': True,
    },
}

changes = 0
for name, cfg in schemes.items():
    sel = cfg['selector_start']
    bg = cfg['bg_fallback']
    is_dark = cfg['is_dark']
    
    # Find the block: locate the selector line, then find the closing }
    idx = content.find(sel)
    if idx == -1:
        print(f'{name}: selector not found')
        continue
    
    # Find the opening brace
    brace_idx = content.find('{', idx)
    if brace_idx == -1:
        print(f'{name}: opening brace not found')
        continue
    
    # Find the closing brace by scanning
    depth = 0
    close_idx = brace_idx
    for i in range(brace_idx, len(content)):
        if content[i] == '{':
            depth += 1
        elif content[i] == '}':
            depth -= 1
            if depth == 0:
                close_idx = i
                break
    
    if close_idx == brace_idx:
        print(f'{name}: closing brace not found')
        continue
    
    # Extract the block and try to find --bg-color or --background-primary
    block = content[brace_idx:close_idx + 1]
    
    # Try to extract --bg-color from block
    bg_match = re.search(r'--bg-color\s*:\s*([^;]+);', block)
    if bg_match:
        bg_val = bg_match.group(1).strip()
        # Remove any var() fallbacks
        if not bg_val.startswith('#'):
            bg_val = bg
        else:
            bg = bg_val
    
    # Compute the insertions
    base_colors = compute_base_colors(bg, is_dark)
    bases_tweaks = compute_bases_tweaks(bg, is_dark)
    
    insertion = f'\n\n  /*Bases - color-base*/\n{base_colors}\n\n{bases_tweaks}'
    
    # Insert before the closing brace
    new_block = block[:-1] + insertion + '\n}'
    content = content[:brace_idx] + new_block + content[close_idx + 1:]
    
    changes += 1
    print(f'{name}: bg={bg} | inserted')

# Write back
with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print(f'\nTotal: {changes} blocks modified')