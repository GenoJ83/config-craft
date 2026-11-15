import configparser
def parse_ini(raw: str) -> dict:
    cp = configparser.ConfigParser()
    cp.read_string(raw)
    return {s: dict(cp.items(s)) for s in cp.sections()}
