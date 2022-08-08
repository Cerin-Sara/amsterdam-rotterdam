from turtle import color
import plotly.graph_objects as go
import pandas as pd


fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="Price per square metre"
)
fig.show()