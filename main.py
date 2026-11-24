"""One-star review of an everyday essential: gravity.

Writes a single deadpan one-star review, at most 160 characters on one
line, to entry.txt. The review complains about gravity in earnest: it is
free and always on, yet somehow only ever noticed at the exact moment it
breaks something that was just paid for.
"""

import os
import sys

REVIEW = (
    "Gravity: free, always on, and somehow only ever noticed "
    "when it is breaking something I just paid for."
)


def validate(text):
    """Check the entry against the competition gate.

    The gate requires UTF-8 text of 1 to 160 characters, a single line,
    and more than whitespace alone. Raises ValueError on any failure.
    """
    if not isinstance(text, str):
        raise ValueError("review must be text")
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    if not 1 <= len(text) <= 160:
        raise ValueError("review must be 1 to 160 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if not text.strip():
        raise ValueError("review must not be only whitespace")
    if text != text.strip():
        raise ValueError("review must not start or end with whitespace")
    return True


def main():
    validate(REVIEW)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(REVIEW)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != REVIEW:
        raise ValueError("read-back mismatch: entry.txt differs from REVIEW")
    print("wrote %s (%d characters)" % (path, len(REVIEW)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
