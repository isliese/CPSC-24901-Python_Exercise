# Isla Kim

import random
import json
import csv

# Initialize the two-dimensional array with floating-point numbers
linear_data_array = [] 

# Generate random numbers as x values, calculate y values, and save them in the array
for i in range(1000000):  
    x = round(random.uniform(-1000, 1000), 3)
    y = (x * 0.5) + 2
    linear_data_array.append([y, x])  

# Display the first, middle, and last pairs
print("The first pair:", linear_data_array[0])
print("The middle pair:", linear_data_array[len(linear_data_array)//2])
print("The last pair:", linear_data_array[-1])

# Saves the data in the array into L1.json
with open('L1.json', 'w') as jsonfile:
    json.dump({"linear": linear_data_array}, jsonfile)  # Store data with "linear" key
print("L1.json well generated!")

# Saves the data in the array into L1.csv
with open('L1.csv', 'w', newline='') as csvfile:
    write = csv.writer(csvfile)
    write.writerows(linear_data_array)  # Write the rows of data to the CSV
print("L1.csv well generated!")

# Initialize the two-dimensional array with floating-point numbers
polynomial_data_array1 = []
polynomial_data_array2 = []

# Generate random numbers as x values, calculate x1, x2, y values, and save them in the array
for i in range(1000000):  
    x = round(random.uniform(-1000, 1000), 3)
    x1 = 0.5*x
    x2 = -3*x**2
    y = (-3 * x**2) + (x * 0.5) + 2
    polynomial_data_array1.append([y, x]) 
    polynomial_data_array2.append([y, x1, x2])  

# Saves the data in the array into Q1.csv with two columns 𝑦 and 𝑥
with open('Q1.csv', 'w', newline='') as csvfile2:
    write = csv.writer(csvfile2)
    write.writerows(polynomial_data_array1)
print("Q1.csv well generated!")

# Saves the data in the array into Q2.csv with two columns (𝑦, 𝑥1, 𝑥2)
with open('Q2.csv', 'w', newline='') as csvfile3:
    write = csv.writer(csvfile3)
    write.writerows(polynomial_data_array2)
print("Q2.csv well generated!")

