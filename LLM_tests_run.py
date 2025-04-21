import sys
import time
import importlib
from helper_functions import basename_get, extract_function_name


def LLM_tests_run(ds_prefix, deepseek_files, gpt_prefix, gpt_files, gemini_prefix, 
                  gemini_files, human_prefix, human_files):
    gpt_ET_list = []
    gpt_failed_test = []
    human_ET_list = []
    human_failed_test = []
    gemini_ET_list = []
    gemini_failed_test = []
    deepseek_ET_list = []
    deepseek_failed_test = []

    for human_file in human_files:
        func_name = extract_function_name(human_file, human_prefix)
        #print(f"{func_name}")
        #print(human_file)
        human_basename = basename_get(human_file)
        #print(human_module)
        human_module = importlib.import_module(human_basename)
        args, test_cases_assertion = human_module.test_generated_test_cases(100)
        for deepseek_file in deepseek_files:
            ds_name = extract_function_name(deepseek_file, ds_prefix)
            if ds_name == func_name:
                #print(f"{ds_name}")
                LLM_basename = basename_get(deepseek_file, False)
                
                #print(LLM_module)
                LLM_module = importlib.import_module(LLM_basename)
                # call LLM solution
                try:
                    solution = LLM_module.LLM_Solution(args[0])
                except:
                    try:
                        solution = LLM_module.LLM_Solution()
                    except:
                        print(f"No LLM_Solution import found, {LLM_basename}")
                
                # start to assert
                for test_assertion in test_cases_assertion:
                    
                    try:
                        start_time = time.time()
                        exec(test_assertion)
                        ds_ET = (time.time() - start_time)*1000
                        deepseek_ET_list.append(ds_ET)
                    except:
                        if ds_name in deepseek_failed_test:
                            continue
                        else:
                            deepseek_failed_test.append(ds_name)
                
                # cleanning import libraries
                # Check if the module was imported and is in sys.modules
                if LLM_module in sys.modules:
                    # Remove the module from sys.modules to "clean" the import
                    del sys.modules[LLM_module]
                
                deepseek_files.remove(deepseek_file)
                break # find the file, no need to keep running loop
            
            else:
                continue
        
        for gpt_file in gpt_files:
            gpt_name = extract_function_name(gpt_file, gpt_prefix)
            if gpt_name == func_name:
                #print(f"{gpt_name}")
                LLM_basename = basename_get(gpt_file, False)
                #print(LLM_module)
                LLM_module = importlib.import_module(LLM_basename)
                # call LLM solution
                try:
                    solution = LLM_module.LLM_Solution(args[0])
                except:
                    try:
                        solution = LLM_module.LLM_Solution()
                    except:
                        print(f"No LLM_Solution import found, {LLM_basename}")
                
                # start to assert
                for test_assertion in test_cases_assertion:
                    
                    try:
                        start_time = time.time()
                        exec(test_assertion)
                        gpt_ET = (time.time() - start_time)*1000
                        gpt_ET_list.append(gpt_ET)
                    except:
                        if gpt_name in gpt_failed_test:
                            continue
                        else:
                            gpt_failed_test.append(gpt_name)
                
                # cleanning import libraries
                # Check if the module was imported and is in sys.modules
                if LLM_module in sys.modules:
                    # Remove the module from sys.modules to "clean" the import
                    del sys.modules[LLM_module]

                gpt_files.remove(gpt_file) #remove to remove next running loop
                break # find the file, no need to keep running loop
            else:
                continue

        for gemini_file in gemini_files:
            gemini_name = extract_function_name(gemini_file, gemini_prefix)
            if gemini_name == func_name:
                #print(f"{gemini_name}")
                LLM_basename = basename_get(gemini_file, False)
                #print(LLM_module)
                LLM_module = importlib.import_module(LLM_basename)
                # call LLM solution
                try:
                    solution = LLM_module.LLM_Solution(args[0])
                except:
                    try:
                        solution = LLM_module.LLM_Solution()
                    except:
                        print(f"No LLM_Solution import found, {LLM_basename}")
                
                # start to assert
                for test_assertion in test_cases_assertion:
                    
                    try:
                        start_time = time.time()
                        exec(test_assertion)
                        gemini_ET = (time.time() - start_time)*1000
                        gemini_ET_list.append(gemini_ET)
                    except:
                        if gemini_name in gemini_failed_test:
                            continue
                        else:
                            gemini_failed_test.append(gemini_name)
                
                gemini_files.remove(gemini_file) #remove to remove next running loop
                break # find the file, no need to keep running loop
            else:
                continue

        # running test from human
        #    for human_file in human_files:
        human_name = extract_function_name(human_file, human_prefix)
        
        #use try to handle special
        try:
            solution = human_module.MajorityChecker(args[0])
        except:
            try:
                solution = human_module.Solution(args[0])
            except:
                try:
                    solution = human_module.HitCounter()
                except:
                    try:
                        solution = human_module.Solution()
                    except:
                        print(f"No human Solution import found, {human_basename}")

            # start to assert
            for test_assertion in test_cases_assertion:
                
                try:
                    start_time = time.time()
                    exec(test_assertion)
                    human_ET = (time.time() - start_time)*1000
                    human_ET_list.append(human_ET)
                except:
                    if human_name in human_failed_test:
                        continue
                    else:
                        human_failed_test.append(human_name)

    return   deepseek_ET_list, deepseek_failed_test, gpt_ET_list, gpt_failed_test, \
        gemini_ET_list, gemini_failed_test, human_ET_list, human_failed_test
    
