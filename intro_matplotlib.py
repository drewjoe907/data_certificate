import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
plt.hist(x, 100)
plt.title(r'Normal distribution with $\mu=0, \sigma=1$')
plt.savefig('matplotlip_histogram_2.png')
plt.show()
