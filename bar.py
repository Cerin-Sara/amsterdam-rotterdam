from bokeh.plotting import figure, show
import pandas as pd
# prepare some data
df=pd.read_csv('daily_graph.csv')
day_1_a=df['DAY1'][0]
day_1_r=df['DAY1'][1]
day_2_a=df['DAY2'][0]
day_2_r=df['DAY2'][1]
day_3_a=df['DAY3'][0]
day_3_r=df['DAY3'][1]
day_4_a=df['DAY4'][0]
day_4_r=df['DAY4'][1]
x = [1, 2, 3, 4]
y = [day_1_a, day_2_a, day_3_a, day_4_a]
y1 =[day_1_r, day_2_r, day_3_r, day_4_r]

# create a new plot with a title and axis labels
p = figure(title="Line trial", x_axis_label='Days', y_axis_label='Price per square metre')

# add a line renderer with legend and line thickness to the plot
p.line(x, y, legend_label="Amsterdam", line_width=2,color='red')
p.line(x, y1, legend_label="Rottendam", line_width=2,color='green')
p.toolbar_location = "below"

# show the results
show(p)