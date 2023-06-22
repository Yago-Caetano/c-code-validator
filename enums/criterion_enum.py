from enum import Enum
from constants.criterion_keys import CriterionKeys
from constants.rules_reserved_keys import RulesReservedKeys

from handlers.criterion_handlers import criterion_handler_lenght_bigger_than, criterion_handler_lenght_less_than, criterion_handler_prefix, criterion_handler_regex, criterion_handler_suffix

class CriterionEnum(Enum):
    NONE = {CriterionKeys.VALUE_IN_RULE: RulesReservedKeys.NONE ,CriterionKeys.REQUIRE_VALUE:False, CriterionKeys.VALUE_TO_CHECK:None,CriterionKeys.HANDLER:None}
    LENGTH_LESS_THAN = {CriterionKeys.VALUE_IN_RULE: RulesReservedKeys.LENGTH_LESS_THAN, CriterionKeys.REQUIRE_VALUE:True, CriterionKeys.VALUE_TO_CHECK:None, CriterionKeys.HANDLER:criterion_handler_lenght_less_than}
    LENGTH_BIGGER_THAN = {CriterionKeys.VALUE_IN_RULE: RulesReservedKeys.LENGTH_BIGGER_THAN, CriterionKeys.REQUIRE_VALUE:True ,CriterionKeys.VALUE_TO_CHECK:None, CriterionKeys.HANDLER:criterion_handler_lenght_bigger_than}
    PREFIX = {CriterionKeys.VALUE_IN_RULE: RulesReservedKeys.PREFIX, CriterionKeys.REQUIRE_VALUE:True, CriterionKeys.VALUE_TO_CHECK: None, CriterionKeys.HANDLER:criterion_handler_prefix}
    SUFFIX = {CriterionKeys.VALUE_IN_RULE: RulesReservedKeys.SUFFIX, CriterionKeys.REQUIRE_VALUE:True, CriterionKeys.VALUE_TO_CHECK: None, CriterionKeys.HANDLER:criterion_handler_suffix}
    REGEX = {CriterionKeys.VALUE_IN_RULE: RulesReservedKeys.REGEX, CriterionKeys.REQUIRE_VALUE:True, CriterionKeys.VALUE_TO_CHECK: None, CriterionKeys.HANDLER:criterion_handler_regex}