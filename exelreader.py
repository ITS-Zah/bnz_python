import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def ReadFromExel(path, sheatName):
    df = pd.read_excel(path, sheet_name=sheatName)
    return df

