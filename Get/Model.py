from pickle import load


class Model(object):
    def __init__(self):
        self.__model: any = self.__load_model()

    @classmethod
    def __load_model(cls) -> any:
        with open("ML_algos/model.pickle", "rb") as f:
            model: any = load(f)
        return model

    @property
    def model(self) -> any:
        return self.__model
