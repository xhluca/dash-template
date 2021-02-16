import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px


def Header(name, app):
    title = html.H1(name)
    logo = html.Img(
        src=app.get_asset_url("dash-logo.png"), style={"float": "right", "height": 60}
    )
    link = html.A(logo, href="https://plotly.com/dash/")

    return dbc.Row([dbc.Col(title, md=8), dbc.Col(link, md=4)], align="center")


df = px.data.tips()
days = df.day.unique()


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # gunicorn needs this for deployment

controls = [
    dbc.Select(
        id="dropdown",
        options=[{"label": x, "value": x} for x in days],
        value=days[0],
    )
]

app.layout = dbc.Container(
    [
        Header("{{cookiecutter.app_name}}", app),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card([dbc.CardHeader("Controls"), dbc.CardBody(controls)]), md=4
                ),
                dbc.Col(dcc.Graph(id="bar-chart"), md=8),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(Output("bar-chart", "figure"), [Input("dropdown", "value")])
def update_bar_chart(day):
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill", color="smoker", barmode="group")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)