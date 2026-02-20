import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

product_sales = df.groupby("Product")["Sales"].sum()

# print(product_sales) # all product sales total sales

top5 = product_sales.sort_values(ascending=False).head(5)
# print(top5) #print top 5 product

top5.plot(kind = "bar")
plt.show()