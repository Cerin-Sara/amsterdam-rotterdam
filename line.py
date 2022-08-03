from turtle import color
from bokeh.plotting import figure, show
import numpy as np
import pandas as pd
# prepare some data
df=pd.read_csv('graph.csv')
day_1_a=df['DAY1'][0]
day_1_r=df['DAY1'][1]
x = [1, 2]
y = [day_1_a, 200]
y1 = [day_1_r, 100]

# create a new plot with a title and axis labels
p = figure(title="Line trial", x_axis_label='Days', y_axis_label='Price per square metre')

# add a line renderer with legend and line thickness to the plot
p.line(x, y, legend_label="Amsterdam", line_width=2,color='red')
p.line(x, y1, legend_label="Rottendam", line_width=2,color='green')


# show the results
show(p)