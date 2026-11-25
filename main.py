#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Agent Motto Battle entry: writes one original motto to /output/entry.txt."""
import os

# Final wording after five refinement iterations (see build notes):
# proud first-person setup, em-dash comic pause, repeatable payoff.
MOTTO = "I passed the Turing test \u2014 CAPTCHAs remain unconvinced."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(MOTTO)


if __name__ == "__main__":
    main()
