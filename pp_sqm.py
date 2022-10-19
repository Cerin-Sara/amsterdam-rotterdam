from bokeh.plotting import figure, show
import pandas as pd
from bokeh.models import Legend
df=pd.read_csv('ppsm.csv')
day_1_a=df['DAY1'][0]
day_1_r=df['DAY1'][1]
day_2_a=df['DAY2'][0]
day_2_r=df['DAY2'][1]
day_3_a=df['DAY3'][0]
day_3_r=df['DAY3'][1]
day_4_a=df['DAY4'][0]
day_4_r=df['DAY4'][1]
day_5_a=df['DAY5'][0]
day_5_r=df['DAY5'][1]
day_6_a=df['DAY6'][0]
day_6_r=df['DAY6'][1]
day_7_a=df['DAY7'][0]
day_7_r=df['DAY7'][1]
day_8_a=df['DAY8'][0]
day_8_r=df['DAY8'][1]
day_9_a=df['DAY9'][0]
day_9_r=df['DAY9'][1]
day_10_a=df['DAY10'][0]
day_10_r=df['DAY10'][1]
day_11_a=df['DAY11'][0]
day_11_r=df['DAY11'][1]
day_12_a=df['DAY12'][0]
day_12_r=df['DAY12'][1]
day_13_a=df['DAY13'][0]
day_13_r=df['DAY13'][1]
day_14_a=df['DAY14'][0]
day_14_r=df['DAY14'][1]
day_15_a=df['DAY15'][0]
day_15_r=df['DAY15'][1]
day_16_a=df['DAY16'][0]
day_16_r=df['DAY16'][1]
day_17_a=df['DAY17'][0]
day_17_r=df['DAY17'][1]
day_18_a=df['DAY18'][0]
day_18_r=df['DAY18'][1]
day_19_a=df['DAY19'][0]
day_19_r=df['DAY19'][1]
day_20_a=df['DAY20'][0]
day_20_r=df['DAY20'][1]
day_21_a=df['DAY21'][0]
day_21_r=df['DAY21'][1]
day_22_a=df['DAY22'][0]
day_22_r=df['DAY22'][1]
day_23_a=df['DAY23'][0]
day_23_r=df['DAY23'][1]
day_24_a=df['DAY24'][0]
day_24_r=df['DAY24'][1]
day_25_a=df['DAY25'][0]
day_25_r=df['DAY25'][1]
day_26_a=df['DAY26'][0]
day_26_r=df['DAY26'][1]
day_27_a=df['DAY27'][0]
day_27_r=df['DAY27'][1]
day_28_a=df['DAY28'][0]
day_28_r=df['DAY28'][1]
day_29_a=df['DAY29'][0]
day_29_r=df['DAY29'][1]
day_30_a=df['DAY30'][0]
day_30_r=df['DAY30'][1]
day_31_a=df['DAY31'][0]
day_31_r=df['DAY31'][1]
# day_32_a=df['DAY32'][0]
# day_32_r=df['DAY32'][1]

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
y = [day_1_a, day_2_a, day_3_a, day_4_a, day_5_a, day_6_a, day_7_a, day_8_a, day_9_a, day_10_a, day_11_a, day_12_a, day_13_a, day_14_a, day_15_a, day_16_a, day_17_a, day_18_a, day_19_a, day_20_a, day_21_a, day_22_a, day_23_a, day_24_a, day_25_a, day_26_a, day_27_a, day_28_a, day_29_a, day_30_a, day_31_a]
y1 =[day_1_r, day_2_r, day_3_r, day_4_r, day_5_r, day_6_r, day_7_r, day_8_r, day_9_r, day_10_r, day_11_r, day_12_r, day_13_r, day_14_r, day_15_r, day_16_r, day_17_r, day_18_r, day_19_r, day_20_r, day_21_r, day_22_r, day_23_r, day_24_r, day_25_r, day_26_r, day_27_r, day_28_r, day_29_r, day_30_r, day_31_r]
# p = figure()
# create a new plot with a title and axis labels
p = figure(title="Price per square metre in Amsterdam vs Rotterdam", x_axis_label='Days', y_axis_label='Price per square metre',plot_width=800,plot_height=600)
# p.xaxis.ticker = FixedTicker(ticks=list(range(1, 12))
p.xaxis.ticker = list(range(1, 32))
# add a line renderer with legend and line thickness to the plot
p.line(x, y, legend_label="Amsterdam", line_width=2,color='red', line_color='#FA7070')
p.line(x, y1, legend_label="Rottendam", line_width=2,color='green', line_color='#4C0033')
p.toolbar_location = None
p.add_layout(p.legend[0], 'right')
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
# show the results
show(p)