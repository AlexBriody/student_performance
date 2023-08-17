from cleaning_data import clean_data
import pandas as pd

class Base:
    def __init__(self):
        self.df = None
        
    def clean_and_process_data(self, filepath):
        df = pd.read_csv(filepath, sep=';')
        self.df = clean_data(df)
