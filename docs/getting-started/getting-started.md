---
name: Getting Started
endpoint: /getting-started
description: Install dash-mantine-components using pip, poetry, or conda.
dmc: false
---

.. toc::

### PyPI

You can install `dash-mantine-components` from PyPI via pip or poetry.

```bash
pip install dash-mantine-components
```

```bash
poetry add dash-mantine-components
```

### Simple Usage

Using Dash Mantine Components is pretty much the same as using Dash Bootstrap Components or the official Dash 
components. 

.. admonition::Don't Forget MantineProvider!
   :icon: radix-icons:info-circled
   :color: red

   It's required that you wrap your app with a dmc.MantineProvider, else dash will complain.

.. admonition::React 18 Issue
   :icon: radix-icons:info-circled
   :color: red

   Dash Mantine Components is based on REACT 18. You must set the env variable REACT_VERSION=18.2.0 before starting up the app.

```python
import dash_mantine_components as dmc
from dash import Dash

app = Dash(__name__)

app.layout = dmc.MantineProvider(
    dmc.Alert(
       "Hi from Dash Mantine Components. You can create some great looking dashboards using me!",
       title="Welcome!",
       color="violet",
    )
)

if __name__ == "__main__":
    app.run_server()
```

### Extensions

Most of the styling is already included but if you are using components like `DatePicker`, `Carousel`, or `CodeHighlight`, then 
you need to include css for them separately.

```python
from dash import Dash

# below covers all the stylesheets, you can pick as per your need.
stylesheets = [
    "https://unpkg.com/@mantine/dates@7/styles.css",
    "https://unpkg.com/@mantine/code-highlight@7/styles.css",
    "https://unpkg.com/@mantine/charts@7/styles.css",
    "https://unpkg.com/@mantine/carousel@7/styles.css",
    "https://unpkg.com/@mantine/notifications@7/styles.css",
    "https://unpkg.com/@mantine/nprogress@7/styles.css",
]

app = Dash(__name__, external_stylesheets=stylesheets)
```

### Documentation

This entire documentation has been created almost entirely using Dash Mantine Components. You can check out the source
code [here](https://github.com/snehilvj/dmc-docs) for some inspiration.

While going through this documentation, you will come across interactive demos meant to show an overview as well as the overall effect of different combinations of a component's props.

.. exec::docs.getting-started.interactive
   :code: false

Note that this documentation has some additional styling applied to it. So when you actually use these components, they 
might look a bit different. You can check out [MantineProvider](/components/mantineprovider) for more details on
theming and customizations.

Here's how you can add the same styling to your apps:

```python
import dash_mantine_components as dmc
from dash import Dash

app = Dash(__name__)

app.layout = dmc.MantineProvider(
     forceColorScheme="light",
     theme={
         "primaryColor": "indigo",
         "fontFamily": "'Inter', sans-serif",
         "components": {
             "Button": {"defaultProps": {"fw": 400}},
             "Alert": {"styles": {"title": {"fontWeight": 500}}},
             "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
             "Badge": {"styles": {"root": {"fontWeight": 500}}},
             "Progress": {"styles": {"label": {"fontWeight": 500}}},
             "RingProgress": {"styles": {"label": {"fontWeight": 500}}},
             "CodeHighlightTabs": {"styles": {"file": {"padding": 12}}},
             "Table": {
                 "defaultProps": {
                     "highlightOnHover": True,
                     "withTableBorder": True,
                     "verticalSpacing": "sm",
                     "horizontalSpacing": "md",
                 }
             },
         },
     },
     children=[
         # content
     ],
 )

if __name__ == "__main__":
    app.run_server()
```
