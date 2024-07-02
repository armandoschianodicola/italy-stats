from utils.formatter import Formatter


class HeaderFormatter(Formatter):

    def __init__(self, df):
        super().__init__(df)

    def format(self):
        self.df.columns = self.df.columns.str.strip()
        self.df.columns = self.df.columns.str.lower()
        self.df.columns = self.df.columns.str.replace(" ", "_")
