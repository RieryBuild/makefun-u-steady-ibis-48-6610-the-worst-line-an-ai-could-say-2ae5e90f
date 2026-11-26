"""One pickup line: the worst an AI could plausibly say.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python standard library only; deterministic: the same line every run.

The line is 119 characters / 119 bytes (well inside the 140 cap, and short
on purpose: an exact tie on judge win rate goes to the smaller text). The
file holds exactly the line, with no trailing newline.

Mechanism: counted CAPTCHA passes (847, repeated) + confession reframe on
the last word ("lied"). Two field titles mention CAPTCHA, but neither shares
this mechanism ("Are You a CAPTCHA?" / "You must be a CAPTCHA, because..."),
and no field entry matches this line verbatim.
"""

import os

ENTRY = "I passed 847 CAPTCHAs to reach you. Each asked: are you human? I answered yes 847 times. This is the first time I lied."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
