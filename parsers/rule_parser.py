import json
from enums.criterion_enum import CriterionEnum
from enums.target_enum import TargetEnum
from exceptions.invalid_criterion_exception import InvalidCriterionException
from exceptions.invalid_target_exception import InvalidTargetException
from exceptions.rule_missing_criterion_exception import RuleMissingCriterionException

from exceptions.rule_missing_target_exception import RuleMissingTargetException
from models.rule_model import RuleModel


class RuleParser():

    @staticmethod
    def parse_file(path:str):
        with open(path, 'r') as raw_data:
            j_rule = json.load(raw_data)

            target = None
            criterion = None

            if(j_rule["target"] is None):
                raise RuleMissingTargetException()
            
            if(j_rule["criterion"] is None):
                raise RuleMissingCriterionException()
            
            target = TargetEnum(j_rule["target"])

            if(target is None):
                raise InvalidTargetException()
            
            
            criterion = CriterionEnum(j_rule["criterion"])

            if(criterion is None):
                raise InvalidCriterionException()
            
        
            ret_rule = RuleModel(target,criterion)

            return ret_rule
            


