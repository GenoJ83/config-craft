from src.parsers.json_parser import parse_json
def test_parse_json():
    d = parse_json('{"name": "app", "port": 8080}')
    assert d['port'] == 8080
