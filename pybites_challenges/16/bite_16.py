#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bite 16:

from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    """Infinitely yields datetime objects
    for every 100 days since PyBites was founded"""

    first_hundred = PYBITES_BORN + timedelta(days=100)
    while True:
        yield first_hundred
        first_hundred = first_hundred + timedelta(days=100)
