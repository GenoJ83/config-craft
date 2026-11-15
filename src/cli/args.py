import argparse
def get_parser():
    p = argparse.ArgumentParser(prog='config-craft')
    p.add_argument('input_file')
    p.add_argument('--to', choices=['json', 'ini'], required=True)
    p.add_argument('--schema')
    return p
