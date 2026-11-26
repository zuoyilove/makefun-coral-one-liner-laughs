#!/usr/bin/env python3
"""One-Liner Laughs entry: writes a single original joke line to /output/entry.txt."""

import os

JOKE = "My therapist says I use jokes to avoid my feelings, so I told her my childhood was a subscription: the free trial was great, but there's no cancel button and the renewal fee is my personality."


def main():
    print(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
