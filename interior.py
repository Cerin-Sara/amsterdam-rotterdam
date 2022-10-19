from bokeh.io import output_file, show
from bokeh.plotting import figure
import numpy as np
import pandas as pd
output_file("interior.html")
df = pd.read_csv("interior.csv")
location = ['Amsterdam', 'Rotterdam']
type = ["FURNISHED", "NOT FURNISHED"]
colors = ["#FFC4C4", "#718dbf"]

data = {'location' : location,
        'FURNISHED'   : [df["FURNISHED"][0], df["FURNISHED"][1]],
        'NOT FURNISHED'   : [df["FURNISHED"][0], df["NOT FURNISHED"][1]]}

p = figure(x_range=location, height=500, title="Interior works details in AMSTERDAM and ROTTERDAM",toolbar_location=None, tools="hover", tooltips="$name @location: @$name")

p.vbar_stack(type, x='location', width=0.4, color=colors, source=data,
             legend_label=type,)

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
#p.legend.location = "top_right"
p.add_layout(p.legend[0], 'right')
p.legend.orientation = "vertical"

show(p)