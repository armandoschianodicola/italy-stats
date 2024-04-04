from utils.formatter import Formatter


class RegionFormatter(Formatter):

    def __init__(self, df):
        super().__init__(df)

    def format(self, col):
        self.df[col] = self.df[col].str.strip()
        self.df.loc[self.df[col] == 'PROV. AUTON. BOLZANO', col] = 'trentino-alto adige'
        self.df.loc[self.df[col] == 'PROV. AUTON. TRENTO', col] = 'trentino-alto adige'
        self.df[col] = self.df[col].str.lower()
        self.df[col] = self.df[col].map(lambda x: x.replace("-", " "))
        self.df[col] = self.df[col].map(lambda x: x.replace("`", "'"))
