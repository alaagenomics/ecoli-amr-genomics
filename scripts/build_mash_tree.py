from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor
from Bio import Phylo

names = [
    "K12_MG1655",
    "AR0346",
    "EC958",
    "CFT073",
    "W3110",
    "EDL933"
]

distances = {
    ("K12_MG1655", "AR0346"): 0.00564181,
    ("K12_MG1655", "EC958"): 0.0296126,
    ("K12_MG1655", "CFT073"): 0.0312752,
    ("K12_MG1655", "W3110"): 0.0000955247,
    ("K12_MG1655", "EDL933"): 0.0223484,
    ("AR0346", "EC958"): 0.0316813,
    ("AR0346", "CFT073"): 0.0327227,
    ("AR0346", "W3110"): 0.0055427,
    ("AR0346", "EDL933"): 0.0242142,
    ("EC958", "CFT073"): 0.0149234,
    ("EC958", "W3110"): 0.0295179,
    ("EC958", "EDL933"): 0.0331502,
    ("CFT073", "W3110"): 0.0311746,
    ("CFT073", "EDL933"): 0.0342477,
    ("W3110", "EDL933"): 0.0223484,
}

matrix = []

for i, name_i in enumerate(names):
    row = []
    for j in range(i + 1):
        if i == j:
            row.append(0.0)
        else:
            name_j = names[j]
            key = (name_j, name_i)
            if key not in distances:
                key = (name_i, name_j)
            row.append(distances[key])
    matrix.append(row)

dm = DistanceMatrix(names, matrix)

constructor = DistanceTreeConstructor()
tree = constructor.nj(dm)

Phylo.write(
    tree,
    "results/phylogeny/ecoli_mash_neighbor_joining.nwk",
    "newick"
)

Phylo.draw_ascii(tree)
