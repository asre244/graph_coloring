from bokeh.plotting import figure, output_notebook, show
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource
import networkx as nx
import numpy as np

output_notebook()

# Create a graph
edges = [[0, 1], [1, 2], [1, 3]]
G = nx.Graph()
G.add_edges_from(edges)

# Create a plot
p = figure(title="Interactive Network", x_range=(-1.5, 1.5), y_range=(-1.5, 1.5))
p.xgrid.visible = False
p.ygrid.visible = False
p.title.text_font_size = '16pt'

# Set up the graph renderer
graph_renderer = GraphRenderer()

# Convert the NetworkX graph to Bokeh
pos = nx.spring_layout(G)
node_x = [pos[node][0] for node in G.nodes()]
node_y = [pos[node][1] for node in G.nodes()]

# Create the Bokeh data sources
graph_renderer.node_renderer.data_source.add(node_x, 'x')
graph_renderer.node_renderer.data_source.add(node_y, 'y')
graph_renderer.node_renderer.glyph = Circle(size=15)

edge_start = [edge[0] for edge in edges]
edge_end = [edge[1] for edge in edges]

graph_renderer.edge_renderer.data_source.data = {
    'start': edge_start,
    'end': edge_end
}
graph_renderer.edge_renderer.glyph.line_color = 'gray'
graph_renderer.edge_renderer.glyph.line_width = 2

# Set up the layout provider
graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=pos)

# Add the graph to the plot
p.add_renderers(graph_renderer)

# Add labels
node_labels = list(G.nodes())
node_label_x = [pos[node][0] for node in G.nodes()]
node_label_y = [pos[node][1] for node in G.nodes()]
labels = LabelSet(x='x', y='y', text=node_labels, source=ColumnDataSource(data=dict(x=node_label_x, y=node_label_y)), level='glyph',
                   x_offset=5, y_offset=5, render_mode='canvas', text_font_size='12pt')

p.add_layout(labels)

# Show the plot
show(p)
