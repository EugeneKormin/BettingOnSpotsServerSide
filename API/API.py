from Predict.PredictScore import PredictScore


class API(object):
    def __init__(self, request):
        parsed_args = self.__parse_args(request)
        self.__prediction: str = self.__predict(parsed_args)

    @classmethod
    def __parse_args(cls, request):
        TEAM_A: str = request.args["team_A"].replace('_', ' ')
        TEAM_B: str = request.args["team_B"].replace('_', ' ')
        return TEAM_A, TEAM_B

    @classmethod
    def __predict(cls, parsed_args) -> str:
        return PredictScore(*parsed_args).predict

    @property
    def predict(self):
        return self.__prediction
