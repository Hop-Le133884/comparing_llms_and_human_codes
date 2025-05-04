import os
#import importlib
#import sys
#import glob
import csv
#import traceback

def extract_function_name(file_path, prefix_string):
    """
    Extract the function name from a .py file path.
    Assumes file name format: Deepseek_easy_<function_name>.py
    """
    # Get the base file name without path or extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # Remove the prefix (handle both 'Deepseek' and 'Deekseek' for robustness)
    prefix = prefix_string
    if file_name.startswith(prefix):
        return file_name[len(prefix):]
    elif file_name.startswith("Deekseek_easy_"):
        return file_name[len("Deekseek_easy_"):]
    
    # If no prefix, return the file name (or handle as needed)
    return file_name
def write_list_to_csv(data_list, file_path="output.csv", continue_writing=False):
    """
    Writes a list to a CSV file, with each item in the list as a separate column.

    Args:
        data_list (list): The list to write to the CSV file.
        file_path (str, optional): The path to the CSV file. Defaults to "output.csv".
        continue_writing (bool, optional): If True, append to the file; otherwise, overwrite.
                                         Defaults to False (overwrite).
    """
    try:
        mode = 'a' if continue_writing else 'w'  # Use 'a' for append, 'w' for write
        with open(file_path, mode=mode, newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write the list as a single row
            writer.writerow(data_list)
        print(f"List successfully {'appended to' if continue_writing else 'written to'} {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def basename_get(path_file, kind = True):
    tempt_base = path_file.replace("/", ".")
    if kind:
        return os.path.splitext(os.path.basename(tempt_base))[0]
    else:
        return os.path.splitext(os.path.basename(tempt_base))[0]
    

def avg(numbers, percentage=1):
    """
    Calculate the average of a list of numbers using built-in sum and len.
    Returns 0 for empty lists.
    """
    if not numbers:
        return 0
    return round((sum(numbers) / len(numbers))*percentage, 4)