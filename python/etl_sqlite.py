import sqlite3
import pandas as pd

con = sqlite3.connect("../data/wafer/db.s3db")

df = pd.read_csv("../data/wafer/LSWMD.csv", index_col="id")
df.to_sql(name="wafer", con=con)

