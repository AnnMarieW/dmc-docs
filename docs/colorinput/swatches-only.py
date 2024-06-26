import dash_mantine_components as dmc

colors = dmc.DEFAULT_THEME["colors"]

component = dmc.ColorInput(
    label="Your favorite color",
    value="#40c057",
    disallowInput=True,
    w=250,
    withPicker=False,
    swatches=colors["red"] + colors["green"],
)
