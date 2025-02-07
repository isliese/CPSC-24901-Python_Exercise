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
    print('\n"L1.csv": ', end='')
    L1_data = csv_file_loader("L1.csv")
    if L1_data:
        print("Well loaded!")

    print('\n"Q1.csv": ', end='')
    Q1_data = csv_file_loader("Q1.csv")
    if L1_data:
        print("Well loaded!")

    print('\n"Q2.csv": ', end='')
    Q2_data = csv_file_loader("Q2.csv")
    if L1_data:
        print("Well loaded!")

    print('\n"L1.json": ', end='')
    L1_json_data = json_file_loader("L1.json")
    if L1_data:
        print("Well loaded!\n") 