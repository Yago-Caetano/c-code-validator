import os
import argparse

from tqdm import tqdm

from parsers.code_parser import CodeParser
from parsers.rule_parser import RuleParser
from utlis.console_utils import  print_exception, print_failure, print_process, print_success
from utlis.files_utils import search_files_by_keyword


ruleParser = RuleParser()

def startup(files,rules_directory):
    print_process("Own C Validator")
    print_process("Reading rules")

    #check all rules
    #local_dir = os.getcwd() + "/rules"

    ret_files = search_files_by_keyword(rules_directory,"rule","json")

    rules = []
    pbar = tqdm(ret_files)
    for file in pbar:
        try:
            pbar.set_description(f'Reading rule: {file}')
            rules.append(ruleParser.parse_file(file))
        except Exception as e:
            print_exception(e)
            print_failure("Cannot read rules")
            return

    print_success("Rules read successfully")

    #with this rules, let's check target files
    try:
        code_parser = CodeParser(rules)
        pbar = tqdm(files)

        for code in pbar:
            pbar.set_description(f"{code}")
            code_parser.parse_code_file(code)
        print_success("Finalizado")
    except Exception as e:
        print_exception(e)

def execute():
    pass

def main():
    parser = argparse.ArgumentParser(description="Own C sintax validator")
    parser.add_argument("--input","-i",nargs="+",help="List of C files to analyse",required=True)
    parser.add_argument("--rules_path","-r",help="Path to rules",required=True)

    args = parser.parse_args()

    in_files = args.input
    rules_path = args.rules_path

    startup(in_files,rules_path)


if __name__ == "__main__":
    main()