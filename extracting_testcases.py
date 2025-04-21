import json
import re
from test_case_modifier import *

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
