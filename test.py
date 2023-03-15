# The embedded software that controls a military satellite suffers from software aging. This satellite’s availability must be no less than six nines (99.9999 %), which means a yearly downtime no longer than 31.56 seconds. Because of the accumulation of the aging effects, the size of the satellite’s main application process grows progressively. The memory size of this process has been monitored monthly, for one year, and the result follows ( in megabyte): 50, 293, 763, 1097, 1355, 1567, 1745, 1900, 2037, 2159, 2269, 2370. It is known that once this process grows beyond 2.8 gigabytes, it will be abruptly forced to terminate by the satellite operating system. Taking into consideration the above-described scenario, answer the following questions:

# To create the python code


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# To create the data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y = np.array([50, 293, 763, 1097, 1355, 1567,
             1745, 1900, 2037, 2159, 2269, 2370])

# To create the function


def func(x, a, b, c):
    return a * np.exp(b * x) + c


# To create the curve fit
popt, pcov = curve_fit(func, x, y)

# To create the plot
plt.plot(x, y, 'ko', label="Original Noised Data")
plt.plot(x, func(x, *popt), 'r-', label="Fitted Curve")
plt.legend()
plt.show()

# To print the result
print(popt)

# To print the result
print(pcov)

# To print the result
print(func(13, *popt))

# To print the result
print(func(13, *popt) - 2800)

# To print the result

print(func(13, *popt) - 2800 > 0)


# To print the result
print(func(13, *popt) - 2800 < 0)

# To print the result
print(func(13, *popt) - 2800 == 0)

# To print the result
print(func(13, *popt) - 2800 != 0)

# To print the result
