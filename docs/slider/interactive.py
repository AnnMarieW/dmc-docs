import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Slider(
    value=69,
    updatemode="mouseup",
    marks=[
        {"value": 20, "label": "20%"},
        {"value": 50, "label": "50%"},
        {"value": 80, "label": "80%"},
    ],
)

configurator = Configurator(target)

configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "md")
configurator.add_slider("radius", "lg")
configurator.add_switch("showLabelOnHover", True)
configurator.add_switch("labelAlwaysOn", False)

component = configurator.panel
