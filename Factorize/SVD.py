from numpy import diag
from numpy import ndarray
from numpy.linalg import svd as svd_factorization
from pandas import DataFrame

from Get.TeamStats import TeamStats


class SVD(TeamStats):
    def __init__(self):
        super(SVD, self).__init__()
        self.__df_truncated = self.__factorize_svd(df=self.team_stats)

    @classmethod
    def __factorize_svd(cls, df: DataFrame) -> DataFrame:
        from Get.Variables import PRINCIPLE_COMPONENTS

        PRINCIPLE_COMPONENTS: int = PRINCIPLE_COMPONENTS
        team_names: list[str] = list(df.index.values)

        u, e, _ = svd_factorization(df.to_numpy(), full_matrices=True)

        truncated_u: ndarray = u[:, :PRINCIPLE_COMPONENTS]
        truncated_e: ndarray = diag(e)[:PRINCIPLE_COMPONENTS, :PRINCIPLE_COMPONENTS]

        df_truncated_teams_stats: DataFrame = DataFrame(truncated_u @ truncated_e)
        df_truncated_teams_stats.index = team_names

        return df_truncated_teams_stats

    @property
    def df_truncated_team_stats(self) -> DataFrame:
        return self.__df_truncated
