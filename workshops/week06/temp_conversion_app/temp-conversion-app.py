"""
Temperature conversion app

A small web application built around the temperature conversion function from
week 5 (Exercise 3). Running this script starts a local web server — open the
URL printed in the terminal to use the app.

The code needs the "dash" package, which is not installed in your base
environment. Create the environment for this project first:

    conda env create --file environment.yml
    conda activate temp-conversion-app

If you would like to learn how dash works, see their
"Dash in 20 Minutes" tutorial: https://dash.plotly.com/tutorial

Note: this is only a demonstration — building dash applications is not part of
the TECH2 curriculum.
"""

from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc


def temp_conversion(temp, scale):
    """
    Convert a temperature between Fahrenheit and Celsius.

    Parameters
    ----------
    temp : float
        The temperature to convert.
    scale : str
        "F" to convert Fahrenheit to Celsius, or "C" to convert Celsius to
        Fahrenheit.

    Returns
    -------
    float
        The converted temperature.
    """
    if scale == "F":
        return (5 / 9) * (temp - 32)
    else:
        return (9 / 5) * temp + 32


# Input for the temperature, and the field displaying the conversion
conversion = dbc.Row(
    children=[
        dbc.Col(dbc.Input(id="temp", type="number", placeholder="Enter temperature...")),
        dbc.Col(html.H4(id="output", children=""))
    ]
)

# Radio buttons to select the direction of the conversion
buttons = dbc.RadioItems(
    id="scale",
    options=[
        {"label": "Celsius to Fahrenheit", "value": "C"},
        {"label": "Fahrenheit to Celsius", "value": "F"}
    ],
    value="C",
    inline=True
)

# Place the inputs and the output inside a card
card = dbc.Card(
    children=[
        dbc.CardHeader("Temperature conversion calculator"),
        dbc.CardBody(
            children=[
                buttons,
                html.Br(),
                conversion,
                html.Br(),
                html.P("Example: (0°C × 9/5) + 32 = 32°F")
            ]
        )
    ]
)

# Initialize the app
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout
app.layout = dbc.Container(
    children=[
        dbc.Row(dbc.Col(card, width=6))
    ],
    className="dbc"
)


# Update the displayed conversion whenever an input changes
@app.callback(
    Output(component_id="output", component_property="children"),
    Input(component_id="temp", component_property="value"),
    Input(component_id="scale", component_property="value"),
)
def update_conversion(temp, scale):
    if temp is not None:
        converted_temp = temp_conversion(temp, scale)
        if scale == "C":
            return f"= {converted_temp:.1f} °F"
        else:
            return f"= {converted_temp:.1f} °C"


if __name__ == "__main__":
    app.run(debug=True)
