import plotly_gruvbox_colorscheme
import plotly.express as px
import plotly.io as pio

# pio.templates.default = "plotly"
# pio.templates.default = "gruvbox_light"
# pio.templates.default = "plotly_dark"
pio.templates.default = "gruvbox_dark"
df = px.data.gapminder()
df_2007 = df.query("year==2007")

fig = px.scatter(df_2007,
                 x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 log_x=True, size_max=60,
                 title="Gapminder 2007: current default theme")
fig.show()
##

import pandas as pd
import plotly.graph_objects as go

z_data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv")



fig = go.Figure(
    data=go.Surface(z=z_data.values * 10),
    layout=go.Layout(
        title="Mt Bruno Elevation",
    ))
fig.show()

##
import plotly.graph_objects as go

fig = go.Figure(go.Carpet(
    a = [4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6],
    b = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    y = [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10],
    aaxis = dict(
        tickprefix = "a = ",
        ticksuffix = "m",
        smoothing = 1,
        minorgridcount = 9,
    ),
    baxis = dict(
        tickprefix = "b = ",
        ticksuffix = "pa",
        smoothing = 1,
        minorgridcount = 9,
    )
))

fig.show()

##

fig = go.Figure(data=[go.Table(header=dict(values=["A Scores", "B Scores"]),
                 cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
                     ])
fig.show()

