"""
- try to see if can make a scheduleing copy simular to FTECH
"""

import pandas as pd 
import numpy as np
from bokeh.plotting import figure, output_file, show

df = pd.read_csv("dataSch.csv")

plan = "square"
clean = "circle"
build = "triangle"

dateData = np.array(df["start"], dtype='datetime64')
howLong  = np.array(df["numDay"], dtype='datetime64')


'''

print(howLong)

numb = np.array([1,2,3,4,5,6])

output_file("Schedule.html", title = "Weekly Schedule")

chart = figure(
    plot_width = 400,
    plot_height = 250,
    x_axis_type = "datetime"
)
chart.circle(dateData, numb, size=4, color='black')

show(chart)
'''