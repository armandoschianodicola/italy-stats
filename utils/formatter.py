from abc import ABC, abstractmethod


class Formatter(ABC):

    def __init__(self, df):
        self.df = df

    @abstractmethod
    def format(self, col):
        pass
