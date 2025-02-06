# Isla Kim

import data_loader

# Load the data from Q1.csv and Q2.csv using the functions from data_loader.py
L1_data = np.array(data_loader.csv_file_loader("L1.csv"), dtype=float)
Q1_data = np.array(data_loader.csv_file_loader("Q1.csv"), dtype=float)

# Loads the 𝑥 values from “L1.csv” and from “Q1.csv”
L1_x = []
for row in L1_data:
    L1_x.append(row[1])

Q1_x = []
for row in Q1_data:
    Q1_x.append(row[1])

    