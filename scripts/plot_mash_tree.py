import matplotlib.pyplot as plt
from Bio import Phylo

tree = Phylo.read(
    "results/phylogeny/ecoli_mash_neighbor_joining.nwk",
    "newick"
)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(1, 1, 1)

Phylo.draw(
    tree,
    axes=ax,
    do_show=False
)

ax.set_title(
    "Neighbor-Joining Tree Based on Mash Whole-Genome Distances"
)

plt.tight_layout()

plt.savefig(
    "results/figures/ecoli_mash_neighbor_joining_tree.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()
