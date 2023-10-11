import pandas as pd
path = 'FakeNameGenerator.csv'
class Dificuldade:
    def read_csv(path):
        return pd.read_csv(path)
        
    def remove_null_values(df):
        return df.dropna()

    def remove_columns(df, columns):
        return df.drop(columns, axis=1)


