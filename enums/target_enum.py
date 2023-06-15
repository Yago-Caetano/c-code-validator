from enum import Enum

class TargetEnum(Enum):
    TARGET_NONE = "none"
    TARGET_FUNCTION = "methods"
    TARGET_GLOBAL_VARIABLE = "globals"
    TARGET_LOCAL_VARIABLE = "variables"
    TARGET_DEFINE = "defines"