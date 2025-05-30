import dash_mantine_components as dmc
from dash_iconify import DashIconify

from lib.configurator import Configurator

target = dmc.ActionIconGroup(
        [
            dmc.ActionIcon(
                variant="default",
                size="lg",
                children=DashIconify(icon="tabler:photo", width=20),
                n_clicks=0,
            ),
            dmc.ActionIcon(
                variant="default",
                size="lg",
                children=DashIconify(icon="tabler:settings", width=20),
                n_clicks=0,
            ),
            dmc.ActionIcon(
                variant="default",
                size="lg",
                children=DashIconify(icon="tabler:heart", width=20),
                n_clicks=0,
            ),
        ],
        orientation="horizontal",
    )

configurator = Configurator(target, center_component=True)
configurator.add_segmented_control("orientation", ["horizontal", "vertical"], "horizontal")

component = configurator.panel

