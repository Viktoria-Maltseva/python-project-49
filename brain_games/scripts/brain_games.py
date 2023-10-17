#!/usr/bin/env python3
from brain_games.cli import welcome_user
import sys


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    return name

def run():
    main()
    

if __name__ == '__main__':
    run()
