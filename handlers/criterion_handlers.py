
from exceptions.criterion_not_respected_exception import  CriterionNotRespectedException


def criterion_handler_lenght_less_than(node,length):
    if(len(node.displayname) > length):
        raise CriterionNotRespectedException(node.displayname + " at " + str(node.extent.start.file))
    

def criterion_handler_lenght_bigger_than(node,length):
    if(len(node.displayname) < length):
        raise CriterionNotRespectedException(node.displayname + " at " + str(node.extent.start.file))
    
def criterion_handler_prefix(node,prefix):
    if(not node.displayname.startswith(prefix)):
        raise CriterionNotRespectedException(node.displayname + " at " + str(node.extent.start.file))

def criterion_handler_suffix(node,suffix):
    if(not node.displayname.endswith(suffix)):
        raise CriterionNotRespectedException(node.displayname + " at " + str(node.extent.start.file))