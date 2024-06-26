import dash_mantine_components as dmc
from dash import html

component = html.Div(
    [
        dmc.RadioGroup(
            children=dmc.Group(
                [dmc.Radio(i, value=i) for i in ["USA", "Canada", "France"]], my=10
            ),
            value="USA",
            label="Size Example - small",
            size="sm",
            mt=10,
        ),
        dmc.RadioGroup(
            children=dmc.Group(
                [dmc.Radio(i, value=i) for i in ["USA", "Canada", "France"]], my=10
            ),
            value="USA",
            label="Size Example - large",
            size="lg",
            mt=30,
        ),
    ]
)
