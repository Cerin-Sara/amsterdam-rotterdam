from turtle import left
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
import pandas as pd

output_file("balcony.html")

locations = ['Amsterdam', 'Rotterdam']
status = ['PRESENT', 'NOT PRESENT']
df = pd.read_csv('balcony.csv')
data = {'locations' : locations,
        'PRESENT'   : [df['PRESENT'][0], df['PRESENT'][1]],
        'NOT PRESENT': [df['NOT PRESENT'][0], df['NOT PRESENT'][1]]}

# this creates [ ("Amsterdam", "presentBalcony"), ("Amsterdam", "notPresentBalcony"), ("Rotterdam", "presentBalcony"), ("Rotterdam", "notPresentBalcony")]
x = [ (location, stat) for location in locations for stat in status ]
counts = sum(zip(data['PRESENT'], data['NOT PRESENT'],), ()) # like an hstack

source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), height=500, title="Balcony details in Amsterdam and Rotterdam",toolbar_location=None, tools="")

p.vbar(x='x', top='counts', width=0.4, source=source, color="#850E35")

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
show(p)