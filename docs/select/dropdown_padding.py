import dash_mantine_components as dmc

component = dmc.Paper(
    [
        dmc.Select(
            label="Zero padding",
            data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
            placeholder="Pick value",
            comboboxProps={"dropdownPadding": 0},
            w=400,
        ),
        dmc.Select(
            label="10px padding",
            data=["Pandas", "NumPy", "TensorFlow", "PyTorch"],
            placeholder="Pick value",
            comboboxProps={"dropdownPadding": 10},
            w=400,
            mt="md",
        ),
    ]
)