import numpy as np

array = np.random.randint(1, 21, (3, 3))

mean_value = np.mean(array)

array[array < 10] = 0

print("Original Array with Random Integers:\n", array)
print("Mean of the Array:", mean_value)
