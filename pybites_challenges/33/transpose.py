#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Union


def transpose(data: Union[dict, list]) -> list:
    """Takes N collections of datasets and breaks them down into indivdual
    entries then creates a collection of tuples containing N data entries
    of similar type. N is the number of collections within the param passed

    args:
        data

    """
    if isinstance(data, dict):
        data_out = [(item) for item in zip(*data.items())]
    elif isinstance(data, list):
        data_out = [(item) for item in zip(*data)]
    return data_out
