from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data


component = dmc.Group(
    [
        dmc.AreaChart(
            id="figure-areachart",
            h=300,
            dataKey="date",
            data=data,
            type="stacked",
            series=[
                {"name": "Apples", "color": "indigo.6"},
                {"name": "Oranges", "color": "blue.6"},
                {"name": "Tomatoes", "color": "teal.6"},
            ],
        ),
        dmc.Text(id="clickdata-areachart1"),
        dmc.Text(id="clickdata-areachart2"),
    ]
)


@callback(
    Output("clickdata-areachart1", "children"),
    Output("clickdata-areachart2", "children"),
    Input("figure-areachart", "clickData"),
    Input("figure-areachart", "clickSeriesName"),
)
def update(data, name):
    return f"clickData:  {data}", f"clickSeriesName: {name}"
