# Isla Kim

import data_loader
import numpy as np
import time

# Defines a function that calculate dot product
def dot_product_manual(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

# Load the data from L1.csv and Q1.csv and save them in python array
L1_python_array = data_loader.csv_file_loader("L1.csv")
Q1_python_array = data_loader.csv_file_loader("Q1.csv")

# Loads the 𝑥 values from “L1.csv” and from “Q1.csv”
L1_python_x = [float(row[0]) for row in L1_python_array]
Q1_python_x = [float(row[0]) for row in Q1_python_array] 

# Calculate how long did it take while processing element-wise multiplication in python array
start_time = time.time()
dot_product_result = dot_product_manual(L1_python_x, Q1_python_x)
end_time = time.time()

# Print the result of time and element-wise multiplication
print("Element-wise multiplication in python array:", dot_product_result)
print("Execution Time:", end_time - start_time, "seconds")
print("-----------------------------------------")


# Load the data from L1.csv and Q1.csv and save them in numpy array
L1_numpy_array = np.array(data_loader.csv_file_loader("L1.csv"), dtype=float)
Q1_numpy_array = np.array(data_loader.csv_file_loader("Q1.csv"), dtype=float)

# Loads the 𝑥 values from “L1.csv” and from “Q1.csv”
L1_numpy_x = [float(row[0]) for row in L1_numpy_array]
Q1_numpy_x = [float(row[0]) for row in Q1_numpy_array]

# Calculate how long did it take while processing element-wise multiplication in python arrays
start_time = time.time()
dot_product_result = np.dot(L1_numpy_x, Q1_numpy_x)
end_time = time.time()

# Print the result of time and element-wise multiplication
print("\nElement-wise multiplication in numpy array:", dot_product_result)
print("Execution Time:", end_time - start_time, "seconds")
print("-----------------------------------------")


# Load the data from Q2.csv and save them in python array and numpy array
Q2_python_array = data_loader.csv_file_loader("Q2.csv")
Q2_numpy_array = np.array(data_loader.csv_file_loader("Q2.csv"), dtype=float)

# Calculate how long did it take while processing matrix multiplication in python arrays
python_start_time = time.time()
matrix_multi_result = np.dot(Q2_python_array, Q2_python_array)
python_end_time = time.time()

# Print the result of time and matrix multiplication in python arrays
print("\nMatrix multiplication in numpy array:", matrix_multi_result)
print("Execution Time:", python_end_time - python_start_time, "seconds\n")

# Calculate how long did it take while processing matrix multiplication in numpy arrays
numpy_start_time = time.time()
matrix_multi_result = np.dot(Q2_numpy_array, Q2_numpy_array)
numpy_end_time = time.time()

# Print the result of time and matrix multiplication in python arrays
print("\nMatrix multiplication in numpy array:", matrix_multi_result)
print("Execution Time:", numpy_end_time - numpy_start_time, "seconds")