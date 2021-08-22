"""
Calculates how many years it will take for a city to grow
in size given:

    p0      = initial population
    percent = annual growth rate
    aug     = growth from people moving in
    p       = target population size

"""

def nb_year(p0, percent, aug, p, years = 0):
    return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1) if p0 < p else years
