"""
Given two speeds v1 (A's speed, integer > 0) and v2 (B's speed, integer > 0) and
a lead g (integer > 0) how long will it take B to catch A?

The result will be an array [hour, min, sec] which is the time needed in hours, 
minutes and seconds (round down to the nearest second)

v1 and v2 are assumed to be feet per hour, and g is assumed in feet.

returns : [hh, mm, ss] or None
"""


def race(v1, v2, g):
    time = g * 3600 // (v2 - v1)
    return None if v1 >= v2 else [time // 3600, time % 3600 // 60, time % 60]
