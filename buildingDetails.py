from bokeh.io import output_file, show
from bokeh.plotting import figure
import pandas as pd
output_file("buildingDetails.html")
df = pd.read_csv("buildingDetails.csv")
location = ['Amsterdam', 'Rotterdam']
type = ["APARTMENTS","HOUSES", "OTHERS"]
colors = ["#FFC4C4", "#718dbf", "#e84d60"]

data = {'location' : location,
        'APARTMENTS'   : [df["APARTMENTS"][0], df["APARTMENTS"][1]],
        'HOUSES'   : [df["HOUSES"][0], df["HOUSES"][1]],
        'OTHERS'   : [df["OTHERS"][0], df["OTHERS"][1]],}

p = figure(x_range=location, height=500, title="Building types in AMSTERDAM and ROTTERDAM",
           toolbar_location=None, tools="hover", tooltips="$name @location: @$name")

p.vbar_stack(type, x='location', width=0.4, color=colors, source=data,legend_label=type,)

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