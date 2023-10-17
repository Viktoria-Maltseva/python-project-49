#!/usr/bin/env python3
from brain_games.cli import welcome_user

name = ''
def main():
    print("Welcome to the Brain Games!")
    name_to_remember = welcome_user()
    return name_to_remember


if __name__ == '__main__':
    name = main()
