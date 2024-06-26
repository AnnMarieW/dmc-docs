import dash_mantine_components as dmc

text = """We Butter the Bread with Butter was founded in 2007 by Marcel Neumann, who was originally guitarist for 
Martin Kesici's band, and Tobias Schultka. The band was originally meant as a joke, but progressed into being a more 
serious musical duo. The name for the band has no particular meaning, although its origins were suggested from when 
the two original members were driving in a car operated by Marcel Neumann and an accident almost occurred. Neumann 
found Schultka "so funny that he briefly lost control of the vehicle." Many of their songs from this point were 
covers of German folk tales and nursery rhymes."""

component = dmc.Spoiler(
    showLabel="Show more",
    hideLabel="Hide",
    maxHeight=50,
    children=[dmc.Text(text)],
)
