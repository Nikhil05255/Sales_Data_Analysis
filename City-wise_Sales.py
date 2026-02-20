import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

city_wise_sales = df.groupby("City")["Sales"].sum()
# print(city_wise_sales) #print city-wise sales

city_wise_sales.plot(kind = "bar")
plt.title("City-wise Total Sales")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.show()