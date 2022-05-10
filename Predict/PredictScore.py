from pandas import DataFrame
from numpy import ndarray
from Factorize.SVD import SVD
from Get.Model import Model
from Get.ProMatches import ProMatches


class PredictScore(Model, SVD):
    def __init__(self, TEAM_A, TEAM_B):
        super(PredictScore, self).__init__()
        self.__PREDICTED_SCORE: str = self.__predict(model=self.model, TEAM_A=TEAM_A, TEAM_B=TEAM_B)

    @classmethod
    def __make_predictions(cls, model: any, df_result_to_pred: DataFrame) -> ndarray:
        return model.predict(df_result_to_pred)

    @classmethod
    def __predict(cls, model: any, TEAM_A: str, TEAM_B: str) -> str:
        df_result_to_pred: DataFrame = ProMatches().data_to_pred(TEAM_A=TEAM_A, TEAM_B=TEAM_B)
        PREDICTED_SCORE: ndarray = PredictScore.__make_predictions(model=model, df_result_to_pred=df_result_to_pred)
        return str(PREDICTED_SCORE.tolist()[0])

    @property
    def predict(self):
        return self.__PREDICTED_SCORE
