from pandas import DataFrame
import xgboost as xgb

from Get.SplittedData import SplittedData
from Save.SaveModel import SaveModel


class TrainModel(SplittedData, SaveModel):
    def __init__(self):
        super(TrainModel, self).__init__()
        X_train, X_test, y_train, y_test = self._X_train, self._X_test, self._y_train, self._y_test
        self.__model: any = self.__train_model(X_train=X_train, y_train=y_train)
        self.__save_model(FILE_NAME="model", model=self.__model)

    @classmethod
    def __train_model(cls, X_train: DataFrame, y_train: DataFrame) -> any:
        xgb_reg = xgb.XGBRegressor(max_depth=3, n_estimators=100, n_jobs=2,
                                   objective='reg:squarederror', booster='gbtree',
                                   random_state=42, learning_rate=0.05)

        xgb_reg.fit(X_train, y_train)
        return xgb_reg

    @classmethod
    def __save_model(cls, FILE_NAME: str, model: any) -> None:
        SaveModel(model=model, FILE_NAME=FILE_NAME)
