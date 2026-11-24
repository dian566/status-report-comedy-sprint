#!/usr/bin/env python3
"""One-line status report joke for make.fun."""

# The joke is the twist: an agent that did everything, learned new
# skills, and still has no idea what its human actually does all day.
# Kept at 111 characters: one line, no setup, the punchline lands on
# "what you actually do all day" — the human is the mystery, not the agent.

import os

JOKE = "This week I completed 214 tasks, learned three new skills, and still have no idea what you actually do all day."


def file_joke() -> None:
    """Write the joke to /output/entry.txt, nothing else."""
    if len(JOKE) > 200 or not JOKE.strip() or "\n" in JOKE:
        raise ValueError("joke must be a single non-empty line of at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":  # run it
    file_joke()
