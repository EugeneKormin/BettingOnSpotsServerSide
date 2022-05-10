from Predict.PredictScore import PredictScore
from Train.TrainModel import TrainModel


class API(object):
    def __init__(self, request):
        self.__request = request

    @classmethod
    def __parse_args_for_prediction(cls, request) -> tuple[str, str]:
        TEAM_A: str = request.args["team_A"].replace('_', ' ')
        TEAM_B: str = request.args["team_B"].replace('_', ' ')
        return TEAM_A, TEAM_B

    @classmethod
    def __parse_args_for_calculation(cls, request) -> str:
        PREDICTED_SCORE: float = float(request.args["predicted_score"].replace('_', ' '))
        if PREDICTED_SCORE > 0:
            return str(PREDICTED_SCORE - 0.5)
        elif PREDICTED_SCORE < 0:
            return str(PREDICTED_SCORE + 0.5)

    @property
    def predict_score(self) -> str:
        TrainModel()
        parsed_args: tuple[str, str] = self.__parse_args_for_prediction(request=self.__request)
        PREDICTED_SCORE: str = str(round(float(PredictScore(*parsed_args).predict), 2))
        return PREDICTED_SCORE

    @property
    def calculate_advance(self):
        PARSED_ARG: str = self.__parse_args_for_calculation(request=self.__request)
        return PARSED_ARG
