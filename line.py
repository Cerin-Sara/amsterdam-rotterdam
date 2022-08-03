from turtle import color
from bokeh.plotting import figure, show
# prepare some data
x = [1, 2, 3, 4, 5]
y = [100, 200, 300, 400, 500]
y1 = [250, 100, 300, 500, 100]

# create a new plot with a title and axis labels
p = figure(title="Line trial", x_axis_label='Days', y_axis_label='Price per square metre')

# add a line renderer with legend and line thickness to the plot
p.line(x, y, legend_label="Amsterdam", line_width=2,color='red')
p.line(x, y1, legend_label="Rottendam", line_width=2,color='green')


# show the results
show(p)