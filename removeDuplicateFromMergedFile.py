import imp
import pandas as pd
# path = "/Users/tony/Downloads/amsterdam.csv"
# data = pd.read_csv(path)
# #drop duplicates based on the colum URL
# data_v1 = data.drop_duplicates(subset=['URL'])
# data_v1.to_csv("/Users/tony/Downloads/amsterdam_v1.csv", index=False)

df = pd.read_csv("amsterdamMerged.csv")
# dv = df.to_csv(header=["CONSTRUCTION YEAR", "COUNT"])
# csv_data = df.to_csv(columns=["CONSTRUCTION YEAR", "COUNT"])
# df.sort_values(['CONSTRUCTION YEAR'])
dv=df["CONSTRUCTION YEAR"].value_counts()
print(dv)
dv.to_csv("amsterdamMerged_v1.csv")
# dv.to_csv("amsterdamVal.csv", index=False)
# print(df[["CONSTRUCTION YEAR"],df["CONSTRUCTION YEAR"].value_counts()])
import pandas as pd
df = pd.read_csv("amsterdamMerged.csv")
dv=df["CONSTRUCTION YEAR"].value_counts()
print(dv)
dv.to_csv("amsterdamMerged_v1.csv")
