import dash_mantine_components as dmc

spending_data = [
    {
        "color": "cyan",
        "name": "Average monthly spending",
        "data": [
            {"age": a, "average_monthly_spending": b}
            for a, b in zip(
                [
                    25,
                    30,
                    35,
                    40,
                    45,
                    28,
                    22,
                    50,
                    32,
                    48,
                    26,
                    38,
                    42,
                    29,
                    34,
                    44,
                    23,
                    37,
                    49,
                    27,
                    41,
                    31,
                    46,
                    24,
                    33,
                    39,
                    47,
                    36,
                    43,
                    21,
                ],
                [
                    1400,
                    2100,
                    1800,
                    2400,
                    2300,
                    1600,
                    1200,
                    3200,
                    1900,
                    2700,
                    1700,
                    2200,
                    2600,
                    1500,
                    2000,
                    2500,
                    1300,
                    2100,
                    2900,
                    1600,
                    2500,
                    1800,
                    2700,
                    1400,
                    2100,
                    2400,
                    2800,
                    2200,
                    2600,
                    1100,
                ],
            )
        ],
    }
]

component = dmc.ScatterChart(
    h=300,
    data=spending_data,
    dataKey={"x": "age", "y": "average_monthly_spending"},
    yAxisProps={"domain": [800, 3500]},
    valueFormatter={
        "x": {"function": "formatYears"},
        "y": {"function": "formatCurrency"}
    }
)
