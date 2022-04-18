import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Bio import SeqIO

plt.close("all")

record = SeqIO.parse("CRTW-F1-C.ab1", "abi")
for seq in record:
    # print(seq)
    seqName = seq.id
    seqStr = str(seq.seq)
    seqQual = seq.letter_annotations["phred_quality"]

    print(seq.keys())
    print(seqQual)


# df = pd.read_csv("crt_codon_contig.coverage", sep="\t")

# crt_df = df[(df["Pos"] >= 202) & (df["Pos"] <= 5413)]

# crt_df = crt_df[["Pos", "Coverage"]]

# # print(crt_df.head())
# print(f"Average coverage in region: { crt_df['Coverage'].mean() }")

# crt_df.plot(x="Pos", y="Coverage", title="Coverage of crt codon")
# plt.savefig("crt-codon-coverage.png")
