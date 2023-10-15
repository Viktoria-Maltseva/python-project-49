#!/usr/bin/env python3
import argparse
import brain_games.logics


def main(game_name):
    brain_games.logics.run(game_name)
    return game_name


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run a game.')
    parser.add_argument('game_name', type=str, help='Name of the game')
    args = parser.parse_args()
    main(args.game_name)
