#!/usr/bin/env python3
from brain_games.engine import run


def main():
    module = __import__('brain_games.scripts.games.brain_progression',
            fromlist=['brain_progression'])
    run(module)


if __name__ == "__main__":
    main()
