import re

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'r', encoding='utf-8') as f:
    content = f.read()

def lerp_color(c1, c2, t):
    r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
    r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return f'#{r:02x}{g:02x}{b:02x}'

def compute_base(bg_hex, is_dark):
    end = '#dadada' if is_dark else '#202020'
    names = ['00', '05', '10', '20', '25', '30', '35', '40', '50', '60', '70', '100']
    steps = [0.0, 0.02, 0.05, 0.10, 0.15, 0.20, 0.28, 0.40, 0.55, 0.72, 0.85, 1.0]
    lines = []
    for name, t in zip(names, steps):
        lines.append(f'  --color-base-{name}: {lerp_color(bg_hex, end, t)};')
    return '\n'.join(lines)

def compute_tweaks(is_dark):
    return (
        '  /*Bases - tweaks*/\n'
        '  --bases-table-stripe-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.08);\n'
        '  --bases-table-header-background: var(--background-secondary-alt);\n'
        '  --bases-table-group-background: transparent;\n'
        '  --bases-table-row-background-hover: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.18);\n'
        '  --bases-table-header-color: var(--deep-color);\n'
        '  --table-border-color: hsla(var(--accent-h), var(--accent-s), var(--accent-l), 0.22);'
    )

schemes = {
    'flamingo-light':    {'sel': 'body.color-scheme-options-flamingo.theme-light',    'bg': '#faf4eb', 'dark': False},
    'flamingo-dark':     {'sel': 'body.color-scheme-options-flamingo.theme-dark',     'bg': '#212121', 'dark': True},
    'honey-light':       {'sel': 'body.color-scheme-options-honey-milk-topaz.theme-light',  'bg': '#fafaf3', 'dark': False},
    'honey-dark':        {'sel': 'body.color-scheme-options-honey-milk-topaz.theme-dark',   'bg': '#1e1e1e', 'dark': True},
    'choco-light':       {'sel': 'body.color-scheme-options-chocolate-topaz.theme-light',   'bg': '#faf4eb', 'dark': False},
    'choco-dark':        {'sel': 'body.color-scheme-options-chocolate-topaz.theme-dark',    'bg': '#0f0f0f', 'dark': True},
    'lilac-light':       {'sel': 'body.color-scheme-options-lilac.theme-light',      'bg': '#fdf7fb', 'dark': False},
    'lilac-dark':        {'sel': 'body.color-scheme-options-lilac.theme-dark',       'bg': '#1b1b1b', 'dark': True},
    'lillimon-light':    {'sel': 'body.color-scheme-options-lillimon-topaz.theme-light',    'bg': '#f8f8f5', 'dark': False},
    'lillimon-dark':     {'sel': 'body.color-scheme-options-lillimon-topaz.theme-dark',     'bg': '#1e1e1e', 'dark': True},
    'simplicity-light':  {'sel': 'body.color-scheme-options-simplicity-topaz.theme-light',  'bg': '#fafaf3', 'dark': False},
    'simplicity-dark':   {'sel': 'body.color-scheme-options-simplicity-topaz.theme-dark',   'bg': '#1b1b1b', 'dark': True},
}

changes = 0
for name, cfg in schemes.items():
    sel = cfg['sel']
    idx = content.find(sel)
    if idx == -1:
        print(f'{name}: NOT FOUND')
        continue
    brace = content.find('{', idx)
    if brace == -1:
        print(f'{name}: no brace')
        continue
    depth = 0
    close = brace
    for i in range(brace, len(content)):
        if content[i] == '{': depth += 1
        elif content[i] == '}':
            depth -= 1
            if depth == 0:
                close = i
                break
    block = content[brace:close+1]
    bg_match = re.search(r'--bg-color\s*:\s*([^;]+);', block)
    bg = cfg['bg']
    if bg_match:
        v = bg_match.group(1).strip()
        if v.startswith('#'):
            bg = v
    
    base = compute_base(bg, cfg['dark'])
    tweaks = compute_tweaks(cfg['dark'])
    insert = f'\n\n  /*Bases - color-base*/\n{base}\n\n{tweaks}'
    new_block = block[:-1] + insert + '\n}'
    content = content[:brace] + new_block + content[close+1:]
    changes += 1
    print(f'{name}: bg={bg}')

with open(r'E:\WORK\Obsidian-Blue-Topaz-Alternate\theme.css', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
print(f'\nTotal: {changes} blocks modified')