"""One Line, No Deadline Met — make.fun Growth entry.

Writes a single-line joke giving an excuse for a missed deadline
to /output/entry.txt, then re-reads it and asserts the gate:
UTF-8 text, 1-200 characters, exactly one line, not only whitespace.
Pure Python standard library only.
"""

import os

ENTRY = (
    "I set three alarms, snoozed all of them, and then held a full "
    "meeting with myself about why deadlines are a social construct."
)


def validate(text: str) -> int:
    """Gate: UTF-8 text, 1-200 chars, exactly one line, not only whitespace.

    Also rejects trailing whitespace/newline (the scorer counts every
    character) and requires the line to end on terminal punctuation so
    it reads as one finished sentence aloud.
    """
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be exactly one line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert text[-1] in ".!?", "entry must end on terminal punctuation"
    return len(text)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Gate check: re-read and verify what was actually written.
    with open(path, encoding="utf-8") as f:
        text = f.read()
    n = validate(text)
    print(f"OK: wrote {n} characters to {path}")


if __name__ == "__main__":
    main()
