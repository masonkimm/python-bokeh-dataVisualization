from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
from bokeh.embed import components
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
    fill_color=factor_cmap(
        'Car',
        palette=Blues8,
        factors = car_list
    ),
    fill_alpha=0.9,
    source=source,
    legend_label='Car'
)

# Add legend
p.legend.orientation = 'vertical'
p.legend.location = 'top_right'
p.legend.label_text_font_size = '10px'

# Add tooltips
hover = HoverTool()
hover.tooltips = '''
<div>
    <h3> @Car <h3/>
    <div> <strong> Price:  </strong>@Price </div>
    <div> <strong> HP:  </strong>@Horsepower </div>
    <div> <img src="@Image" alt="" width="200"/></div>
</div>
'''

p.add_tools(hover)

# show
# show(p)

# save
save(p)

# Print out div and script
script, div = components(p)
print(div)
print(script)