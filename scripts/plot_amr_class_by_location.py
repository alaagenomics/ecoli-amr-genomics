import matplotlib.pyplot as plt

classes = [
    "Aminoglycoside",
    "Beta-lactam",
    "Colistin",
    "Fosfomycin",
    "Macrolide",
    "Phenicol",
    "Sulfonamide",
    "Tetracycline",
    "Trimethoprim"
]

chromosome = [3, 2, 0, 0, 2, 1, 2, 0, 1]
plasmid = [3, 4, 1, 1, 0, 1, 1, 1, 0]

x = range(len(classes))

plt.figure(figsize=(10, 6))
plt.bar(x, chromosome, label="Chromosome")
plt.bar(x, plasmid, bottom=chromosome, label="Plasmid")

plt.xticks(x, classes, rotation=45, ha="right")
plt.xlabel("Antibiotic class")
plt.ylabel("AMR gene-replicon occurrences")
plt.title("AMR Determinants by Antibiotic Class and Genomic Location")
plt.legend()

plt.tight_layout()

plt.savefig(
    "results/figures/amr_class_by_location.png",
    dpi=300,
    bbox_inches="tight"
)
