import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Indicator(
        dmc.Avatar(
            size="lg",
            radius="sm",
            src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-1.png",
        ),   
    )

configurator = Configurator(target, center_component=True)

configurator.add_colorpicker("color", "indigo")
configurator.add_select(
    "position",
    [
        "bottom-end",
        "bottom-start",
        "top-end",
        "top-start",
        "bottom-center",
        "top-center",
        "middle-center",
        "middle-end",
        "middle-start",
    ],
    "top-end",
)
configurator.add_number_input("size", 10)
configurator.add_slider("radius", "xl")
configurator.add_switch("processing", False)
configurator.add_switch("withBorder", False)
configurator.add_switch("disabled", False)

component = configurator.panel
