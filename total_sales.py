import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

total_sales = df["Sales"].sum()

print(f"Total sales {total_sales}")