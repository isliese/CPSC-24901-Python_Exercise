# Isla Kim

import numpy as np
import pandas as pd
import data_loader

# Load the data from Q1.csv and Q2.csv using the functions from data_loader.py
Q1_data = np.array(data_loader.csv_file_loader("Q1.csv"), dtype=float)
Q2_data = np.array(data_loader.csv_file_loader("Q2.csv"), dtype=float)

def calculate_mean_std(data):
    mean = np.mean(data, axis=0)
    std_dev = np.std(data, axis=0)
    return mean, std_dev

# Compute Mean and Standard Deviation for each column in Q1.csv and Q2.csv
Q1_mean, Q1_std = calculate_mean_std(Q1_data)
Q2_mean, Q2_std = calculate_mean_std(Q2_data)

print(f'\nMean of "Q1.csv": {Q1_mean}')
print(f'Standard Deviation of "Q1.csv": {Q1_std}')
print(f'\nMean of "Q2.csv": {Q2_mean}')
print(f'Standard Deviation of "Q2.csv": {Q2_std}')

# Identify Outliers (Values beyond 2 Standard Deviations)
def identify_outliers(data, mean, std):
    outliers_2std = (data < mean - 2 * std) | (data > mean + 2 * std)
    outliers_1std = (data < mean - std) | (data > mean + std)

    if np.any(outliers_2std):
        print("Outliers (beyond 2 std dev):", data[outliers_2std])
    else:
        print("No values beyond 2 std dev, showing values beyond 1 std dev:", data[outliers_1std])

print("\nOutliers in Q1.csv:")
identify_outliers(Q1_data, Q1_mean, Q1_std)

print("\nOutliers in Q2.csv:")
identify_outliers(Q2_data, Q2_mean, Q2_std)

# Remove Outliers and Normalize Data
def normalize_data(data, mean, std):
    filtered_data = data[(data >= mean - 2 * std) & (data <= mean + 2 * std)]
    normalized = (filtered_data - np.min(filtered_data)) / (np.max(filtered_data) - np.min(filtered_data))
    normalized = normalized - np.mean(normalized)  # Adjust mean to 0
    return normalized

Q1_normalized = normalize_data(Q1_data, Q1_mean, Q1_std)
Q2_normalized = normalize_data(Q2_data, Q2_mean, Q2_std)

# Randomly sample 10 values to verify normalization
print("\n10 Random Samples from Normalized Q1 Data:", np.random.choice(Q1_normalized, 10))
print("\n10 Random Samples from Normalized Q2 Data:", np.random.choice(Q2_normalized, 10))

# Convert to Pandas DataFrame and NumPy Array
Q1_df = pd.DataFrame(Q1_normalized, columns=['Normalized Q1'])
Q2_df = pd.DataFrame(Q2_normalized, columns=['Normalized Q2'])

print("\n10 Random Rows from Pandas Q1 DataFrame:\n", Q1_df.sample(10))
print("\n10 Random Rows from Pandas Q2 DataFrame:\n", Q2_df.sample(10))

# Convert to NumPy arrays
Q1_array = Q1_df.to_numpy()
Q2_array = Q2_df.to_numpy()

# Split into X (input) and Y (output) data
X_data = Q1_array[:, 0]
Y_data = Q2_array[:, 0]

print("\nX_data (First 10 values):", X_data[:10])
print("\nY_data (First 10 values):", Y_data[:10])
