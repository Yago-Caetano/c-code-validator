import os

from parsers.code_parser import CodeParser
from parsers.rule_parser import RuleParser
from utlis.console_utils import  print_exception, print_failure, print_process, print_success
from utlis.files_utils import search_files_by_keyword


ruleParser = RuleParser()

def startup():
    print_process("Reading rules")

    #check all rules
    local_dir = os.getcwd() + "/rules"

    ret_files = search_files_by_keyword(local_dir,"rule","json")

    rules = []

    for file in ret_files:
        try:
            print_process(f'Reading rule: {file}')
            rules.append(ruleParser.parse_file(file))
        except Exception as e:
            print_exception(e)
            print_failure("Cannot read rules")
            return

    print_success("Rules read successfully")

    #with this rules, let's check target files
    code_files = search_files_by_keyword(os.getcwd(),"code","c")
    try:
        code_parser = CodeParser(rules)
        for code in code_files:
            code_parser.parse_code_file(code)
        print_success("Finalizado")
    except Exception as e:
        print_exception(e)

def execute():
    pass


startup()