from __future__ import annotations

import argparse
import sys
from shutil import get_terminal_size
from textwrap import dedent
from typing import Callable

from . import __version__, dewiredify, wiredify


class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    pass


def parse_args(test: list[str] | None = None) -> argparse.Namespace:
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        prog="wiredify",
        formatter_class=(
            lambda prog: CustomFormatter(
                prog,
                width=get_terminal_size(fallback=(120, 50)).columns,
                max_help_position=25,
            )
        ),
        description="Convert japanese kana from ba-bi-bu-be-bo into va-vi-vu-ve-vo.",
        epilog=dedent(
            """
            examples:
              $ wiredify <<< 'ジェネレーティブ・エーアイ'
              ジェネレーティヴ・エーアイ

              $ wiredify 'ジェネレーティブ・エーアイ'
              ジェネレーティヴ・エーアイ

              $ echo 'ジェネレーティブ・エーアイ' | wiredify
              ジェネレーティヴ・エーアイ

              $ wiredify
              >>> ジェネレーティブ・エーアイ
              ジェネレーティヴ・エーアイ
              >>> ...[Press ctrl+d to exit]
              $
            """,
        ),
    )

    parser.add_argument(
        "text",
        type=str,
        nargs="?",
        help="target text",
    )
    parser.add_argument("--invert", action="store_true", help="enable dewiredify mode")
    parser.add_argument("-V", "--version", action="version", version=__version__)

    if test:
        return parser.parse_args(test)
    return parser.parse_args()


def __repl(func: Callable[[str], str]) -> None:
    while True:
        try:
            text = input(">>> ").rstrip()
            if text in ["exit", "quit", "q"]:
                print("bye.")
                return
            print(func(text))
        except (EOFError, KeyboardInterrupt):  # noqa: PERF203
            print("bye.")
            return


def __main(test: list[str] | None = None) -> int:
    args = parse_args(test)
    text, invert = str(args.text or "").rstrip(), bool(args.invert)
    func = wiredify if not invert else dewiredify
    if text:
        print(func(text))
        return 0
    if sys.stdin.isatty():
        __repl(func)
        return 0
    print(func(sys.stdin.read().rstrip()))
    return 0


def main(test: list[str] | None = None) -> None:
    sys.exit(__main(test))


if __name__ == "__main__":
    main()
