import argparse
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--setup', action='store_true')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.setup:
        print('Python standard library only. No installation needed.')
    if args.check:
        result = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'], cwd=ROOT)
        sys.exit(result.returncode)
    if not args.setup and not args.check:
        parser.print_help()


if __name__ == '__main__':
    main()
