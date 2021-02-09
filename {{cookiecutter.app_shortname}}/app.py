import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px


def Col(*args, md=None, **kwargs):
    if md is None:
        class_name = f"col"
    else:
        class_name = f"col-12 col-md-{md}"

    return html.Div(*args, className=class_name, **kwargs)


def Row(*args, **kwargs):
    return html.Div(*args, className="row", **kwargs)


def Header(name, app):
    title = html.H1(name)
    logo = html.Img(
        src=app.get_asset_url("dash-logo.png"), style={"float": "right", "height": 60}
    )
    link = html.A(logo, href="https://plotly.com/dash/")

    return Row([Col(title, md=8), Col(link, md=4)])


df = px.data.tips()
days = df.day.unique()

bootstrap_css = (
    "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
)
app = dash.Dash(__name__, external_stylesheets=[bootstrap_css])
server = app.server  # gunicorn needs this for deployment

controls = [
    dcc.Dropdown(
        id="dropdown", options=[{"label": x, "value": x} for x in days], value=days[0],
    )
]

app.layout = html.Div(
    className="container",
    children=[
        Header("{{cookiecutter.app_name}}", app),
        html.Hr(),
        Row(
            [
                Col(
                    html.Div(
                        [
                            html.Div("Controls", className="card-header"),
                            html.Div(controls, className="card-body"),
                        ],
                        className="card",
                    ),
                    md=4,
                ),
                Col(dcc.Graph(id="bar-chart"), md=8),
            ]
        ),
    ],
)


@app.callback(Output("bar-chart", "figure"), [Input("dropdown", "value")])
def update_bar_chart(day):
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill", color="smoker", barmode="group")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
