"""The Dog Ate My Homework: Funniest Excuse — one line (81 characters).

Writes the excuse to /output/entry.txt.
"""

import os

LINE = "My dog didn't eat my homework. He graded it. He gave it a D and ate the evidence."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
