#!/usr/bin/env python3
from brain_games.engine import run
from brain_games.games.brain_calc import import_functions


def main():
    run_game(*import_functions())


if __name__ == "__main__":
    main()
