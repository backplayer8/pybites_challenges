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
    bite_path = _path.joinpath(starting_dir, "pybites_challenges")
    test_path = _path.joinpath(starting_dir, "tests")
    bite_file = f"{bite_path}/bite_{num}.py"
    test_file = f"{test_path}/test_bite_{num}.py"
    # do(f"touch {bite_file}")
    with open(bite_file, "w+") as w:
        w.write(f" # Bite {num}: <name of the challenge>")
    with open(test_file, "w+") as wt:
        wt.write(
            f" # Test for Bite {num}: \n\nfrom pybites_challenges.bite_{num} import"
        )


def main():
    make_files(args.n)


if __name__ == "__main__":
    main()
