import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

category_profit = df.groupby("Category")["Profit"].sum()
# print(Most_Profitable_Category) #print sum of categrory

most_profitable = category_profit.sort_values(ascending=False)
# print(most_profitable) #print most profitable category

print("Most Profitable Category: ",most_profitable.index[0])