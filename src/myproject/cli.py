from __future__ import annotations

import argparse

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="my_project")
    parser.add_argument("--version", action="store_true", help="Print version and exit")

    sub = parser.add_subparsers(dest="command", required=False)

    hello = sub.add_parser("hello", help="Say hello")
    hello.add_argument("name", help="Name to greet")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        print(__version__)
        return 0

    if args.command == "hello":
        print(f"Hello, {args.name}!")
        return 0

    parser.print_help()
    return 0
