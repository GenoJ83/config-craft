from src.engine.diff import diff_configs
def test_diff():
    d = diff_configs({'a': 1, 'b': 2}, {'b': 2, 'c': 3})
    assert 'c' in d['added']
    assert 'a' in d['removed']
