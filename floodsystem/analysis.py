import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def polyfit(dates, levels, p):
    """returns a tuple of a numpy.poly1d object and a shift of the date axis"""

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    return(poly, d0)


#d0 ???????