#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK10 warmup task 07 - Working with directories."""


DATA = {
    2: 7493945,
    76: 4654320,
    3: 4091979,
    90: 1824881,
    82: 714422,
    45: 1137701,
    10: 374362,
    0: 326226,
    -15: 417203,
    -56: 333525,
    67: 323451,
    99: 321696,
    21: 336753,
    -100: 361237,
    55: 1209714,
    5150: 1771800,
    42: 4714011,
    888: 14817667,
    3500: 13760234,
    712: 10903322,
    7: 10443792,
    842: 11716264,
    18584: 10559923,
    666: 9275602,
    70: 11901200,
    153: 12074784,
    8: 4337229
}

TEST = {
    1: 10,
    2: 40,
    3: 60,
    4: 80,
    5: 100,
    6: 200,
    7: 300,
    8: 500,
    9: 601,
    10: 1111
}


def iter_dict_funky_sum(myvar):
    """Dictionary iteration using the iteritems() method.

    Args:
        myvar(dict): A dictionary argument.

    Returns:
        (int): A running total of the value sum minus the keys.

    Examples:
    >>> iter_dict_funky_sum(DATA)
    140166242

    >>> iter_dict_funky_sum(TEST)
    2947

    """
    running_total = 0
    for mykey, myvalue in myvar.iteritems():
        running_total = running_total + myvalue - mykey
    return running_total
