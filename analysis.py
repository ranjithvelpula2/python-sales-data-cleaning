import pandas as pd

df = pd.read_csv("sales.csv")
print(df.head())
print(df.info())

df = df.drop_duplicates()
df["region"] = df["region"].str.title()
df["quantity"] = df["quantity"].fillna(df["quantity"].median())

df["revenue"] = df["quantity"] * df["unit_price"]

print(df.groupby("product")["revenue"].sum())
print(df.groupby("region")["revenue"].sum().sort_values(ascending=False))
print("Total revenue:", df["revenue"].sum())

df.to_csv("sales_clean.csv", index=False)
