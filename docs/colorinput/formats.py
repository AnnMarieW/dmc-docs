import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.ColorInput(value="#C5D899", format="rgb", label="Select color", w=250)

configurator = Configurator(target)

configurator.add_select("format", ["hex", "hexa", "rgba", "rgb", "hsl", "hsla"], "rgb")

component = configurator.panel
