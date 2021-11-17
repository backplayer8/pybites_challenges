#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bite 15: Enumerate 2 Sequences

names = "Julian Bob PyBites Dante Martin Rodolfo".split()
countries = "Australia Spain Global Argentina USA Mexico".split()


def enumerate_names_countries():
    """Outputs:
    1. Julian     Australia
    2. Bob        Spain
    3. PyBites    Global
    4. Dante      Argentina
    5. Martin     USA
    6. Rodolfo    Mexico"""
    for name in enumerate(zip(names, countries)):
        space_needed = -len(name[1][0]) + 11
        print(f"{name[0] + 1}. {name[1][0]}" + " " * space_needed + name[1][1])
