import matplotlib.pyplot as plt

graus = [1, 3, 1, 5, 8, 4, 1, 3, 6, 3, 6, 5, 6, 6, 3, 3, 5, 5, 3, 2, 1, 3, 2, 2, 4, 2, 6]

plt.hist(graus, 5, rwidth=0.9)
plt.show()