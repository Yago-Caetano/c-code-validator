
from enums.criterion_enum import CriterionEnum
from enums.target_enum import TargetEnum


class RuleModel:

    def __init__(self,target: TargetEnum, criterion: CriterionEnum) -> None:
        self.__target = TargetEnum.TARGET_NONE
        self.__criterion = CriterionEnum.NONE

    def get_criterion(self) -> CriterionEnum:
        return self.__criterion
    
    def get_target(self) -> TargetEnum:
        return self.__target

    def check():
        pass

    def on_success():
        pass

    def on_failure():
        pass