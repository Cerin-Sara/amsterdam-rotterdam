from bokeh.io import output_file, show
from bokeh.plotting import figure
import numpy as np
import pandas as pd
output_file("bedroomDetails.html")
df = pd.read_csv("bedroomDetails.csv")
location = ['Amsterdam', 'Rotterdam']
type = ["1 ROOM", "2 ROOMS", "3 ROOMS", "4 ROOMS"]
colors = ["#FFC4C4", "#718dbf", "#e84d60", "#000000"]

data = {'location' : location,
        '1 ROOM'   : [df["1 ROOM"][0], df["1 ROOM"][1]],
        '2 ROOMS'   : [df["2 ROOMS"][0], df["2 ROOMS"][1]],
        '3 ROOMS'   : [df["3 ROOMS"][0], df["3 ROOMS"][1]],
        '4 ROOMS'   : [df["4 ROOMS"][0], df["4 ROOMS"][1]]}

p = figure(x_range=location, height=500, title="Rooms in AMSTERDAM and ROTTERDAM",
           toolbar_location=None, tools="hover", tooltips="$name @location: @$name")

p.vbar_stack(type, x='location', width=0.6, color=colors, source=data,
             legend_label=type,)

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
#p.legend.location = "top_right"
p.add_layout(p.legend[0], 'right')
p.legend.orientation = "vertical"

show(p)