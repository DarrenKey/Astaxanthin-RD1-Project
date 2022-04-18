from dna_features_viewer import GraphicFeature, GraphicRecord, BiopythonTranslator
from bokeh.plotting import figure, output_file, show, save

graphic_record = BiopythonTranslator().translate_record(
    "test2.gb")
x = graphic_record.plot_with_bokeh(
    figure_width=10)


output_file("test.html")

save(x)

# from Bio import SeqIO

# with open("../processing-pcr-phred-scores/CRTW-F1-D.fastq", 'r') as input_file:
#     for record in SeqIO.parse(input_file, "fastq"):
#         score = record.letter_annotations["phred_quality"]
# from pybioviz import dashboards
# import panel as pn
# # need to load panel extension first
# pn.extension()
# app = dashboards.genome_features_viewer("crt-operon-from-Prokka.gff")
