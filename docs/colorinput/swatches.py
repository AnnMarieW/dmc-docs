import dash_mantine_components as dmc

component = dmc.ColorInput(
    label="Your favorite color",
    value="#e05e5e",
    w=250,
    format="hex",
    swatches=[
        "#25262b",
        "#868e96",
        "#fa5252",
        "#e64980",
        "#be4bdb",
        "#7950f2",
        "#4c6ef5",
        "#228be6",
        "#15aabf",
        "#12b886",
        "#40c057",
        "#82c91e",
        "#fab005",
        "#fd7e14",
    ],
)
