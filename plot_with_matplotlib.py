import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np


# rcParams.update({'font.size': 18, 'font.family': 'serif'})
# Font style
# global setting
plt.rcParams["font.family"] = "Times New Roman"
x = np.linspace(0, 5, 100)
y = x ** 2

fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r"$y = \alpha^2$")
    ax.set_title('title')

fig.tight_layout()


plt.show()

# plt.savefig('test.pdf', dpi=1200)
print("image saved")