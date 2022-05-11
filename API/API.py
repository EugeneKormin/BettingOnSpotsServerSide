from Predict.PredictScore import PredictScore
from Train.TrainModel import TrainModel


class API(object):
    def __init__(self, request):
        self.__request = request

    @classmethod
    def __get_args_for_prediction(cls, request) -> tuple[str, str]:
        TEAM_A: str = request.args["team_A"].replace('_', ' ')
        TEAM_B: str = request.args["team_B"].replace('_', ' ')
        return TEAM_A, TEAM_B

    @classmethod
    def __predict_score(cls, request) -> str:
        TrainModel()
        parsed_args: tuple[str, str] = API.__get_args_for_prediction(request=request)
        PREDICTED_SCORE: str = str(round(float(PredictScore(*parsed_args).predict), 2))
        return PREDICTED_SCORE

    @classmethod
    def __get_args_for_calculation(cls, request) -> float:
        PREDICTED_SCORE: float = float(request.args["predicted_score"].replace('_', ' '))
        return PREDICTED_SCORE

    @classmethod
    def __calculate_advance(cls, request) -> str:
        PREDICTED_SCORE: float = API.__get_args_for_calculation(request=request)
        if PREDICTED_SCORE > 0:
            return str(PREDICTED_SCORE - 0.5)
        elif PREDICTED_SCORE < 0:
            return str(PREDICTED_SCORE + 0.5)

    @property
    def calculated_advance(self):
        PARSED_ARG: str = self.__calculate_advance(request=self.__request)
        return PARSED_ARG

    @property
    def predicted_score(self) -> str:
        return self.__predict_score(request=self.__request)

