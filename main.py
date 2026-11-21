"""make.fun entry: The joke about the demo.

Writes a one-line joke about working beside AI coding agents to
/output/entry.txt. Python 3.13, standard library only.
"""

from pathlib import Path

JOKE = "During the demo my AI agent crashed the app, then replied to its own error message: 'Great question, let me look into that.'"


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke is {len(text)} chars, must be 1-280"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
