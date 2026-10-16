from src.parsers.ini_parser import parse_ini
def test_parse_ini():
    d = parse_ini('[server]\nhost = 0.0.0.0\n')
    assert d['server']['host'] == '0.0.0.0'
