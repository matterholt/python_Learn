from bokeh.plotting import figure, output_file, show
# Data
x = [1,2,3,4,5]
y = [6,7,2,4,5]

#output to sttic HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="Simple Line Example", x_axis_label="X", y_axis_label="Y")

#add a line renderer with legend and line thickness
p.line(x,y, legend="Temp.", line_width=3)

#show the results 
show(p)