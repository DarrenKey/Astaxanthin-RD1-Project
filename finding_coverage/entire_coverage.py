import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

df = pd.read_csv("rd1_genome.coverage", sep="\t")

print(f"Summary: { df['Coverage'].describe() }")
