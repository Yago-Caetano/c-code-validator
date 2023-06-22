from exceptions.criterion_not_respected_exception import  CriterionNotRespectedException
import re

def criterion_handler_lenght_less_than(node,rule,length):
    if(len(node.displayname) > length):
        raise CriterionNotRespectedException("Rule: \"" + rule.get_file_name() + "\" on node \"" + node.displayname + "\" at " + str(node.location.file) + ":" + str(node.location.line) + ":" + str(node.location.column))
    

def criterion_handler_lenght_bigger_than(node,rule,length):
    if(len(node.displayname) < length):
        raise CriterionNotRespectedException("Rule: \"" + rule.get_file_name() + "\" on node \"" + node.displayname + "\" at " + str(node.location.file) + ":" + str(node.location.line) + ":" + str(node.location.column))
    
def criterion_handler_prefix(node,rule,prefix):
    if(not node.displayname.startswith(prefix)):
        raise CriterionNotRespectedException("Rule: \"" + rule.get_file_name() + "\" on node \"" + node.displayname + "\" at " + str(node.location.file) + ":" + str(node.location.line) + ":" + str(node.location.column))

def criterion_handler_suffix(node,rule,suffix):
    if(not node.displayname.endswith(suffix)):
        raise CriterionNotRespectedException("Rule: \"" + rule.get_file_name() + "\" on node \"" + node.displayname + "\" at " + str(node.location.file) + ":" + str(node.location.line) + ":" + str(node.location.column))

def criterion_handler_regex(node,rule,regex):
    if(re.match(regex,node.displayname) is None):
        raise CriterionNotRespectedException("Rule: \"" + rule.get_file_name() + "\" on node \"" + node.displayname + "\" at " + str(node.location.file) + ":" + str(node.location.line) + ":" + str(node.location.column))

