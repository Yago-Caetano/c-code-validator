import os
import argparse

from tqdm import tqdm
from constants.strings import StringsConstants
from exceptions.lib_clang_not_found_exception import LibClangNotFoundException

from parsers.code_parser import CodeParser
from parsers.rule_parser import RuleParser
from utlis.console_utils import  print_exception, print_failure, print_header, print_process, print_success
from utlis.files_utils import search_files_by_keyword


ruleParser = RuleParser()

def check_prerequisites():

    #check if there is libclang environment variable
    if (os.environ.get('LIBCLANG_LIBRARY_PATH') is None):
        raise LibClangNotFoundException()
    

def startup(files,rules_directory):

    check_prerequisites()

    print_header()
    print_process(StringsConstants.PARSING_RULES_TITLE)
    
    rules = []
    ret_files = search_files_by_keyword(rules_directory,"rule","json")

    if(len(ret_files) == 0):
        print_failure(StringsConstants.NO_RULES_FOUND)
        return
    
    pbar = tqdm(ret_files)
    for file in pbar:
        try:
            pbar.set_description(f'Reading rule: {file}')
            rules.append(ruleParser.parse_file(file))
        except Exception as e:
            print_exception(e)
            print_failure(StringsConstants.RULE_PARSING_FAILED)
            return

    print_success(StringsConstants.RULE_PARSING_SUCCEDED)

    try:
        print_process(StringsConstants.CODE_CHECKING_TITLE)

        code_parser = CodeParser(rules)
        pbar = tqdm(files)

        for code in pbar:
            pbar.set_description(f"{code}")
            code_parser.parse_code_file(code)
        print_success(StringsConstants.CODE_CHECKING_SUCCEDED)
    except Exception as e:
        print_exception(e)

def execute():
    pass

def main():
    parser = argparse.ArgumentParser(description=StringsConstants.TITLE)
    parser.add_argument("--input","-i",nargs="+",help="List of C files to analyse",required=True)
    parser.add_argument("--rules_path","-r",help="Path to rules",required=True)

    args = parser.parse_args()

    in_files = args.input
    rules_path = args.rules_path

    startup(in_files,rules_path)


if __name__ == "__main__":
    main()