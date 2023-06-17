import os
from parsers.rule_parser import RuleParser
from utlis.console_utils import print_error, print_exception, print_failure, print_process, print_success
from utlis.files_utils import search_files_by_keyword




def startup():
    print_process("Reading rules")

    #check all rules
    local_dir = os.getcwd() + "/rules"

    ret_files = search_files_by_keyword(local_dir,"rule","json")

    rules = []

    for file in ret_files:
        try:
            print_process(f'Reading rule: {file}')
            rules.append(RuleParser.parse_file(file))
        except Exception as e:
            print_exception(e)
            print_failure("Cannot read rules")
            return

    print_success("Rules read successfully")
    
def execute():
    pass


startup()