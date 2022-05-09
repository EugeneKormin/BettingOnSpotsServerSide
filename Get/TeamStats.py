from pandas import DataFrame, concat
from sportsreference.nhl.teams import Teams


class TeamStats(object):
    def __init__(self):
        self.__get_team_data_stats()

    @classmethod
    def __get_team_data_stats(cls) -> DataFrame:
        df_team_stats: DataFrame = DataFrame({})

        for team in Teams(2022):
            df_team_stats: DataFrame = concat([df_team_stats, team.dataframe])

        df_team_stats.index = df_team_stats["name"]

        df_team_stats.drop(columns=[
            "abbreviation", "total_goals_per_game", "name", "pdo_at_even_strength", "goals_against"
        ], inplace=True)

        return df_team_stats

    @property
    def team_stats(self) -> DataFrame:
        return self.__get_team_data_stats()
