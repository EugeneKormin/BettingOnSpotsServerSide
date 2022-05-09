from pickle import load


class Scaler(object):
    def __init__(self):
        self.__scaler: any = self.__load_scaler()

    @classmethod
    def __load_scaler(cls) -> any:
        with open("ML_algos/scaler.pickle", "rb") as f:
            model: any = load(f)
        return model

    @property
    def scaler(self) -> any:
        return self.__scaler