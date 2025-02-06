# Isla Kim

import json
import csv

# Define a function that loads csv file and save the data into Python array data structures.
def csv_file_loader(file_name):
    with open(file_name, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        data = list(csvreader)  
    return data  

# Define a function that loads json file and save the data into Python array data structures.
def json_file_loader(file_name):
    with open(file_name, 'r') as jsonfile:
        json_data = json.load(jsonfile)  
        json_data_array = json_data["linear"]  
    return json_data_array  

# Read and load the data stored in each of the file “L1.csv”, “Q1.csv”, “Q2.csv”, “L1.json”
if __name__ == "__main__": # Process only when this script runs directly
    print('\n"L1.csv": ')
    L1_data = csv_file_loader("L1.csv")
    for row in L1_data:
        print(row) 

    print('\n"Q1.csv": ')
    Q1_data = csv_file_loader("Q1.csv")
    for row in Q1_data:
        print(row)  

    print('\n"Q2.csv": ')
    Q2_data = csv_file_loader("Q2.csv")
    for row in Q2_data:
        print(row) 

    print('\n"L1.json": ')
    L1_json_data = json_file_loader("L1.json")
    for row in L1_json_data:
        print(row) 
