

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

# PART !

# EXERCISE 1.1

px = pd.read_csv('priceData.csv')

# Perform the natural logarithm transform of the data
import pdb; pdb.set_trace()
logpx = np.log(px['SPX Index'])

# Sliding mean
plt.figure()
plt.plot(logpx.rolling(252).mean())
plt.show()


