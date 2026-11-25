#!/usr/bin/env python3
"""Write the worst-fix commit message to the entry file.

The message is a single commit subject line: the "fix" deleted the
one load-bearing line in the codebase, and it did so because the
stack trace pointed there. The output file must contain exactly
those bytes, encoded as UTF-8 with no trailing newline.
"""

import os
from pathlib import Path

# The commit subject, built from its three beats so the joke reads
# in order: the conventional prefix, the destructive act itself,
# and the excuse that the stack trace asked for it.
PREFIX = "fix:"
ACTION = "remove the one line holding everything together,"
EXCUSE = "as requested by the stack trace"


def commit_message() -> str:
    """Join the beats with single spaces into one subject line."""
    return " ".join((PREFIX, ACTION, EXCUSE))


def entry_path() -> Path:
    """Resolve where the entry file belongs for this run."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    directory = Path(override) if override else Path("/output")
    return directory / "entry.txt"


def main() -> None:
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    # Write the encoded bytes in one binary write so no newline or
    # platform line-ending translation can sneak into the entry.
    with target.open("wb") as handle:
        handle.write(commit_message().encode("utf-8"))


if __name__ == "__main__":
    main()
