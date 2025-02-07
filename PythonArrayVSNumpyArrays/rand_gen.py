# Isla Kim

import random

array1 = [1.0] * 10  

for i in range(len(array1)):
    array1[i] = random.uniform(-10, 10)

print("\nRandomly generated array with 10 floating numbers in range -10 to 10: \n", array1, "\n")
