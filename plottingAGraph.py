import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

df = pd.read_csv('graph_file.csv')

trace1 = go.Scatter( x=df['index'], y=df['health'], mode='lines+markers', showlegend=True)
layout = go.Layout(title='Tracking all populations', plot_bgcolor='rgb(230, 230,230)')
fig = go.Figure(data=[trace1], layout=layout)
py.plot(fig, filename='graph')