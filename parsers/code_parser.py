import os
import platform

import clang.cindex
from clang.cindex import Index,LinkageKind,CursorKind

from clang.cindex import TypeKind

import clang.enumerations
from constants.criterion_keys import CriterionKeys

from constants.target_keys import TargetKeys
from utlis.console_utils import print_process

class CodeParser():
   
  def __init__(self,rules) -> None:
    self.__OS_PLATFORM = platform.system()
    clang.cindex.Config.set_library_path(os.getenv("LIBCLANG_LIBRARY_PATH"))
    
    self.__rules = rules


  def __check_rule_compliance(self,node,rule):
      criterion = rule.get_criterion()

      if(criterion[CriterionKeys.HANDLER] is not None):
        criterion[CriterionKeys.HANDLER](node,rule,criterion[CriterionKeys.VALUE_TO_CHECK])

  def __is_this_node_able_be_checked(self,node):
    if((node.kind == CursorKind.MACRO_DEFINITION) or (node.kind == CursorKind.MACRO_INSTANTIATION)):
      #only accept local macro definitions
      if(node.location.file != None):
        return True
      else:
        return False
    else:
      if(node.linkage != LinkageKind.INVALID):
        return True
      else:
        return False


  def __parse_node_recursively(self,node):
      
      if(self.__is_this_node_able_be_checked(node)):
        #print(f'nome: {node.displayname} - - kind: {node.kind} tipo: {node.type.kind } -- acessibilidade: {node.access_specifier}')
        for rule in self.__rules:
          for rule_target in rule.get_target():
            if(node.kind in rule_target[TargetKeys.CLANG_KINDS]):

              if(rule_target[TargetKeys.CLANG_LINKAGE_KIND] != None):

                if(node.linkage in rule_target[TargetKeys.CLANG_LINKAGE_KIND]):

                  if(rule_target[TargetKeys.CLANG_PARENT_KIND] is not None):

                    if node.lexical_parent.kind in rule_target[TargetKeys.CLANG_PARENT_KIND]:
                      self.__check_rule_compliance(node,rule)

                  else:

                    self.__check_rule_compliance(node,rule)

              else:
                self.__check_rule_compliance(node,rule)

      
      for c in node.get_children():
        self.__parse_node_recursively(c)


  def parse_code_file(self,file):
    index = Index.create()
    tu = index.parse(file,options=clang.cindex.TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD)
    self.__parse_node_recursively(tu.cursor)