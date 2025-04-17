import random
import json

# Load JSON data from a file or a string
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Extract text from the markdown description

def extracting_markdown_desciption(raw_desc):
    descriptions = []
    # Extract text after ">"
    for line in raw_desc.splitlines():
        #join list of sentences and remove the &qout;
        #sentence = ''.join(list_words).replace("&quot;", '')
        # continue to remove junk words
        if line != '' and line != '```' and line != '\xa0':
            descriptions.append(line)
    
    return descriptions

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

        # create path to folder
        if difficult_level == "Easy":
            path_to_file = "easy_probs/" #+ difficult_level.lower() + "_problems.json"
        if difficult_level == "Medium":
            path_to_file = "medium_probs/" #+ difficult_level.lower() + "_problems.json"
        if difficult_level == "Hard":
            path_to_file = "hard_probs/" # + difficult_level.lower() + "_problems.json"

        # extracting info from dictionary
        filtered_dict = {key: value for key, value in temp_dict.items() 
                         if key == "task_name" or key == "markdown_description" 
                         or key == "test_case_generator" or key == "difficulty"
                         or key == "algorithms"}

        # Name, level + task_name + key(solution, generator, prompt)

        task_name = temp_dict["task_name"]
        #extracting naming
        if len(task_name.split()) > 2:
            naming_file = (" ".join(task_name.split()[:2]) + "_"+ task_name.split()[-1]).lower()
        else:
            naming_file = task_name.lower().replace(" ", "_")

        # Extracting markdown description output to prompt file
        with open(path_to_file+ difficult_level.lower()+ "_descr_"+ 
                  naming_file+ ".txt", "w") as markdow_file:
            markdow_file.write(task_name + "\n")
            # Loop thourgh the lines
            for line in extracting_markdown_desciption(temp_dict["markdown_description"]):
                markdow_file.write(line + "\n")
        
        # Extracting generator
        with open(path_to_file+ difficult_level.lower()+ "_generator_"+
                  naming_file+ ".py", "w") as generator:
            # Loop through the lines
            for line in temp_dict["test_case_generator"].splitlines():
                generator.write(line + "\n")

        # Extracting solution
        with open(path_to_file+ difficult_level.lower()+ "_solution_"+
                  naming_file+ ".py", "w") as solution_code:
            # Loop through the lines
            for line in temp_dict["test_case_generator"].splitlines():
                if line == "def generate_test_case():":
                    break
                solution_code.write(line + "\n")


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