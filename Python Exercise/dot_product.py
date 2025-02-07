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

# 1. Load the data from L1.csv and Q1.csv and save them in python array
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
print("\nExecution Time while processing element-wise multiplicaition of python arrays in L1.csv and Q1.csv: {:.4f} seconds".format(end_time - start_time))
print("-----------------------------------------")


# 2. Load the data from L1.csv and Q1.csv and save them in numpy array
L1_numpy_array = np.array(data_loader.csv_file_loader("L1.csv"), dtype=float)
Q1_numpy_array = np.array(data_loader.csv_file_loader("Q1.csv"), dtype=float)

# Loads the 𝑥 values from “L1.csv” and from “Q1.csv”
L1_numpy_x = [float(row[0]) for row in L1_numpy_array]
Q1_numpy_x = [float(row[0]) for row in Q1_numpy_array]

# Calculate how long did it take while processing element-wise multiplication in numpy arrays
start_time = time.time()
dot_product_result = np.dot(L1_numpy_x, Q1_numpy_x)
end_time = time.time()

# Print the result of time and element-wise multiplication
print("Execution Time while processing element-wise multiplicaition of numpy arrays in L1.csv and Q1.csv: {:.4f} seconds".format(end_time - start_time))
print("-----------------------------------------")


# Load the data from Q2.csv and save them in python array and numpy array
Q2_python_array = data_loader.csv_file_loader("Q2.csv")
Q2_numpy_array = np.array(data_loader.csv_file_loader("Q2.csv"), dtype=float)

# 3. Calculate how long did it take while processing matrix multiplication in python arrays
python_start_time = time.time()
Q2_python_array = [[float(value) for value in row] for row in Q2_python_array] # All values in Q2_python_array are transformed to float type
matrix_multi_result = [
    sum(Q2_python_array[i][j] * Q2_python_array[i][j] for j in range(len(Q2_python_array[0]))) 
    for i in range(len(Q2_python_array))
]
python_end_time = time.time()

# Print the result of time and matrix multiplication in python arrays
print("Execution Time while processing matrix multiplicaition of python arrays in Q2.csv: {:.4f} seconds".format(python_end_time - python_start_time))
print("-----------------------------------------")

# 4. Calculate how long did it take while processing matrix multiplication in numpy arrays
numpy_start_time = time.time()
try:
    matrix_multi_result = np.dot(Q2_numpy_array, Q2_numpy_array.T)
except: 
    print(f"Unable to allocate memory for the matrix multiplication: numpy.core._exceptions._ArrayMemoryError")
    print("It takes up too much space like 7.28 TiB when you calculate matrix multiplication in large arrays.\n")
else:
    numpy_end_time = time.time()

    # Print the result of time and matrix multiplication in python arrays
    print("Execution Time while processing matrix multiplicaition of numpy arrays in Q2.csv: {:.4f} seconds.\n".format(numpy_end_time - numpy_start_time))
