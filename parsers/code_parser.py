import os
import platform

import clang.cindex
from clang.cindex import Index,LinkageKind

from clang.cindex import TypeKind

import clang.enumerations
from constants.criterion_keys import CriterionKeys

from constants.target_keys import TargetKeys
from utlis.console_utils import print_process

class CodeParser():
   
  def __init__(self,rules) -> None:
    self.__OS_PLATFORM = platform.system()

    if self.__OS_PLATFORM == "Windows":  
      clang.cindex.Config.set_library_file('C:/Program Files/LLVM/bin/libclang.dll')
    else:
      clang.cindex.Config.set_library_file('/usr/lib/llvm-6.0/lib/libclang.so.1')

    self.__rules = rules


  def __check_rule_compliance(self,node,rule):
      criterion = rule.get_criterion()

      if(criterion[CriterionKeys.HANDLER] is not None):
        criterion[CriterionKeys.HANDLER](node,criterion[CriterionKeys.VALUE_TO_CHECK])


  def __parse_node_recursively(self,node):
      
      if(node.linkage != LinkageKind.INVALID):
        #print(f'nome: {node.displayname} - - kind: {node.kind} tipo: {node.type.kind } -- acessibilidade: {node.access_specifier}')
        for rule in self.__rules:
          if(node.kind in rule.get_target()[TargetKeys.CLANG_KINDS]):
            if(node.linkage in rule.get_target()[TargetKeys.CLANG_LINKAGE_KIND]):
              if(rule.get_target()[TargetKeys.CLANG_ACCESS_KIND] is not None):
                if node.access_specifier in rule.get_target()[TargetKeys.CLANG_ACCESS_KIND]:
                  self.__check_rule_compliance(node,rule)
              else:
                self.__check_rule_compliance(node,rule)

      for c in node.get_children():
        self.__parse_node_recursively(c)


  def parse_code_file(self,file):
    print_process(f"Checking: {file}")
    index = Index.create()
    tu = index.parse(file)
    self.__parse_node_recursively(tu.cursor)