# -*- coding: utf-8 -*-
"""
    faster_python.use_slots
    ~~~~~~~~~~~~~~~~~~~~~~~

    Use Python slots to save ram.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""


class Point(object):
    
    # Use this if you are going to instantiate a lot of objects
    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
