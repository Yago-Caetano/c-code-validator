class CriterionNotRespectedException(Exception):
    def __init__(self,msg):
        self.message = f'Criterion not respected on :{msg}'

    def __str__(self):
        return self.message 