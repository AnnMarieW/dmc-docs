import dash_mantine_components as dmc
from .data import data


component = dmc.BarChart(
    h=300,
    dataKey="month",
    data=data,
    series=[
        {"name": "Smartphones", "color": "violet.6"},
        {"name": "Laptops", "color": "blue.6"},
        {"name": "Tablets", "color": "teal.6"}
    ],
    tickLine="y",
    gridAxis="y",
    withXAxis=True,
    withYAxis=True,
    tooltipProps={"content":  {"function": "chartTooltip"}}
)