from src.cli.args import get_parser
def test_cli():
    p = get_parser()
    args = p.parse_args(['config.json', '--to', 'ini'])
    assert args.to == 'ini'
