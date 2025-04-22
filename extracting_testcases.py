import json
import re
from test_case_modifier import *
import glob
import os

# Load JSON data from a file or a string
def read_json_file(file_path):
    # Introdue file error here before open
   
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def extracting_info(algo, difficult_level, json_file):
    # extracting problems's name and markdown description, test_case_generator, 
    # solution inside test_case_generator
    count = 0
    json_len = len(json_file)
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
        
        path_to_file = create_empty_LLM_solution(difficult_level, function_name)
        # Extracting markdown description output to prompt file
        create_desciption_prompt(task_name, path_to_file, difficult_level, 
                                 function_name, temp_dict)
        
        search_case = str("\n")
        # Extracting solution
        # Extracting generator, temp_dict["markdown_description"]
        with open(path_to_file+ difficult_level.lower()+ "_test_generator_"+
                  function_name+ ".py", "w") as generator:
            #"def generate_test_case()")"def test_generated_test_cases")
            #write import
            import_helper(generator, temp_dict["test_case_generator"], temp_dict["canonical_solution"])
            #special case
            if "searchMatrix" in temp_dict["test_case_generator"]:
                for line in temp_dict["test_case_generator"].splitlines():
                    if line == "test_case_generator_results = []":
                        break
                    if line == "\n":
                        continue
                    line = "\n" + line
                    search_case += line

            #test case generator for search Matrix
                with open("search_matrix_test_geneator.txt", "r") as search_matrix_generator:
                    for matrix_line in search_matrix_generator:
                        if matrix_line == "\n":
                            continue
                        matrix_line = "\n" + matrix_line
                        search_case += matrix_line
                temp_dict["test_case_generator"] = search_case.strip("\n")
        
            # write to test_case_generator

            testcase_idx = find_first_return_index_fast(temp_dict["test_case_generator"].splitlines(), \
                                                         "def test_generated_test_cases")
            solution_idx = find_first_return_index_fast(temp_dict["test_case_generator"].splitlines(), \
                                                        "def generate_test_case()")

            # splitting parts
            temp_solution = temp_dict["test_case_generator"].splitlines()[:solution_idx]
            temp_testcase = temp_dict["test_case_generator"].splitlines()[solution_idx:testcase_idx]
            generated_testcase = temp_dict["test_case_generator"].splitlines()[testcase_idx:]

            solution_writting(generator, temp_solution)
            generate_test_case_cleaning(generator, temp_testcase)
            generated_test_case_cleaning(generator, generated_testcase)



#from test_case_modifier import find_first_return_index_fast


def creating_json_memory_measurer(algo, difficult_level, json_file, LLM_list, LLM_output, human_list=False):
    # extracting problems's name and markdown description, test_case_generator, 
    # solution inside test_case_generator
    count = 0
    human_json = []
    json_len = len(json_file)
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

        temp_list = list(temp_dict.items())[:-2]
        temp_dict = dict(temp_list)
        if human_list:
            temp_dict["completion"] = temp_dict["canonical_solution"]
            human_json.append(temp_dict)
        #extracting function name
        test_case_string = temp_dict['test_case']
        match = re.search(r"solution\.(\w+)\(", test_case_string)
        if match:
            function_name = match.group(1)
        
        lvl_sub = difficult_level.lower()
        dir_llm = LLM_output + lvl_sub + "/"
        files = glob.glob(os.path.join(dir_llm, f"*{function_name}.py"))
        #task_name = temp_dict["task_name"]
        #dseasy_sol_path = dir_llm + files[0], HitCounter: MajorityChecker

        #read solution from ds
        with open(files[0], 'r') as ds_f:
            llm_easysolution = ds_f.read()
        #canonical solution
        # Replace "LLM_Solution" with "Solution" in the entire content
        if "HitCounter" in temp_dict["canonical_solution"]:
            modified_solution = llm_easysolution.replace("LLM_Solution", "HitCounter")
        elif "MajorityChecker" in temp_dict["canonical_solution"]:
            modified_solution = llm_easysolution.replace("LLM_Solution", "MajorityChecker")
        else:
            modified_solution = llm_easysolution.replace("LLM_Solution", "Solution")
        
        # modified canonical to llm solution
        temp_dict["completion"] = "```python\n" + modified_solution + "\n```"
        # modified testcase generator to llm solution
        #index to split
        """class_idx = find_first_return_index_fast(temp_dict["test_case_generator"].splitlines(), \
                                                "class")
        generator_idx = find_first_return_index_fast(temp_dict["test_case_generator"].splitlines(), \
                                            "def generate_test_case()")
        # split
        lines_testcase = temp_dict["test_case_generator"].splitlines()
        canonical_lines = temp_dict["canonical_solution"].splitlines()
        new_lines_testcase = lines_testcase[:class_idx] + canonical_lines + lines_testcase[generator_idx:]

        #replace test case generator
        temp_dict["test_case_generator"] = "\n".join(new_lines_testcase)"""
        
        # add all json data to one list
        LLM_list.append(temp_dict)

    return human_json