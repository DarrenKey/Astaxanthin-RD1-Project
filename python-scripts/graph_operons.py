from dna_features_viewer import GraphicFeature, GraphicRecord
from bokeh.plotting import figure, output_file, show
output_file("test.html")

features = [
    GraphicFeature(start=0, end=20, strand=+1, color="#ffd700",
                   label="Small feature"),
    GraphicFeature(start=20, end=500, strand=+1, color="#ffcccc",
                   label="Gene 1 with a very long name"),
    GraphicFeature(start=400, end=700, strand=-1, color="#cffccc",
                   label="Gene 2"),
    GraphicFeature(start=600, end=900, strand=+1, color="#ccccff",
                   label="Gene 3")
]
record = GraphicRecord(sequence_length=1000, features=features)

x = record.plot_with_bokeh(figure_width=10)

show(x)

print(type(record.plot_with_bokeh(figure_width=5)))
