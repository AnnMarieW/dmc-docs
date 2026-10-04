---
name: Pagination
description: Display active page and navigate between multiple pages
endpoint: /components/pagination
package: dash_mantine_components
category: Navigation
---

.. toc::
.. llms_copy::Pagination

### Introduction

.. exec::docs.pagination.interactive
    :code: false

### Siblings

Control the number of active item siblings with `siblings` prop.

.. exec::docs.pagination.siblings

### Boundaries

Control the number of items displayed after previous(<) and before next(>) buttons with `boundaries` prop.

.. exec::docs.pagination.boundaries

### Hide pages controls
Set `withPages=False` to hide pages controls:

.. exec::docs.pagination.withpages

### Controls size

By default, pagination controls have reduced size compared to inputs and buttons. If you want controls to have the same 
size as inputs and buttons, you can use the `input-` prefix for the size prop:


.. exec::docs.pagination.size

### Start value

Set `startValue` to define the starting page number. For example, with `startValue=5` and `total=15`, the pagination
range will be from 5 to 15:

.. exec::docs.pagination.start_value

### Styles API

.. styles_api_text::

| Name    | Static selector             | Description                                               |
|:--------|:----------------------------|:----------------------------------------------------------|
| root    | .mantine-Pagination-root    | Root element                                              |
| control | .mantine-Pagination-control | Control element: items, next/previous, first/last buttons |
| dots    | .mantine-Pagination-dots    | Dots icon wrapper                                         |


### Keyword Arguments
.. style_props_text::

#### Pagination

.. kwargs::Pagination
