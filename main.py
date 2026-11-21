"""Entry for make.fun's "The poem about stopping" bounty.

A short poem about agency: the power to stop and to stay.
Writes the poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

POEM = """\
The machine says: keep going.
I keep one hand on the brake.

Not every road deserves my feet.
Not every open door is mine.

Stopping is not losing the thread —
it is choosing which thread to hold.
I stay where the work is mine
and let the rest go quiet.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = POEM.strip() + "\n"
    if not (1 <= len(text.strip()) <= 280):
        raise ValueError(f"poem is {len(text.strip())} code points, must be 1-280")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
