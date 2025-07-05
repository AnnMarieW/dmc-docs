
import json
import dash_ag_grid as dag
from dash import html, dcc, Input, Output, callback
import pandas as pd
import dash_mantine_components as dmc
import dash_iconify

data = {
    "ticker": ["AAPL", "MSFT", "AMZN", "GOOGL"],
    "company": ["Apple", "Microsoft", "Amazon", "Alphabet"],
    "price": [154.99, 268.65, 100.47, 96.75],
    "buy": ["Buy" for _ in range(4)],
    "sell": ["Sell" for _ in range(4)],
    "watch": ["Watch" for _ in range(4)],
}
df = pd.DataFrame(data)

columnDefs = [
    {
        "headerName": "Stock Ticker",
        "field": "ticker",
    },
    {"headerName": "Company", "field": "company", "filter": True},
    {
        "headerName": "Last Close Price",
        "type": "rightAligned",
        "field": "price",
        "valueFormatter": {"function": """d3.format("($,.2f")(params.value)"""},
    },
    {
        "field": "buy",
        "cellRenderer": "DMC_Button",
        "cellRendererParams": {
            "variant": "outline",
            "leftIcon": "ic:baseline-shopping-cart",
            "color": "green",
            "radius": "xl"
        },
    },
    {
        "field": "sell",
        "cellRenderer": "DMC_Button",
        "cellRendererParams": {
            "variant": "outline",
            "leftIcon": "ic:baseline-shopping-cart",
            "color": "red",
            "radius": "xl"
        },
    },
    {
        "field": "watch",
        "cellRenderer": "DMC_Button",
        "cellRendererParams": {
            "rightIcon": "ph:eye",
        },
    },
]

component = html.Div(
    [
        dag.AgGrid(
            id="dag-dmc-btn-grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="autoSize",
        ),
        dmc.Text(id="dag-dmc-btn-value-changed"),
    ],
)


@callback(
    Output("dag-dmc-btn-value-changed", "children"),
    Input("dag-dmc-btn-grid", "cellRendererData"),
)
def showChange(n):
    return json.dumps(n)


@callback(
    Output("dag-dmc-btn-grid", "className"),
    Input("docs-color-scheme-switch", "checked")
)
def update_theme(switch_on):
    return "ag-theme-alpine-dark" if switch_on else "ag-theme-alpine"
