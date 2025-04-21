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

"""    for line in temp_testcase:
        if "expected_results = []" in line or "expected_results.append(" in line:
            generator.write(line+"\n")
            continue
        elif "expected_result" in line:
            if "return" in line:
                line = line.replace("return", "return human_ET,")
            else:
                indent = len(line) - len(line.lstrip())
                generator.write(indent*' ' +"start_time = time.time()\n")
                generator.write(line + "\n")
                #generator.write("first condition expected_re")
                generator.write(indent*' ' +"human_ET = (time.time() - start_time)*1000" + "\n")
                continue
        generator.write(line+"\n")"""

    
def generated_test_case_cleaning(generator, temp_testcase):
    for line in temp_testcase:
        generator.write(line+"\n")

"""    for line in temp_testcase:
        if "test_generated_test_cases" in line:
            line = line.replace("(", "(LLM, ")
            line = line.replace(")", ", llm_solution)")
            generator.write(line + "\n")
            continue
        
        elif  line == "test_case_generator_results = []":
            generator.write(line+"\n")
            generator.write("LLMaverage_ET = []\n")
            generator.write("LLMaverage_ET = []\n")
            continue

        elif "generate_test_case()" in line:
            indent = len(line) - len(line.lstrip())
            starting = indent*' ' + "human_ET, "
            for word in line.split():
                starting += word + ' '

         # start with 
        elif "solution = Solution()" in line:
            line = line.replace("Solution()", "llm_solution")
        elif "solution = MajorityChecker(arr)" in line:
            line = line.replace("MajorityChecker(arr)", "llm_solution(arr)")

                
        elif "== expected_result" in line:
            indent = len(line) - len(line.lstrip())
            generator.write(indent*' ' +"start_time = time.time()" + "\n")
            generator.write(line +"\n")
            generator.write(indent*' ' +'LLM_ET = f"{LLM}_ET"' +"\n")                      
            generator.write(indent*' ' +"LLM_ET = (time.time() - start_time)*1000" +"\n")
            continue    
        if "expected_results = generate_test_case()" in line:
                    expect_result_cout += 1
                    if "return" in line:
                        line = line.replace("return", "return human_ET,")
                    if expect_result_cout == 1:
                        if count_indent == 1:
                            generator.write(indent*4 +"start_time = time.time()" + "\n")
                            generator.write(line + "\n")
                            #generator.write("first condition expected_re")
                            generator.write(indent*4 +"human_ET = (time.time() - start_time)*1000" + "\n")
                            continue
                        elif count_indent == 2:
                            generator.write(indent*8 +"start_time = time.time()" + "\n")
                            generator.write(line + "\n")
                            generator.write(indent*8 +"human_ET = (time.time() - start_time)*1000" + "\n")
                            continue
"""
        
    