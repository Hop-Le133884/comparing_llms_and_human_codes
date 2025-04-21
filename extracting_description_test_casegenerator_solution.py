import json
import re

# Load JSON data from a file or a string
def read_json_file(file_path):
    # Introdue file error here before open
   
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Extract text from the markdown description

def extracting_markdown_desciption(raw_desc):
    descriptions = []
    # Extract text after ">"
    for line in raw_desc.splitlines():
        # continue to remove junk words
        if line != '' and line != '```' and line != '\xa0':
            descriptions.append(line)
    
    return descriptions

def extracting_info(algo, difficult_level, json_file):
    # extracting problems's name and markdown description, test_case_generator, 
    # solution inside test_case_generator
    json_len = len(json_file)
    count = 0

    for json_idx in range(json_len):
        temp_dict = json_file[json_idx]
        # filtering
        if temp_dict["difficulty"] != difficult_level or algo != temp_dict["algorithms"]:
            continue
        # update count or break
        if count == 10:
            break
        else:
            count += 1

        # Name, level + task_name + key(solution, generator, prompt)

        task_name = temp_dict["task_name"]

        #extracting function name
        test_case_string = temp_dict['test_case']
        match = re.search(r"solution\.(\w+)\(", test_case_string)
        if match:
            function_name = match.group(1)

        # create path to json file
        # also create solution file name for each LLMs
        if difficult_level == "Easy":
            path_to_file = "easy/"
            #Deepseek
            easy_path = "Deepseek_Outputs/easy/"
            with open(easy_path+"Deekseek_"+f"{difficult_level.lower()}_{function_name}.py", "w") as file:
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
            with open(easy_path+"Deekseek_"+f"{difficult_level.lower()}_{function_name}.py", "w") as file:
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
            with open(easy_path+"Deekseek_"+f"{difficult_level.lower()}_{function_name}.py", "w") as file:
                file.write("")
            #Gemini
            easy_path = "Gemini_Outputs/hard/"
            with open(easy_path+"Gemini_"+f"{difficult_level.lower()}_{function_name}.py", "w") as file:
                file.write("")
            #GPT
            easy_path = "GPT_Outputs/hard/"
            with open(easy_path+"GPT_"+f"{difficult_level.lower()}_{function_name}.py", "w") as file:
                file.write("")


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
        
        # Extracting solution
        
        # Variable skip
        repeated_solution_cout = 0
        # Extracting generator
        with open(path_to_file+ difficult_level.lower()+ "_test_generator_"+
                  function_name+ ".py", "w") as generator:
            #check if any undefied libraries
            if "lcm" in temp_dict["test_case_generator"] and "import lcm" \
                not in temp_dict["test_case_generator"]:
                generator.write(f"\nfrom math import lcm")
            # Counter
            if "Counter" in temp_dict["test_case_generator"] and "import Counter"\
                  not in temp_dict["test_case_generator"]:
                generator.write(f"\nfrom collections import Counter")
            # bisect
            if "bisect" in temp_dict["test_case_generator"]:
                generator.write(f"\nfrom bisect import *")
            #tee
            if "tee" in temp_dict["test_case_generator"]:
                generator.write(f"\nfrom itertools import tee")
            #List
            if "List" in temp_dict["test_case_generator"] and "import List" \
                not in temp_dict["test_case_generator"]:
                generator.write(f"\nfrom typing import List")
            #random
            if "random" in temp_dict["test_case_generator"] and "import random" \
                not in temp_dict["test_case_generator"]:
                generator.write(f"\nimport random")
            
            # Loop through the lines
            for line in temp_dict["test_case_generator"].splitlines():
                if "test_generated_test_cases" in line:
                    line = line.replace("(num_tests)", "(num_tests, llm_solution)")
                # start with 
                if "solution = Solution()" in line:
                    repeated_solution_cout += 1
                    if repeated_solution_cout == 2:
                        line = line.replace("Solution()", "llm_solution")
                generator.write(line + "\n")


# Usage
if __name__ == "__main__":
    file_path = "dataset_with_difficulty_and_algorithm.json"  # Replace with your JSON file path
    try:
        json_data = read_json_file(file_path)
        #pretty_print_json(json_data)
    except FileNotFoundError:
        print(f"File {file_path} not found. Please check the file path.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

#####################
difficult_level = ["Easy", "Hard", "Medium"]
algo = ["binary_search"]

# loop through diff level
for diff_lvl in difficult_level:
    extracting_info(algo, diff_lvl, json_data)