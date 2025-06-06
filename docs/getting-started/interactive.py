import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Button("Settings")

configurator = Configurator(target, center_component=True)

configurator.add_select(
    "variant",
    ["link", "filled", "outline", "light", "gradient", "subtle", "default"],
    "filled",
)
configurator.add_colorpicker("color", "indigo")
configurator.add_switch("loading", False)

component = configurator.panel
