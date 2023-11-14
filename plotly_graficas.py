import pandas as pd
import plotly.express as px

data = pd.read_csv("datasets/weekly_stocks.csv",parse_dates=True)
#print(data.head())
fig = px.line(data, x="Date", y=["MSFT", "FB"], title="Microsoft Stocks")

fig_box = px.box(data, y=["MSFT", "AAPL"], title="Grafica de Caja y Bigotes")

fig_area = px.area(data, x="Date", y=["AAPL","MSFT", "FB"], title="Grafica de Area")

data["Date"] = pd.to_datetime(data["Date"])
data2 = data.set_index("Date")
data_3Months = data2.resample(rule="M").mean()[-3:]
data_3Months = data_3Months.reset_index()
#print(data_3Months)

columnas = ["MSFT", "FB", "AAPL"]
fig_bar = px.bar(data_3Months, x="Date", y=columnas)
fig_bar.update_layout(xaxis_title="Mes", yaxis_title="Dolar($)",
                      title="Stocks Mensuales")

nbins = int(len(data)**(1/2))
#print(nbins)
fig_hist = px.histogram(data, x="Date", y="MSFT", nbins=nbins)

fig_scatter = px.scatter(data, x="Date", y="MSFT",
                         size="MSFT", color="Date")

df_iris = px.data.iris()
fig_iris = px.scatter(df_iris, x="species", y="petal_width",
                      size="petal_length", color="species")
#print(df_iris.sample(5))

df_tips = px.data.tips()
#print(df_tips.sample(5))
fig_pie = px.pie(df_tips, values="total_bill", names="day")
fig_pie.show()

#fig_iris.show()


#fig_scatter.show()

#fig_hist.show()

#fig_bar.show()

#fig_area.show()
#fig_box.show()
#fig.show()