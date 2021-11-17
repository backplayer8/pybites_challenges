#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A script to automatically create both the bite and the test_bite files

import argparse
from pathlib import PosixPath as _path
from os import system as do

parser = argparse.ArgumentParser(
    description="""Provide the bite number
    to create the bite.py file and test_bite.py file"""
)

parser.add_argument(
    "-n",
    metavar="--bite-number",
    required=True,
    type=int,
    help="The number of the exercise as found on codechalleng.es",
)

args = parser.parse_args()


def make_files(num):
    starting_dir = _path(_path.cwd())

    # Creates the path object for the pytest file then creates the file
    test_file = starting_dir.joinpath("tests", f"test_bite_{num}")
    with open(test_file, "w+") as wt:
        wt.write(
            f" # Test for Bite {num}: \n\nfrom pybites_challenges.bite_{num} import"
        )
    # Creates the path object then makes the directory and bite_num.py file
    bite_path = starting_dir.joinpath("pybites_challenges", str(num))
    bite_path.mkdir()
    bite_file = bite_path.joinpath(f"bite_{num}.py")

    with open(bite_file, "w+") as w:
        w.write(f" # Bite {num}: <name of the challenge>")


def main():
    make_files(args.n)


if __name__ == "__main__":
    main()
