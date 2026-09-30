def diff_configs(c1: dict, c2: dict):
    k1, k2 = set(c1.keys()), set(c2.keys())
    return {'added': list(k2 - k1), 'removed': list(k1 - k2), 'common': list(k1 & k2)}
