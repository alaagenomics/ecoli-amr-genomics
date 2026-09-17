import matplotlib.pyplot as plt

samples= [
     "K-12 MG1655",
     "AR Bank #0346"
]

counts= [0, 18]

plt.figure(figsize=(8, 6))
plt.bar(samples, counts)

plt.xlabel("E. coli strain")
plt.ylabel("Unique AMR determinants")
plt.title("Comparison of AMR determinants in E. coli")

plt.tight_layout()

plt.savefig(
    "results/figures/amr_comparison.png",
     dpi=300,
     bbox_inches="tight"
)
