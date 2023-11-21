import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import constantes_dash as cd
from dash import Dash, dcc, html, dash_table, callback, Input, Output

# dcc -----> Dash Core Components
# html -----> Dash Html Components

data = pd.read_csv(cd.PATH_ARCHIVO, index_col=0)


def tarjeta_filtros():
    control = dbc.Card([
        html.Div([
            dbc.Label("Gender:"),
            dcc.Dropdown(options=["All", "Male", "Female"], value="All")
        ]),
        html.Div([
            dbc.Label("Medal:"),
            dcc.Dropdown(options=["all", "gold", "silver", "bronze"],
                         value="all", id="ddMedal"),
        ]),
        html.Div([
            dbc.Label("Year:"),
            dbc.Input(type="number", min=1940, max=2023)
        ])
    ])
    return control


def dashboard():
    data_Pais = data.groupby("country", as_index=False).sum(numeric_only=True)
    g1 = px.line(data_Pais, x="country", y=["gold", "silver", "bronze"])
    body = html.Div([
        html.H2(cd.TITULO),
        html.P(cd.OBJETIVO),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div([
                        html.H3("Filtros"),
                        tarjeta_filtros()
                    ]), width=4
                ),
                dbc.Col(
                    html.Div([
                        dbc.Row(dcc.Graph(figure=g1, id="figMedal")),
                        dbc.Row(dash_table.DataTable(data=data.to_dict("records"),
                                                     page_size=10))
                    ]), width=8
                )
            ], align="center"
        ),
    ])
    return body


if __name__ == "__main__":
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dashboard()
    app.run(debug=True)
