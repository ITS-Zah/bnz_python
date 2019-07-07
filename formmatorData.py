import pandas as pd
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("C:\\MetaDoc\\results_avg.csv")
columnsTitles=["Name","FR","TR","EN"]
df = data.sample(frac=1)
columnsTitles=["FR","TR","EN"]
df=df.reindex(columns=columnsTitles)
# Preview the first 5 lines of the loaded data
splitter = (int)(len(df)*0.7)
df_new1, df_new2 = df[:splitter], df[splitter:]
print(len(df_new1))
print(len(df_new2))
df_new1.to_excel("train.xlsx",sheet_name='FirstList')  # doctest: +SKIP
df_new2.to_excel("test.xlsx",sheet_name='FirstList')  # doctest: +SKIP
import csv
spamReader = csv.reader(open("C:\\MetaDoc\\results_avg.csv", newline=''), delimiter=' ', quotechar='|')

