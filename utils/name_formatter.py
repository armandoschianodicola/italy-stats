from utils.formatter import Formatter


class NameFormatter(Formatter):

    def __init__(self, df):
        super().__init__(df)

    def format(self, col):
        self.df[col] = self.df[col].str.strip()
        self.df[col] = self.df[col].str.lower()
