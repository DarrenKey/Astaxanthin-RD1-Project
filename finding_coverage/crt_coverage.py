import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

df = pd.read_csv("crt_codon_contig.coverage", sep="\t")

crt_df = df[(df["Pos"] >= 202) & (df["Pos"] <= 5413)]

crt_df = crt_df[["Pos", "Coverage"]]
# print(crt_df.head())

print(f"Average coverage in region: { crt_df['Coverage'].mean() }")

crt_df.plot(x="Pos", y="Coverage", title="Coverage of crt codon")
plt.savefig("crt-codon-coverage.png")
