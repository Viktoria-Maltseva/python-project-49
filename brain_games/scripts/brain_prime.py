#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.brain_prime import import_functions


def main():
    run_game(*import_functions())


if __name__ == "__main__":
    main()
