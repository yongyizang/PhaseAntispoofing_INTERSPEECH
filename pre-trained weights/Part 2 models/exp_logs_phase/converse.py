import os, sys, pandas as pd

csvFileDir = "middle.csv"

# reverse row and column.

csv_a = pd.read_csv(csvFileDir).T.to_csv("converted.csv", header=False, index=False)

# save.