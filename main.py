from bokeh.plotting import figure, output_file, show
import pandas

# x = [1, 2, 3, 4, 5]
# y = [4, 6, 2, 4, 3]

# Read in csv
df = pandas.read_csv('cars.csv')

car = df['Car']
hp = df['Horsepower']

output_file('index.html')

# Add plot
p = figure(
    y_range=car,
    plot_width=800,
    plot_height=600,
    title='Cars With Top HorsePower',
    x_axis_label='Horsepower',
    # y_axis_label='Y Axis'
    tools=''
)

# Render glyph
p.hbar(
    y=car,
    right=hp,
    left=0,
    height=0.4,
    color='orange',
    fill_alpha=0.5
)

# show
show(p)
