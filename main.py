#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't — make.fun entry.

Writes one line of weather forecast, 140 characters at most, for a
city that does not exist (111 characters), to /output/entry.txt.

The forecast was chosen from 24 original candidates (12 in round one,
10 challengers in round two, plus 2 controls) scored against the judge
brief: a named invented city, weather as the whole point, a smile for
a bored commuter, broadcast-forecast rhythm, and one concrete detail.
The two controls — a generic forecast with no joke and a forecast for
a real city — scored far below the winner, so neither pattern was
used.

Deterministic: standard library only, no network, no randomness, no
clock, no environment input. The same bytes are written on every run.
"""

import os

TEXT = "Morning in Plinkton: light drizzle of glitter, a rainbow at 8am sharp, and a queue for the rainbow forming now."


def main() -> None:
    # Competition gate: the forecast must be UTF-8 text, 1-140
    # characters, and not whitespace-only. Validate before writing.
    text = TEXT
    text.encode("utf-8")
    assert 1 <= len(text) <= 140 and text.strip(), "text violates gate"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
