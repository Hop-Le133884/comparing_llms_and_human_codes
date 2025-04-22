import re

def import_helper(generator, temp_dict, canonical_solution):
    #check if any undefied libraries
    if "import time" not in temp_dict:
        generator.write(f"import time\n")
    if "lcm" in temp_dict and "import lcm" not in temp_dict:
        generator.write(f"\nfrom math import lcm\n")
    # Counter
    if "Counter" in temp_dict and "import Counter" not in temp_dict:
        generator.write(f"\nfrom collections import Counter\n")
    # bisect
    if "bisect" in temp_dict:
        generator.write(f"\nfrom bisect import *\n")
    #tee
    if "tee" in temp_dict:
        generator.write(f"\nfrom itertools import tee\n")
    #List
    if "List" in temp_dict and "import List" not in temp_dict:
        generator.write(f"\nfrom typing import List\n")
    #random
    if "import random" not in temp_dict:
        generator.write(f"\nimport random\n")
    
    if "findNthDigit" in temp_dict:
        for line in canonical_solution.splitlines():
            generator.write(line +"\n")

def find_first_return_index_fast(string_list, key):
    try:
        return next(idx for idx, s in enumerate(string_list) if f"{key}" in s)
    except StopIteration:
        return None

def create_empty_LLM_solution(difficult_level, function_name):
    # create path to json file
        # also create solution file name for each LLMs
    if difficult_level == "Easy":
        path_to_file = "easy/"
        #Deepseek
        easy_path = "Deepseek_Outputs/easy/"
        with open(easy_path+"Deepseek_"+f"{difficult_level.lower()}_{function_name}.py", "w") as file:
            file.write("")
        #Gemini
        easy_path = "Gemini_Outputs/easy/"
        with open(easy_path+"Gemini_"+f"{difficult_level.lower()}_{function_name}.py", "w") as file:
            file.write("")
        #GPT
        easy_path = "GPT_Outputs/easy/"
        with open(easy_path+"GPT_"+f"{difficult_level.lower()}_{function_name}.py", "w") as file:
            file.write("")
    if difficult_level == "Medium":
        path_to_file = "medium/"
        #Deepseek
        easy_path = "Deepseek_Outputs/medium/"
        with open(easy_path+"Deepseek_"+f"{difficult_level.lower()}_{function_name}.py", "w") as file:
            file.write("")
        #Gemini
        easy_path = "Gemini_Outputs/medium/"
        with open(easy_path+"Gemini_"+f"{difficult_level.lower()}_{function_name}.py", "w") as file:
            file.write("")
        #GPT
        easy_path = "GPT_Outputs/medium/"
        with open(easy_path+"GPT_"+f"{difficult_level.lower()}_{function_name}.py", "w") as file:
            file.write("")
    if difficult_level == "Hard":
        path_to_file = "hard/"
        #Deepseek
        easy_path = "Deepseek_Outputs/hard/"
        with open(easy_path+"Deepseek_"+f"{difficult_level.lower()}_{function_name}.py", "w") as file:
            file.write("")
        #Gemini
        easy_path = "Gemini_Outputs/hard/"
        with open(easy_path+"Gemini_"+f"{difficult_level.lower()}_{function_name}.py", "w") as file:
            file.write("")
        #GPT
        easy_path = "GPT_Outputs/hard/"
        with open(easy_path+"GPT_"+f"{difficult_level.lower()}_{function_name}.py", "w") as file:
            file.write("")

    return path_to_file

def extracting_markdown_desciption(raw_desc):
    # Extract text from the markdown description
    descriptions = []
    # Extract text after ">"
    for line in raw_desc.splitlines():
        # continue to remove junk words
        if line != '' and line != '```' and line != '\xa0':
            descriptions.append(line)
    
    return descriptions

def create_desciption_prompt(task_name, path_to_file, difficult_level, function_name,  temp_dict):
    #temp_dic["markdown_desciption"]
    # Extracting markdown description output to prompt file
    with open(path_to_file+ difficult_level.lower()+ "_descr_"+ 
                function_name+ ".txt", "w") as markdow_file:

        #Add precise prompt
        temp_header = f"Solve the following problem using python script titled \
            '{difficult_level.lower()}_{function_name}.py'. Only include function,\
                    named '{function_name}' within Class 'LLM_Solution'.\n"

        markdow_file.write(temp_header + "\n")

        markdow_file.write(task_name + "\n")
        # Loop thourgh the lines
        for line in extracting_markdown_desciption(temp_dict["markdown_description"]):
            markdow_file.write(line + "\n")
    
def solution_writting(generator, temp_testcase):
    for line in temp_testcase:
        generator.write(line+"\n")


def generate_test_case_cleaning(generator, temp_testcase):
    for line in temp_testcase:
        generator.write(line+"\n")

    
def generated_test_case_cleaning(generator, temp_testcase):
    adding_return = ''
    for line in temp_testcase:
        if "= generate_test_case()" in line:
            variable_word = ''
            for word in line.split():
                if word == 'expected_result' or word == 'expected_results':
                    break
                else:
                    variable_word += word
                    #print(variable_word)
            adding_return = re.sub(",$", "", variable_word)
        if "return" in line:
            #global new_rep
            new_rep = "return " + "(" + adding_return + "),"
            line = line.replace("return", new_rep)
            #print(new_rep)
        if "print" in line and "assert" in line:
            continue
        #print(new_rep)
        generator.write(line+"\n")
