import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Checkbox(label="I agree to sell my privacy.", checked=True)

configurator = Configurator(target, center_component=True)

configurator.add_segmented_control("labelPosition", ["left", "right"], "right")
configurator.add_text_input("label", "I agree to sell my privacy")
configurator.add_text_input("description", "")
configurator.add_text_input("error", "")
configurator.add_colorpicker("color", "indigo")
configurator.add_segmented_control("variant", ["filled", "outline"], "filled")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_switch("disabled", False)
configurator.add_switch("indeterminate", False)

component = configurator.panel
