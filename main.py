from bokeh.plotting import figure, output_file, show, ColumnDataSource
import pandas

# x = [1, 2, 3, 4, 5]
# y = [4, 6, 2, 4, 3]

# Read in csv
df = pandas.read_csv('cars.csv')

# car = df['Car']
# hp = df['Horsepower']
source = ColumnDataSource(df)


output_file('index.html')

# car list
car_list = source.data['Car'].tolist()

# Add plot
p = figure(
    y_range= car_list,
    plot_width=800,
    plot_height=600,
    title='Cars With Top HorsePower',
    x_axis_label='Horsepower',
    y_axis_label='Cars',
    tools= 'pan, box_select, zoom_in, zoom_out,save, reset',
)

# Render glyph
p.hbar(
    y='Car',
    right='Horsepower',
    left=0,
    height=0.4,
    color='orange',
    fill_alpha=0.5,
    source=source
)

# show
show(p)

save(p)
