from exceptions.criterion_not_respected_exception import  CriterionNotRespectedException


def criterion_handler_lenght_less_than(node,rule,length):
    if(len(node.displayname) > length):
        raise CriterionNotRespectedException("Rule: \"" + rule.get_name() + "\" at " + rule.get_file_name() + " on " + node.displayname + " at " + str(node.extent.start.file))
    

def criterion_handler_lenght_bigger_than(node,rule,length):
    if(len(node.displayname) < length):
        raise CriterionNotRespectedException("Rule: \"" + rule.get_name() + "\" at " + rule.get_file_name() + " on " + node.displayname + " at " + str(node.extent.start.file))
    
def criterion_handler_prefix(node,rule,prefix):
    if(not node.displayname.startswith(prefix)):
        raise CriterionNotRespectedException("Rule: \"" + rule.get_name() + "\" at " + rule.get_file_name() + " on " + node.displayname + " at " + str(node.extent.start.file))

def criterion_handler_suffix(node,rule,suffix):
    if(not node.displayname.endswith(suffix)):
        raise CriterionNotRespectedException("Rule: \"" + rule.get_name() + "\" at " + rule.get_file_name() + " on " + node.displayname + " at " + str(node.extent.start.file))
