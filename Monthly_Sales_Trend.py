import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

# print(df["Date"].dtype) # datatype check

df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

monthly_sales.plot(marker="o")
plt.xlabel("Month")
plt.ylabel("Total sales")
plt.xticks(rotation=45)
plt.show()