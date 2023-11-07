import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("datasets/weekly_stocks.csv",
                   parse_dates=True, index_col="Date")
#print(data.sample(5))

#data.plot(y="MSFT", figsize=(9, 6))
#data.plot.line(y="MSFT", title="Microsoft Stocks",
 #              ylabel="USD", xlabel="Week", color="lightgreen")

#data.plot(kind="box", vert=False)

#data.plot(kind="area")
#data.plot(kind="area", stacked=False)

data_3Months = data.resample(rule="M").mean()[-3:]
#data_3Months.plot(kind="bar",stacked=True, ylabel="Price")
#data_3Months.plot(kind="barh", ylabel="Price")

#data.plot(kind="hist", alpha=0.6, bins=25)

#data2 = data.reset_index()
#print(data2.sample(5))
#data2.plot(kind="scatter", x="Date", y="MSFT")

print(data_3Months)
#data_3Months.plot(kind="pie", subplots=True, legend=False,
 #                 figsize=(14, 7), autopct="%.f")

data_3Months.MSFT.plot(kind="pie", figsize=(14, 7),
                       autopct="%.f")
plt.show()