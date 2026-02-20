import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

plt.scatter(df["Sales"], df["Profit"])
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()