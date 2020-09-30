import sys
import csv
import re


def main():

    # Check if correct number of commant line arguments
    if len(sys.argv) != 3:
        print("Usage: python program.py file.csv file.txt")
        sys.exit(1)
    # Get list of STR sequences
    STR_list = get_STR_list(sys.argv[1])
    # Calculate largest consecutive repeat of each STR sequence in DNA sequence
    STR_repeats = read_DNA_Sequence(sys.argv[2], STR_list)
    # Compare STR repeat counts to individuals STR repeat counts in database
    return compare_STR_repeats(sys.argv[1], STR_repeats)
        

def get_STR_list(database_csv_file):
    # Open csv file, read STR sequences into memory as list and close file
    with open(sys.argv[1], "r") as csvfile:
        database_reader = csv.reader(csvfile)
        # Read first row of csv file (i.e the different STR sequences) into a list
        for first_row in database_reader:
            STR_list = first_row
            break
        # Remove first element (i.e. "name")
        del STR_list[0]
        return STR_list


def read_DNA_Sequence(sequence_txt_file, STR_list):
    with open(sys.argv[2], "r") as txtfile:
        dna_reader = txtfile.read()
    # Append STR sequences and their repeat counts to dictionary
    STR_repeats = {}
    for STR in STR_list:
        STR_repeats.update({STR: (get_STR_repeat(dna_reader, STR))})
    return STR_repeats
            
            
def get_STR_repeat(dna_sequence, STR_sequence):
    # Calculate longest consecutive repeat of given STR sequence
    repeat = 0
    pattern = str(STR_sequence)
    while pattern in dna_sequence:
        repeat += 1
        pattern += str(STR_sequence)
    return str(repeat)


def compare_STR_repeats(database_csv_file, STR_repeats):
    # Open database CSV file and read contents into memory as dictionary
    with open(sys.argv[1], "r") as csvfile:
        database_reader = csv.DictReader(csvfile)
        # Create copy of database dictionary to compare with STR repeat counts dictionary
        database_dict = {}
        for row in database_reader:
            # Reaplace key-value pairs in dictionary database copy with key-value pairs from current row
            database_dict.update(row)
            # Make copy of current individuals name from database
            name = database_dict['name']
            # Remove "name" element from current row 
            database_dict.pop("name")
            # Compare dictionary with values from current row to STR repeat counts dictionary
            if database_dict == STR_repeats:
                return print(f"{name}")
            else:
                continue
        return print("No match")
        

main()