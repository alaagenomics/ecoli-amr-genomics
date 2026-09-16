import matplotlib.pyplot as plt
replicons = [
       "Chromosome CP066366.1",
       "Plasmid CP066367.1",
       "Plasmid CP066368.1"  ]
counts = [11, 10, 2]
plt.figure(figsize=(9, 6))
plt.bar(replicons, counts)
plt.xlabel("Genomic replicon")
plt.ylabel("AMR gene-replicon occurrences")
plt.title("AMR determinants by genomic replicon")
plt.tight_layout()
plt.savefig(
     "results/figures/amr_by_replicon.png",
     dpi=300,
     bbox_inches="tight"
)
