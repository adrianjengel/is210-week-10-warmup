#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK10 warmup task 04 - Working with directories."""

import data

data.BANDS['Buckingham Nicks'] = {
    'Lindsey Buckingham': ['guitar', 'vocals'],
    'Stevie Nicks': ['vocals', 'tambourine']
}

data.BANDS['Fleetwood Mac'].update(data.BANDS['Buckingham Nicks'])
