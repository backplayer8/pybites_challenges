#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A script to automatically create both the bite and the test_bite files

import argparse
from pathlib import PosixPath as _path
from os import system as do


def make_files(num: int) -> None:
    starting_dir = _path(_path.cwd())

    # Creates a path object for the bite_num directory
    bite_path = starting_dir.joinpath("pybites_challenges", str(num))
    if bite_path.is_dir() is False:
        bite_path.mkdir()

    bite_file = bite_path.joinpath(f"bite_{num}.py")
    with open(bite_file, "w+") as w:
        w.write(f" # Bite {num}: <name of the challenge>")

    test_file = bite_path.joinpath(f"test_bite_{num}")
    with open(test_file, "w+") as wt:
        wt.write(f" # Test for Bite {num}: \n\nfrom bite_{num} import *")


def main():
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

    make_files(args.n)


if __name__ == "__main__":
    main()
