# ISM2411 Lab 13 - First DataFrame: Retail Sales Explorer
#
# Daniel Souza
#
# Self Assessment:
#
# 1. What does a boolean filter do?
# A boolean filter filters on a true/ false question across all rows
# eg. is the region South? The filter selects all rows for which the response is true. This is #similar to the excel filter function but is coded so it can be applied to any data.
#
# 2. df["revenue"] vs. df[["revenue"]]
#df["revenue"] (single brackets) returns a Series, which is one column of values. df[["revenue"]] #(double brackets) returns a DataFrame with one column,because the inner brackets are a list #of column names. It matters when a later step needs a DataFrame versus a Series (like taking #a mean or sorting by that column).
#
#3. Why pandas instead of excel?
# Repeatability and scalability of analysis using pandas. A small number of lines can be re-run #on new data or even on millions of rows which would either fail or be very slow in excel. Also #because the analysis is coded it is clear what has been performed and there are no manual #operations that may be unclear.

import pandas as pd

print("=== Exercise 1: Load it ===")
df = pd.read_csv("data/retail_sales.csv")
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.dtypes)

print("\n=== Exercise 2: Filter by region ===")
south = df[df["region"] == "South"]
print("South rows:", len(south))
print(south.head())

print("\n=== Exercise 3: Top 5 by revenue ===")
top5 = df.sort_values("revenue", ascending=False).head(5)
print(top5)
# The index values are not 0-4 because the original row labels stay attached
# after sorting. reset_index(drop=True) would renumber them.

print("\n=== Exercise 4: Two-condition filter ===")
big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]
print("South AND revenue > 1000 rows:", len(big_south))
print(big_south.head())

print("\n=== Exercise 5: A new column ===")
df["per_unit"] = df["revenue"] / df["quantity"]
print(df.head())
print("Mean per-unit price:", df["per_unit"].mean())

print("\n=== Exercise 6: Unique values ===")
print(df["region"].unique())
print(df["region"].value_counts(dropna=False))

print("\n=== Exercise 7: Select columns ===")
subset = df[["region", "product", "revenue"]]
print("Subset shape:", subset.shape)

print("\n=== Exercise 8: Save ===")
df.to_csv("data/explored.csv", index=False)
check = pd.read_csv("data/explored.csv")
print("Saved data/explored.csv with shape:", check.shape)
print("Header row:", check.columns.tolist())
