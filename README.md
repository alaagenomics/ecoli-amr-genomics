# Comparative Genomic Analysis of Antimicrobial Resistance in *Escherichia coli*

## Project Overview

This project investigates the genomic distribution of antimicrobial resistance (AMR) determinants in *Escherichia coli* using publicly available whole-genome sequence data and command-line bioinformatics tools.

The analysis compares *E. coli* K-12 MG1655, a complete reference strain, with *E. coli* AR Bank #0346, a multidrug-resistant isolate from the CDC & FDA Antimicrobial Resistance Isolate Bank.

The project focuses on:

* Genome quality assessment
* Bacterial genome annotation
* AMR determinant identification
* AMR classification by antibiotic class
* Chromosomal and plasmid localization of AMR determinants
* Comparative AMR analysis
* Genomic context of selected resistance determinants
* Whole-genome distance analysis using Mash
* Data visualization and reproducible scripting

This project was developed as a practical bacterial genomics and antimicrobial resistance bioinformatics portfolio project.

---

## Research Question

**How does the genomic distribution of antimicrobial resistance determinants differ between a reference *E. coli* strain and a multidrug-resistant *E. coli* isolate?**

---

## Objectives

1. Assess the quality and genomic structure of the selected *E. coli* genomes.
2. Annotate bacterial genomic features using Bakta.
3. Identify AMR determinants using AMRFinderPlus.
4. Classify detected determinants by antibiotic class.
5. Determine the genomic replicon associated with each AMR determinant.
6. Compare AMR profiles between K-12 MG1655 and AR Bank #0346.
7. Examine the genomic context of selected AMR determinants.
8. Investigate whole-genome similarity and distance using Mash.
9. Generate figures and summary tables using Python.
10. Organize the workflow into reproducible command-line scripts.

---

## Dataset

### *Escherichia coli* K-12 MG1655

| Feature             | Information     |
| ------------------- | --------------- |
| Strain              | K-12 MG1655     |
| RefSeq assembly     | GCF_000005845.2 |
| Assembly            | ASM584v2        |
| Chromosome          | NC_000913.3     |
| Genome status       | Complete        |
| Number of replicons | 1               |

### *Escherichia coli* AR Bank #0346

| Feature             | Information                                     |
| ------------------- | ----------------------------------------------- |
| Isolate             | AR Bank #0346                                   |
| Source              | CDC & FDA Antimicrobial Resistance Isolate Bank |
| Chromosome          | CP066366.1                                      |
| Plasmid 1           | CP066367.1                                      |
| Plasmid 2           | CP066368.1                                      |
| Number of replicons | 3                                               |

---

## Bioinformatics Workflow

The analysis was performed using a command-line workflow in Linux/WSL2 with Conda-managed software.

```text
Public genome data
       │
       ▼
Genome quality assessment
       │
       ▼
Genome annotation
       │
       ▼
AMR detection
       │
       ▼
AMR classification
       │
       ├── Chromosome vs plasmid
       │
       ├── Antibiotic class
       │
       └── Comparative analysis
       │
       ▼
Genomic context analysis
       │
       ▼
Whole-genome distance analysis
       │
       ▼
Visualization and interpretation
```

### Tools

| Tool          | Purpose                             |
| ------------- | ----------------------------------- |
| Linux / WSL2  | Command-line analysis environment   |
| Conda         | Environment and software management |
| Bash          | Workflow automation                 |
| Python        | Data analysis and visualization     |
| QUAST         | Genome quality assessment           |
| Bakta         | Bacterial genome annotation         |
| AMRFinderPlus | AMR determinant detection           |
| Mash          | Whole-genome distance analysis      |

---

## Genome Quality Assessment

### K-12 MG1655

QUAST confirmed a complete single-contig reference genome:

* Genome size: 4,641,652 bp
* Number of contigs: 1
* Largest contig: 4,641,652 bp
* N50: 4,641,652 bp
* GC content: 50.79%
* Ns per 100 kb: 0

### AR Bank #0346

The AR Bank #0346 assembly contains one chromosome and two plasmids:

* Total sequence length: 4,885,435 bp
* Number of replicons: 3
* Chromosome length: 4,718,281 bp
* N50: 4,718,281 bp
* GC content: 50.68%
* Ns per 100 kb: 0

Detailed QC output is available in:

`results/qc/ar0346_quast_report.tsv`

---

## Genome Annotation

Genome annotation was performed using Bakta.

For AR Bank #0346, the annotation identified:

* 4,573 coding sequences (CDSs)
* 87 tRNAs
* 22 rRNAs
* 228 ncRNAs
* 2 CRISPR arrays
* 3 genomic replicons

Annotation outputs are provided in:

`results/annotation/`

The annotation was subsequently used to investigate the genomic context of selected AMR determinants.

---

# Antimicrobial Resistance Analysis

AMRFinderPlus was used to identify antimicrobial resistance determinants in both genomes.

Under the analysis conditions used:

* **K-12 MG1655:** 0 AMR determinants detected
* **AR Bank #0346:** 18 unique AMR determinants detected

The AR Bank #0346 isolate contained determinants associated with multiple antimicrobial classes, including:

* Aminoglycosides
* Beta-lactams
* Phenicols
* Macrolides
* Sulfonamides
* Trimethoprim
* Fosfomycin
* Colistin
* Tetracyclines

### AMR Determinants Identified in AR Bank #0346

| Gene          | Antibiotic class | Genomic location                 |
| ------------- | ---------------- | -------------------------------- |
| `aadA5`       | Aminoglycoside   | Chromosome                       |
| `aph(3'')-Ib` | Aminoglycoside   | Chromosome + plasmid             |
| `aph(6)-Id`   | Aminoglycoside   | Chromosome + plasmid             |
| `rmtB1`       | Aminoglycoside   | Plasmid CP066367.1               |
| `blaCMY-2`    | Beta-lactam      | Chromosome                       |
| `blaCTX-M-55` | Beta-lactam      | Plasmids CP066367.1 + CP066368.1 |
| `blaTEM`      | Beta-lactam      | Plasmid CP066367.1, partial hit  |
| `blaTEM-1`    | Beta-lactam      | Chromosome + plasmid             |
| `catA1`       | Phenicol         | Chromosome                       |
| `floR`        | Phenicol         | Plasmid CP066367.1               |
| `dfrA17`      | Trimethoprim     | Chromosome                       |
| `fosA3`       | Fosfomycin       | Plasmid CP066367.1               |
| `mcr-1.1`     | Colistin         | Plasmid CP066368.1               |
| `mph(A)`      | Macrolide        | Chromosome                       |
| `mrx(A)`      | Macrolide        | Chromosome                       |
| `sul1`        | Sulfonamide      | Chromosome                       |
| `sul2`        | Sulfonamide      | Chromosome + plasmid             |
| `tet(A)`      | Tetracycline     | Plasmid CP066367.1               |

---

## AMR Determinants by Antibiotic Class

| Antibiotic class | Unique determinants |
| ---------------- | ------------------: |
| Aminoglycoside   |                   4 |
| Beta-lactam      |                   4 |
| Phenicol         |                   2 |
| Macrolide        |                   2 |
| Sulfonamide      |                   2 |
| Trimethoprim     |                   1 |
| Fosfomycin       |                   1 |
| Colistin         |                   1 |
| Tetracycline     |                   1 |

Aminoglycoside and beta-lactam resistance had the highest number of unique determinants in this dataset, with four determinants detected in each class.

---

## AMR Determinants by Genomic Replicon

| Replicon              | AMR determinant occurrences |
| --------------------- | --------------------------: |
| Chromosome CP066366.1 |                          11 |
| Plasmid CP066367.1    |                          10 |
| Plasmid CP066368.1    |                           2 |

These values represent **gene-replicon occurrences rather than unique genes**. Therefore, the total number of occurrences can exceed the 18 unique AMR determinants because some determinants were detected on more than one replicon.

Across the 23 AMR gene-replicon occurrences:

* 12 (52.2%) were plasmid-associated
* 11 (47.8%) were chromosomal

Considering unique determinants, **11 of 18 (61.1%) had at least one plasmid-associated copy**.

---

## AMR Distribution by Antibiotic Class and Genomic Location

| Antibiotic class | Chromosome | Plasmid | Total |
| ---------------- | ---------: | ------: | ----: |
| Aminoglycoside   |          3 |       3 |     6 |
| Beta-lactam      |          2 |       4 |     6 |
| Colistin         |          0 |       1 |     1 |
| Fosfomycin       |          0 |       1 |     1 |
| Macrolide        |          2 |       0 |     2 |
| Phenicol         |          1 |       1 |     2 |
| Sulfonamide      |          2 |       1 |     3 |
| Tetracycline     |          0 |       1 |     1 |
| Trimethoprim     |          1 |       0 |     1 |

Plasmid-associated occurrences were particularly represented among beta-lactam and aminoglycoside determinants.

In this dataset, colistin, fosfomycin, and tetracycline determinants were detected only on plasmid replicons, while the detected macrolide and trimethoprim determinants were chromosomal.

The corresponding visualization is available at:

`results/figures/amr_class_by_location.png`

---

# Genomic Context Analysis

Genomic context analysis was performed for selected AMR determinants, with particular focus on `mcr-1.1` and `blaCTX-M-55`.

### `mcr-1.1`

The `mcr-1.1` determinant was located on plasmid CP066368.1 downstream of a region containing the mobilization-associated proteins MobC and MbeA DNA relaxase.

This genomic arrangement provides evidence of a **mobilization-associated local context**, although genomic proximity alone does not demonstrate horizontal gene transfer.

### `blaCTX-M-55`

Two copies of `blaCTX-M-55` were identified.

The copy on plasmid CP066367.1 was located within a region containing:

* `fosA3`
* `blaTEM`
* `wbuC`
* Multiple IS6-family/IS15 transposases

The second copy, located on plasmid CP066368.1, was surrounded primarily by hypothetical and other annotated proteins, without an obvious adjacent mobility-associated gene identified in the examined region.

### Genomic Context Summary

| AMR determinant | Replicon   |   Coordinates | Key genomic context                                                                    |
| --------------- | ---------- | ------------: | -------------------------------------------------------------------------------------- |
| `mcr-1.1`       | CP066368.1 | 23,493–25,118 | Downstream of `mbeA` DNA relaxase and MobC                                             |
| `blaCTX-M-55`   | CP066367.1 | 86,270–87,145 | Region containing `fosA3`, `blaTEM`, `wbuC`, and multiple IS6-family/IS15 transposases |
| `blaCTX-M-55`   | CP066368.1 |   7,385–8,260 | Region containing predominantly hypothetical/other annotated proteins                  |

These observations provide genomic-context evidence for further investigation of plasmid-associated AMR and mobile genetic elements. They should not be interpreted as direct evidence of horizontal gene transfer.

---

# Whole-Genome Distance Analysis

Whole-genome distance analysis was performed using Mash.

The resulting Mash distances were used to construct a neighbor-joining tree to visualize genomic relationships among the analyzed *E. coli* genomes.

Outputs include:

* Mash sketches
* Pairwise genomic distances
* Neighbor-joining tree
* Tree visualization

Files are available in:

`results/phylogeny/`

The resulting figure is available at:

`results/figures/ecoli_mash_neighbor_joining_tree.png`

---

# Visualization

Python scripts were used to generate figures summarizing the AMR analysis.

Available visualizations include:

* AMR determinants by antibiotic class
* AMR determinants by genomic replicon
* AMR class distribution by genomic location
* Comparative AMR profile
* Mash-based whole-genome neighbor-joining tree

Figures are available in:

`results/figures/`

---

# Key Findings

The analysis identified **18 unique AMR determinants** in AR Bank #0346 compared with **0 AMR determinants detected in K-12 MG1655** under the analysis conditions used.

The AR Bank #0346 isolate contained resistance determinants associated with nine antimicrobial classes and carried AMR determinants on both chromosomal and plasmid replicons.

A notable finding was the detection of **`mcr-1.1` on plasmid CP066368.1**, alongside `blaCTX-M-55` on the same plasmid.

Plasmid CP066367.1 also contained multiple AMR determinants, including `blaCTX-M-55`, `fosA3`, `blaTEM`, `floR`, `tet(A)`, and aminoglycoside resistance determinants.

The genomic-context analysis identified regions containing mobile-element-associated features around selected AMR determinants, providing targets for further investigation.

---

# Interpretation and Limitations

The results demonstrate that AMR in AR Bank #0346 is associated with multiple resistance determinants distributed across both chromosomal and plasmid replicons.

The analysis suggests that plasmids represent an important component of the AMR genomic landscape in this isolate, based on the presence and distribution of multiple resistance determinants.

However, several limitations should be considered:

* AMRFinderPlus detects sequence determinants associated with resistance; detection alone does not demonstrate gene expression or phenotypic resistance.
* The presence of a resistance determinant does not establish that it is actively expressed.
* Genomic proximity to mobility-associated genes does not by itself demonstrate horizontal gene transfer.
* The analysis compares two selected genomes and therefore does not represent the diversity of *E. coli* as a species.
* The Mash analysis describes genomic similarity/distance within the selected dataset and should not be interpreted as a population-scale phylogeny.
* The `blaTEM` result was classified by AMRFinderPlus as a partial hit and was therefore distinguished from the complete `blaTEM-1` determinant.

The `qacEdelta1` determinant was also detected. AMRFinderPlus classified this as a biocide/stress determinant rather than an AMR determinant, so it was excluded from the total of 18 AMR determinants.

---

# Reproducibility

The analysis was performed in a Linux/WSL2 environment using Conda-managed software.

The repository contains:

* Analysis scripts
* AMR result tables
* Genome annotation outputs
* Quality-control results
* Mash distance and tree files
* Generated figures
* Metadata
* Documentation

The main workflow can be executed using the provided Bash scripts in:

`scripts/`

---

# Skills Demonstrated

This project demonstrates practical experience with:

**Bacterial genomics**

* Whole-genome sequence analysis
* Genome annotation
* Replicon-level analysis
* Genomic context analysis

**Antimicrobial resistance**

* AMR determinant detection
* AMR classification
* Chromosomal vs plasmid localization
* Interpretation of AMR genomic context
* Mobile genetic element-associated analysis

**Bioinformatics**

* Linux / WSL2
* Bash scripting
* Conda environments
* Python data analysis
* Data visualization
* Command-line bioinformatics tools
* Reproducible workflows

**Tools**

* QUAST
* Bakta
* AMRFinderPlus
* Mash
* Python

---

# Project Status

* [x] Genome selection
* [x] Genome sequence retrieval
* [x] Genome quality assessment
* [x] Genome annotation
* [x] AMR detection
* [x] AMR classification
* [x] Replicon-level analysis
* [x] Comparative AMR analysis
* [x] AMR visualization
* [x] Genomic context analysis
* [x] Whole-genome distance analysis using Mash
* [x] Comparative interpretation of AMR genomic context

---

## Research Relevance

This project provided hands-on experience in bacterial genomics, antimicrobial resistance bioinformatics, genome annotation, command-line analysis, genomic-context interpretation, and computational data visualization.

The workflow is directly relevant to research involving bacterial genomics, antimicrobial resistance, infectious disease, pathogen genomics, and computational approaches to life-science research.

