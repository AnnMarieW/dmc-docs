import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.TabsTab("Gallery", value="gallery"),
                dmc.TabsTab("Messages", value="messages"),
                dmc.TabsTab("Settings", value="settings"),
            ],
        ),
        dmc.TabsPanel("Gallery tab content", value="gallery", px="xs"),
        dmc.TabsPanel("Messages tab content", value="messages", px="xs"),
        dmc.TabsPanel("Settings tab content", value="settings", px="xs"),
    ],
    value="gallery",
    orientation="vertical",
    placement="right",
)

configurator = Configurator(target)

configurator.add_select("placement", ["left", "right"], "right")


component = configurator.panel
