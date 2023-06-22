from enum import Enum

from clang.cindex import CursorKind,LinkageKind,AccessSpecifier
from constants.rules_reserved_keys import RulesReservedKeys

from constants.target_keys import TargetKeys

class TargetEnum(Enum):
    TARGET_NONE = {TargetKeys.VALUE_IN_RULE: RulesReservedKeys.TARGET_TYPE_NONE,TargetKeys.CLANG_KINDS:[],TargetKeys.CLANG_LINKAGE_KIND:None,TargetKeys.CLANG_ACCESS_KIND:None}
    TARGET_FUNCTION = {TargetKeys.VALUE_IN_RULE: RulesReservedKeys.TARGET_TYPE_METHODS, TargetKeys.CLANG_KINDS:[CursorKind.FUNCTION_DECL,CursorKind.FUNCTION_TEMPLATE],TargetKeys.CLANG_LINKAGE_KIND:[LinkageKind.INTERNAL],TargetKeys.CLANG_ACCESS_KIND:None}
    TARGET_GLOBAL_VARIABLE = {TargetKeys.VALUE_IN_RULE:RulesReservedKeys.TARGET_TYPE_GLOBALS, TargetKeys.CLANG_KINDS:[CursorKind.VAR_DECL], TargetKeys.CLANG_LINKAGE_KIND:[LinkageKind.INTERNAL], TargetKeys.CLANG_ACCESS_KIND:[AccessSpecifier.PUBLIC]}
    TARGET_LOCAL_VARIABLE = {TargetKeys.VALUE_IN_RULE: RulesReservedKeys.TARGET_TYPE_VARIABLES,TargetKeys.CLANG_KINDS:[CursorKind.VAR_DECL], TargetKeys.CLANG_LINKAGE_KIND:[LinkageKind.INTERNAL],TargetKeys.CLANG_ACCESS_KIND:None}
    TARGET_DEFINE = {TargetKeys.VALUE_IN_RULE:RulesReservedKeys.TARGET_TYPE_DEFINES,TargetKeys.CLANG_KINDS:[CursorKind.MACRO_DEFINITION,CursorKind.MACRO_INSTANTIATION], TargetKeys.CLANG_LINKAGE_KIND:None,TargetKeys.CLANG_ACCESS_KIND:None}