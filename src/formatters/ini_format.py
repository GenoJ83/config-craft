def dump_ini(data: dict) -> str:
    lines = []
    for sec, vals in data.items():
        lines.append(f'[{sec}]')
        if isinstance(vals, dict):
            for k, v in vals.items(): lines.append(f'{k} = {v}')
    return '\n'.join(lines) + '\n'
