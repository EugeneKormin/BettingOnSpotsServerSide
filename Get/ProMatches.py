from sklearn.preprocessing import MinMaxScaler
from pandas import DataFrame
from pandas import concat
from pandas import Series
from sportsreference.nhl.teams import Teams
from datetime import datetime, timedelta
from numpy import hstack
from numpy import ndarray

from Factorize.SVD import SVD
from Get.Variables import variables
from Get.Variables import OFFSET
from Save.SaveModel import SaveModel
from Get.Scaler import Scaler


min_max_scaler: MinMaxScaler = MinMaxScaler()


class ProMatches(SVD, SaveModel):
    def __init__(self):
        super(ProMatches, self).__init__()

    @classmethod
    def __scale_df(cls, df: DataFrame, train: bool, min_max_scaler: MinMaxScaler) -> DataFrame:
        if train:
            y: Series = df["y"].values
            df: ndarray = df.drop(columns=["y"]).to_numpy()
            min_max_scaler.fit(df)
            df_scaled: DataFrame = DataFrame(min_max_scaler.transform(df))
            df_scaled["y"]: DataFrame = y
        else:
            df_scaled: DataFrame = DataFrame(min_max_scaler.transform(df))
        return df_scaled

    @classmethod
    def __process_data_to_pred(cls, TEAM_A: str, TEAM_B: str) -> DataFrame:
        df_truncated_teams_stats = SVD().df_truncated_team_stats
        df_result_to_pred: DataFrame = DataFrame(hstack([
            df_truncated_teams_stats.loc[TEAM_A].T,
            df_truncated_teams_stats.loc[TEAM_B].T
        ])).T
        return df_result_to_pred

    @classmethod
    def __get_pro_matches(cls, df_truncated_teams_stats: DataFrame) -> DataFrame:
        def check_data() -> bool:
            match_date: datetime = datetime.fromisoformat(game.date)
            nowadays: datetime = datetime.now()
            offset: datetime = nowadays - timedelta(days=variables.offset)
            return True if offset < match_date < (nowadays - timedelta(days=4)) else False

        result_df: DataFrame = DataFrame({})

        for team in Teams(2022):
            TEAM_NAME: str = team.name
            for game in team.schedule:
                OPPONENT_NAME: str = game.opponent_name
                if check_data():
                    current_result_df: DataFrame = DataFrame(hstack([
                        df_truncated_teams_stats.loc[TEAM_NAME].T,
                        df_truncated_teams_stats.loc[OPPONENT_NAME].T
                    ])).T

                    current_result_df["y"]: int = game.goals_scored - game.goals_allowed
                    result_df: DataFrame = concat([result_df, current_result_df])
        return result_df

    @property
    def current_matches_data(self) -> DataFrame:
        df: DataFrame = self.__get_pro_matches(df_truncated_teams_stats=self.df_truncated_team_stats)
        df_normalized: DataFrame = self.__scale_df(df=df, train=True, min_max_scaler=min_max_scaler)
        SaveModel(FILE_NAME="scaler", model=min_max_scaler)
        return df_normalized

    def data_to_pred(self, TEAM_A: str, TEAM_B: str) -> DataFrame:
        df: DataFrame = self.__process_data_to_pred(TEAM_A=TEAM_A, TEAM_B=TEAM_B)
        min_max_scaler = Scaler().scaler
        df_normalized: DataFrame = self.__scale_df(df=df, train=False, min_max_scaler=min_max_scaler)
        return df_normalized
