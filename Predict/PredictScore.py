from pandas import DataFrame

from Factorize.SVD import SVD
from Get.Model import Model
from Get.ProMatches import ProMatches


class PredictScore(Model, SVD):
    def __init__(self, TEAM_A, TEAM_B):
        super(PredictScore, self).__init__()
        self.__result = self.__predict(model=self.model, TEAM_A=TEAM_A, TEAM_B=TEAM_B)

    @classmethod
    def __evaluate_advance(cls, ADVANCE: float):
        FULL_ADVANCE: int = int(ADVANCE)
        PARTIAL_ADVANCE: float = abs(ADVANCE - FULL_ADVANCE)
        if 0.25 > PARTIAL_ADVANCE:
            PARTIAL_ADVANCE = 0
        elif 0.25 <= PARTIAL_ADVANCE < 0.75:
            if FULL_ADVANCE > 0:
                PARTIAL_ADVANCE = 0.5
            else:
                PARTIAL_ADVANCE = -0.5
        elif PARTIAL_ADVANCE > 0.75:
            if FULL_ADVANCE > 0:
                PARTIAL_ADVANCE = 1
            else:
                PARTIAL_ADVANCE = -1
        return FULL_ADVANCE + PARTIAL_ADVANCE

    @classmethod
    def __make_predictions(cls, model: any, df_result_to_pred: DataFrame) -> float:
        return model.predict(df_result_to_pred)

    @classmethod
    def __predict(cls, model: any, TEAM_A: str, TEAM_B: str) -> str:
        df_result_to_pred: DataFrame = ProMatches().data_to_pred(TEAM_A=TEAM_A, TEAM_B=TEAM_B)
        PREDICTED_SCORE: float = PredictScore.__make_predictions(model=model, df_result_to_pred=df_result_to_pred)
        ROUNDED_PRIDICTED_SCORE: float = PredictScore.__evaluate_advance(ADVANCE=PREDICTED_SCORE)
        if ROUNDED_PRIDICTED_SCORE < 0:
            result: str = f"фора: +{round(float(-ROUNDED_PRIDICTED_SCORE), 2)} на {TEAM_A}"
        else:
            result: str = f"фора: +{round(float(ROUNDED_PRIDICTED_SCORE), 2)} на {TEAM_B}"

        return result

    @property
    def predict(self):
        return self.__result
