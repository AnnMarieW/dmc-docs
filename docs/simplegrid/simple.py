import dash_mantine_components as dmc
from dash import html

from components.configurator import Configurator

style = {
    "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
    "textAlign": "center",
}

target = dmc.SimpleGrid(
    cols=3,
    children=[
        html.Div("1", style=style),
        html.Div("2", style=style),
        html.Div("3", style=style),
        html.Div("4", style=style),
        html.Div("5", style=style),
    ],
)

configurator = Configurator(target)

configurator.add_slider("spacing", "md")
configurator.add_number_input("cols", 3, min=1, max=6)

component = configurator.panel