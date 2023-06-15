from enum import Enum

class CriterionEnum(Enum):
    NONE = "none"
    LENGTH_LESS_THAN = "length_less_than"
    LENGTH_BIGGER_THAN = "length_bigger_than"
    PREFIX = "prefix"
    SUFFIX = "suffix"