import string
from random import choice

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
from dash.exceptions import PreventUpdate

ALL = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


def generate_password(password_length: int) -> str:
    return "".join(choice(ALL) for _ in range(password_length))


external_scripts = ["https://cdn.plot.ly/plotly-1.39.1.min.js"]
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(
    __name__,
    external_scripts=external_scripts,
    external_stylesheets=[dbc.themes.SLATE, external_stylesheets]
)
app.config["suppress_callback_exceptions"] = True
server = app.server

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                html.Div(
                                    [
                                        dbc.Button(
                                            "Generate Password",
                                            id="generate-password-button",
                                            n_clicks=0,
                                            size="sm",
                                            style={
                                                "background-color": "#913535",
                                                "border": "transparent",
                                                "font-weight": "bold",
                                                "width": "90%",
                                            },
                                            className="mt-3"
                                        )
                                    ],
                                    className="d-flex justify-content-center"
                                ),
                                html.Div(
                                    id="password-space",
                                    style={"padding": 10}
                                ),
                                html.Div(
                                    id="password",
                                    className="d-flex justify-content-center mb-3",
                                )
                            ],
                            className="card border-dark mb-1 mt-3 ml-2 mr-2"
                        )
                    ],
                    width=3,
                )
            ],
            justify="center",
        )
    ],
    fluid=True,
)


@app.callback(
    Output("password", "children"),
    Input("generate-password-button", "n_clicks")
)
def update_generate_password_button(n_clicks):
    if n_clicks > 0:
        return generate_password(16), ""

    raise PreventUpdate


if __name__ == "__main__":
    app.run_server(debug=True, port=8125)
