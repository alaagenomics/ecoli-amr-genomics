import matplotlib.pyplot as plt
classes = [
     "Aminoglycoside",
     "Beta-lactam",
     "Phenicol",
     "Macrolide",
     "Sulfonamide",
     "Trimethoprim",
     "Fosfomycin",
     "Colistin",
     "Tetracycline"  ]
counts = [4, 4, 2, 2, 2, 1, 1, 1, 1]
plt.figure(figsize=(10, 6))
plt.bar(classes, counts)
plt.xlabel("Antibiotic class")
plt.ylabel("Number of unique AMR determinants")
plt.title("Antimicrobial resistance determinants by antibiotic class")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(
     "results/figures/amr_by_antibiotic_class.png",
      dpi=300,
      bbox_inches="tight"
)

