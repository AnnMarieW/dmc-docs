import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-password"

target = dmc.PasswordInput(
        label="Enter your password",
        placeholder="Password",
        description="Password must include at least one letter, number and special character",
        required=True,
        w=250,
    )

configurator = Configurator(target, center_component=True)

configurator.add_text_input("placeholder", "Password", **{"placeholder": "Placeholder"})
configurator.add_text_input("label", "Enter your password", **{"placeholder": "Label"})
configurator.add_text_input(
    "description",
    "Password must include at least one letter, number and special character",
    **{"placeholder": "Description"}
)
configurator.add_text_input("error", "", **{"placeholder": "Error"})
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_switch("required", True)

component = configurator.panel
