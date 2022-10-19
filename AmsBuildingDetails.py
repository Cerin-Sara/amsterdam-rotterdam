from math import pi
import pandas as pd
from bokeh.palettes import Category20c
from bokeh.plotting import figure, show
from bokeh.transform import cumsum
import pandas as pd
# prepare some data
df=pd.read_csv('buildingDetails.csv')
ams_apartments = df['APARTMENTS'][0]
ams_houses = df['HOUSES'][0]
ams_others = df['OTHERS'][0]
rot_apartments = df['APARTMENTS'][1]
rot_houses = df['HOUSES'][1]
rot_others = df['OTHERS'][1]
chart_colors = ['#4C0033', '#25316D', '#F2D388']
ams = {
    'ams_house': ams_houses,
    'ams_apartments': ams_apartments,
    'ams_others': ams_others,  
}


data = pd.Series(ams).reset_index(name='value').rename(columns={'index': 'AMSTERDAM'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = chart_colors[:len(data)]


p = figure(height=500, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@AMSTERDAM: @value", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='AMSTERDAM', source=data)

p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None

show(p)

