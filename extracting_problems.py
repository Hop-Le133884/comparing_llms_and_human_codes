import random
import json

# Load JSON data from a file or a string
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def extracting_info(algo, difficult_level, json_file):
    # extracting problems's name and markdown description, test_case_generator, 
    # solution inside test_case_generator
    json_len = len(json_file)
    count = 0
    used_indices = set() # tracking random number
    output_json = []
    while count < 10: 
        random_int = random.randint(0,json_len-1)
        if random_int in used_indices:
            continue
        # update used_indices
        used_indices.add(random_int)
        temp_dict = json_file[random_int]
        # filtering
        if temp_dict["difficulty"] != difficult_level or algo not in temp_dict["algorithms"]:
            continue
        if len(temp_dict["algorithms"]) != 1:
            continue
        # update data
        count += 1

        # create path to json file
        if difficult_level == "Easy":
            path_to_file = "easy_probs/" + difficult_level.lower() + "_problems.json"
        if difficult_level == "Medium":
            path_to_file = "medium_probs/" + difficult_level.lower() + "_problems.json"
        if difficult_level == "Hard":
            path_to_file = "hard_probs/" + difficult_level.lower() + "_problems.json"

        # extracting info from dictionary
        filtered_dict = {key: value for key, value in temp_dict.items() 
                         if key == "task_name" or key == "markdown_description" 
                         or key == "test_case_generator" or key == "difficulty"
                         or key == "algorithms"}

        # add to list
        output_json.append(filtered_dict)
        # save json file
        with open(path_to_file, "w") as jsonfile:
            json.dump(output_json, jsonfile, indent=4) # indent make the file more readable
    
        # break if 10 probs found
        if count == 10:
            break

# Example usage
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
algo = "binary_search"

# loop through diff level
for diff_lvl in difficult_level:
    extracting_info(algo, diff_lvl, json_data)