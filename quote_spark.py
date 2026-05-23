#!/usr/bin/env python3
"""quote_spark – a tiny random‑quote CLI.

The script contains an inline list of quotes to keep the project self‑contained.
It can be executed as a module (`python -m quote_spark`) or as a script.
"""

import random
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Quote data – kept deliberately short to stay tiny.
# ---------------------------------------------------------------------------
_QUOTES = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "Do one thing every day that scares you. – Eleanor Roosevelt",
]


def get_random_quote() -> str:
    """Return a random quote from the internal list."""
    return random.choice(_QUOTES)


def main(argv: list[str] | None = None) -> int:
    """Entry point for the CLI.

    Parameters
    ----------
    argv: list[str] | None
        Argument vector supplied by the caller – defaults to ``sys.argv``.

    Returns
    -------
    int
        Exit status (always ``0``).
    """
    if argv is None:
        argv = sys.argv[1:]
    # Currently we ignore arguments – future extensions could add filters.
    _ = argv  # silence unused‑variable lint warnings.
    print(get_random_quote())
    return 0


if __name__ == "__main__":
    sys.exit(main())
