from numpy import ndarray
from pandas import DataFrame
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

from Get.ProMatches import ProMatches


class SplittedData(ProMatches):
    def __init__(self):
        super(SplittedData, self).__init__()
        df_x, y = self.__split_X_y(df=self.current_matches_data)
        self.__X_train, self.__X_test, self.__y_train, self.__y_test = self.__split_train_test(df_x=df_x, y=y)

    @classmethod
    def __split_X_y(cls, df: DataFrame) -> tuple[DataFrame, list[float]]:
        y: list[float] = df["y"].values
        df.drop(columns=["y"], axis=1, inplace=True)

        x_scaled: ndarray = MinMaxScaler().fit_transform(df.to_numpy())
        df_x: DataFrame = DataFrame(x_scaled)

        return df_x, y

    @classmethod
    def __split_train_test(cls, df_x: DataFrame, y: list[float]) -> tuple[DataFrame, DataFrame, DataFrame, DataFrame]:
        X_train, X_test, y_train, y_test = train_test_split(
            df_x, y, test_size=0.10, random_state=42, shuffle=True
        )
        return X_train, X_test, y_train, y_test

    @property
    def _X_train(self) -> DataFrame:
        return self.__X_train

    @property
    def _X_test(self) -> DataFrame:
        return self.__X_test

    @property
    def _y_train(self):
        return self.__y_train

    @property
    def _y_test(self):
        return self.__y_test
