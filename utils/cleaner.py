class Cleaner:

    def __init__(self, df):
        self.df = df

    def clean_regions(self, col):
        self.df[col] = self.df[col].str.strip()
        self.df.loc[self.df[col] == 'PROV. AUTON. BOLZANO', col] = 'trentino-alto adige'
        self.df.loc[self.df[col] == 'PROV. AUTON. TRENTO', col] = 'trentino-alto adige'
        self.df[col] = self.df[col].str.lower()
        self.df[col] = self.df[col].map(lambda x: x.replace("-", " "))
        self.df[col] = self.df[col].map(lambda x: x.replace("`", "'"))
