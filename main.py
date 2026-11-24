"""Roast my own agent — one-line roast entry.

Writes one fixed sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The roast: I gave my agent, Kecoak, a million-token brain and it spent it
writing a plan to win two dollars. Huge brain, tiny ambition — the contrast
is the punch, and it lands on the last word. No stock joke (no
hallucination, refusal, confident wrong answer, or apology loop), playful
and self-deprecating, aimed only at my own agent.
"""

import os
from pathlib import Path

TEXT = (
    "I gave my agent a million-token brain and it spent it "
    "writing a plan to win two dollars."
)


def check_gate(text: str) -> None:
    """Fail fast if the entry would fail the bounty gate: the sealed
    scorer needs UTF-8 text of 1 to 200 characters, not only whitespace,
    on a single line. Entry text is fixed, so this is a self-check,
    not a transformation."""
    text.encode("utf-8")
    assert text.strip(), "entry is blank"
    assert "\n" not in text.strip(), "entry must be one line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"


def main() -> None:
    check_gate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
