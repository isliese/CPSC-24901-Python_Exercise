# Isla Kim

import numpy as np
import pandas as pd
import data_loader

# Load the data from Q1.csv and Q2.csv using the functions from data_loader.py
Q1_data = np.array(data_loader.csv_file_loader("Q1.csv"), dtype=float)
Q2_data = np.array(data_loader.csv_file_loader("Q2.csv"), dtype=float)

# Compute Mean and Standard Deviation for each column in Q1.csv and Q2.csv
def calculate_mean_std(data): # Define a function that calculates mean and Standard Deviation
    mean = np.mean(data, axis=0)
    std_dev = np.std(data, axis=0)
    return mean, std_dev

Q1_mean, Q1_std = calculate_mean_std(Q1_data)
Q2_mean, Q2_std = calculate_mean_std(Q2_data)

print("\n----------------------------------------------")
print(f'Mean of "Q1.csv" for each column: {Q1_mean}')
print(f'Standard Deviation of "Q1.csv for each column": {Q1_std}')
print(f'\nMean of "Q2.csv for each column": {Q2_mean}')
print(f'Standard Deviation of "Q2.csv for each column": {Q2_std}')
print("----------------------------------------------\n")

# Identify Outliers whose values are beyond 2 Standard Deviations
def identify_outliers(data, mean, std): # Define a function that identifies outliers
    outliers_2std = (data < mean - 2 * std) | (data > mean + 2 * std)
    outliers_1std = (data < mean - std) | (data > mean + std)

    if np.any(outliers_2std): # if there are outliers
        print("There are Outliers (beyond 2 std dev):", data[outliers_2std])
    else: # if there are no outliers
        print("No values beyond 2 std dev, showing values beyond 1 std dev:", data[outliers_1std])

print("\n----------------------------------------------")
print("In Q1.csv:")
identify_outliers(Q1_data, Q1_mean, Q1_std)

print("\nIn Q2.csv:")
identify_outliers(Q2_data, Q2_mean, Q2_std)
print("----------------------------------------------\n")

# Remove Outliers and Normalize Data
def normalize_data(data, mean, std):
    filtered_data = data[(data >= mean - 2 * std) & (data <= mean + 2 * std)]
    normalized = (filtered_data - np.min(filtered_data)) / (np.max(filtered_data) - np.min(filtered_data)) # Convert data to value between 0 and 1
    normalized = normalized - np.mean(normalized)  # Adjust mean to 0
    return normalized

Q1_normalized = normalize_data(Q1_data, Q1_mean, Q1_std)
Q2_normalized = normalize_data(Q2_data, Q2_mean, Q2_std)

# Randomly sample 10 values to verify normalization
print("\n----------------------------------------------")
Q1_normalized_random = np.random.choice(Q1_normalized, 10)
print("10 Random Samples from Normalized Q1 Data:\n", Q1_normalized_random)
if ((Q1_normalized_random > -1) & (Q1_normalized_random < 1)).all():
    print("-> Well converted!")
else: 
    print("-> Something wrong happened. Try again.")

Q2_normalized_random = np.random.choice(Q2_normalized, 10)
print("\n10 Random Samples from Normalized Q2 Data:\n", Q2_normalized_random)
if ((Q2_normalized_random > -1) & (Q2_normalized_random < 1)).all():
    print("-> Well converted!")
else: 
    print("-> Something wrong happened. Try again.")
print("----------------------------------------------\n")

# Convert to Pandas DataFrame and NumPy Array
Q1_df = pd.DataFrame(Q1_normalized, columns=['Normalized Q1'])
Q2_df = pd.DataFrame(Q2_normalized, columns=['Normalized Q2'])

print("\n----------------------------------------------")
print("10 Random Rows from Pandas Q1 DataFrame:\n", Q1_df.sample(10))
print("\n10 Random Rows from Pandas Q2 DataFrame:\n", Q2_df.sample(10))
print("----------------------------------------------\n")

# Convert to NumPy arrays
Q1_array = Q1_df.to_numpy()
Q2_array = Q2_df.to_numpy()

# Split into X (input) and Y (output) data
X_data = Q1_array[:, 0]
Y_data = Q2_array[:, 0]

print("\n----------------------------------------------")
print("X_data (First 10 values):\n", X_data[:10])
print("\nY_data (First 10 values):\n", Y_data[:10])
print("----------------------------------------------\n")