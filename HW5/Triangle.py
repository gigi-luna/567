"""methods that check functions"""

import math


def classify_triangle(sidea, sideb, sidec):
    """checks triangle type."""

    if not(isinstance(sidea, int) and isinstance(sideb, int) and isinstance(sidec, int)):
        return 'InvalidInput'

    if (sidea >= (sideb + sidec)) or \
            (sideb >= (sidea + sidec)) or (sidec >= (sidea + sideb)):
        return 'NotATriangle'

    maxi = max(sidea, sideb,  sidec)
    if maxi == sidea:
        total = pow(sidec, 2) + pow(sideb, 2)
    if maxi == sideb:
        total = pow(sidea, 2) + pow(sidec, 2)
    if maxi == sidec:
        total = pow(sidea, 2) + pow(sideb, 2)

    if math.sqrt(total) == maxi:
        return "Right"

    if sidea == sidec or sidea == sideb or sidec == sideb:
        if sidea == sideb and sidea == sidec:
            return "Equilateral"
        return "Isosceles"
    return "Scalene"
