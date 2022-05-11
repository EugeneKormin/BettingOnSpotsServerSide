from os import getcwd
from pickle import dump


class SaveModel(object):
    def __init__(self, model: any, FILE_NAME: str):
        super(SaveModel, self).__init__()
        self.__save_model(FILE_NAME=FILE_NAME, model=model)

    @classmethod
    def __save_model(cls, FILE_NAME: str, model: any) -> None:
        with open(getcwd() + fr'\ML_algos\{FILE_NAME}.pickle', 'wb') as f:
            dump(model, f)
