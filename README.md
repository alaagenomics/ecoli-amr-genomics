# Comparative Genomic Analysis of Antimicrobial Resistance in *Escherichia coli*

## Project Overview

This project investigates the genomic distribution of antimicrobial resistance (AMR) determinants in *Escherichia coli* using publicly available whole-genome sequence data and bioinformatics analysis.

The project compares the reference strain *E. coli* K-12 MG1655 with *E. coli* AR Bank #0346, a multidrug-resistant isolate from the CDC & FDA Antimicrobial Resistance Isolate Bank.

The analysis focuses on identifying AMR determinants, characterizing their genomic locations, and examining their distribution between chromosomal and plasmid replicons.

## Research Question

How does the genomic distribution of antimicrobial resistance determinants differ between a reference *E. coli* strain and a multidrug-resistant *E. coli* isolate?

## Objectives

* Assess the genomic quality and structure of the selected *E. coli* genomes.
* Annotate the bacterial genomes.
* Identify antimicrobial resistance determinants using AMRFinderPlus.
* Classify AMR determinants according to antibiotic class.
* Determine whether resistance determinants are located on the chromosome or plasmids.
* Compare the genomic characteristics of the resistant isolate with the K-12 reference strain.
* Investigate the potential contribution of plasmids to the genomic distribution of antimicrobial resistance.

## Dataset

### *Escherichia coli* K-12 MG1655

* Strain: K-12 MG1655
* RefSeq assembly: GCF_000005845.2
* Assembly: ASM584v2
* Chromosome: NC_000913.3
* Genome status: Complete
* Number of replicons: 1

### *Escherichia coli* AR Bank #0346

* Isolate: AR Bank #0346
* Source: CDC & FDA Antimicrobial Resistance Isolate Bank
* Chromosome: CP066366.1
* Plasmid 1: CP066367.1
* Plasmid 2: CP066368.1
* Number of replicons: 3

## Bioinformatics Workflow

The analysis was performed using a reproducible command-line workflow:

1. Genome sequence retrieval from public databases
2. Genome quality assessment with QUAST
3. Genome annotation with Bakta
4. Antimicrobial resistance detection with AMRFinderPlus
5. Classification of AMR determinants by antibiotic class
6. Analysis of AMR determinants by genomic replicon
7. Comparative AMR analysis
8. AMR data visualization
9. Further genomic context and phylogenetic analysis

## Software and Tools

* Linux / WSL2
* Conda
* Bash
* Python
* QUAST
* Bakta
* AMRFinderPlus

## Genome Quality Assessment

### *E. coli* K-12 MG1655

QUAST analysis confirmed a complete single-contig reference genome:

* Genome size: 4,641,652 bp
* Number of contigs: 1
* Largest contig: 4,641,652 bp
* N50: 4,641,652 bp
* GC content: 50.79%
* Ns per 100 kb: 0

### *E. coli* AR Bank #0346

QUAST analysis identified three sequence replicons consisting of one chromosome and two plasmids:

* Total sequence length: 4,885,435 bp
* Number of replicons: 3
* Chromosome length: 4,718,281 bp
* N50: 4,718,281 bp
* GC content: 50.68%
* Ns per 100 kb: 0

## Genome Annotation

The genomes were annotated using Bakta.

For AR Bank #0346, the annotation identified:

* 4,573 coding sequences (CDSs)
* 87 tRNAs
* 22 rRNAs
* 228 ncRNAs
* 2 CRISPR arrays
* 3 genomic replicons

The annotation provides genomic features that support downstream analysis of AMR determinants and their genomic context.

## Antimicrobial Resistance Analysis

AMRFinderPlus was used to identify antimicrobial resistance determinants in *E. coli* K-12 MG1655 and *E. coli* AR Bank #0346.

No AMRFinderPlus antimicrobial resistance determinants were detected in the K-12 MG1655 reference genome under the analysis conditions used.

A total of **18 unique AMR determinants** were identified in AR Bank #0346.

These determinants were distributed across multiple antimicrobial classes, including aminoglycosides, beta-lactams, phenicols, macrolides, sulfonamides, trimethoprim, fosfomycin, colistin, and tetracyclines.

The AR Bank #0346 isolate contained AMR determinants on both chromosomal and plasmid replicons, with some determinants detected on more than one replicon.

### AMR Determinants

| Gene          | Antibiotic Class | Genomic Location                 |
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

## AMR Determinants by Antibiotic Class

| Antibiotic Class | Number of Unique Determinants |
| ---------------- | ----------------------------: |
| Aminoglycoside   |                             4 |
| Beta-lactam      |                             4 |
| Phenicol         |                             2 |
| Macrolide        |                             2 |
| Sulfonamide      |                             2 |
| Trimethoprim     |                             1 |
| Fosfomycin       |                             1 |
| Colistin         |                             1 |
| Tetracycline     |                             1 |

Aminoglycoside and beta-lactam resistance had the highest number of unique determinants, with four determinants identified in each class.

## AMR Determinants by Replicon

| Replicon              | AMR Determinant Occurrences |
| --------------------- | --------------------------: |
| Chromosome CP066366.1 |                          11 |
| Plasmid CP066367.1    |                          10 |
| Plasmid CP066368.1    |                           2 |

These counts represent **gene-replicon occurrences**, rather than unique genes. Therefore, the counts can exceed 18 because several AMR determinants were detected on more than one replicon.

## AMR Visualization

The analysis results were visualized to summarize:

* AMR determinants by antibiotic class
* AMR determinant occurrences by genomic replicon
* Comparison of AMR determinants between K-12 MG1655 and AR Bank #0346

Figures are available in [`results/figures/`](results/figures/).

## Key Finding

A major finding was the detection of **`mcr-1.1` on plasmid CP066368.1**.

AMRFinderPlus detected **18 unique AMR determinants** in AR Bank #0346 compared with **0 detected AMR determinants** in the K-12 MG1655 reference genome under the analysis conditions used.

The *mcr-1* family is associated with resistance to colistin, an important antimicrobial used in the treatment of infections caused by multidrug-resistant Gram-negative bacteria.

The isolate also contained resistance determinants associated with beta-lactams, aminoglycosides, sulfonamides, phenicols, macrolides, tetracyclines, trimethoprim, and fosfomycin.

Plasmid CP066367.1 carried a diverse collection of AMR determinants, while CP066368.1 carried both **`mcr-1.1`** and **`blaCTX-M-55`**.

This distribution provides a basis for further investigation of the contribution of plasmids and other mobile genetic elements to antimicrobial resistance.

## Interpretation

The results demonstrate that antimicrobial resistance in AR Bank #0346 involves multiple resistance determinants spanning several antibiotic classes.

AMR determinants were distributed across both the chromosome and plasmids, with plasmid CP066367.1 containing a particularly diverse collection of resistance determinants.

The detection of plasmid-associated **`mcr-1.1`** is particularly relevant because plasmid-mediated resistance determinants have the potential to contribute to horizontal transfer of antimicrobial resistance between bacterial populations.

Further analysis will examine the genomic context of these determinants, their association with mobile genetic elements, and their relationship to other genomic features.

## Important Analytical Notes

AMRFinderPlus identifies resistance determinants through sequence comparison against a curated antimicrobial resistance database. Detection of a resistance determinant indicates the presence of a sequence associated with resistance but does not, by itself, demonstrate gene expression or phenotypic resistance.

The AMRFinderPlus result for **`blaTEM`** was classified as a partial hit and is therefore distinguished from the complete **`blaTEM-1`** determinant.

The **`qacEdelta1`** determinant was also detected. AMRFinderPlus classified it as a biocide/stress determinant rather than an antimicrobial resistance determinant, so it was excluded from the total of 18 unique AMR determinants.

## Project Status

* [x] Genome selection
* [x] Genome sequence retrieval
* [x] Genome quality assessment
* [x] Genome annotation
* [x] AMR detection
* [x] AMR classification
* [x] Replicon-level analysis
* [x] Comparative analysis with *E. coli* K-12
* [x] AMR distribution visualization
* [ ] Genomic context analysis
* [ ] Phylogenetic analysis
* [ ] Final comparative interpretation

## Reproducibility

The analysis is being performed using command-line bioinformatics tools in a Conda-managed Linux/WSL2 environment.

The repository contains analysis results, scripts, figures, and documentation supporting reproducibility of the workflow.

## Research Relevance

This project provides practical experience in bacterial genomics, antimicrobial resistance analysis, genome annotation, command-line bioinformatics, and genomic data interpretation.

The skills developed through this project are relevant to research in bacterial genomics, antimicrobial resistance, infectious disease, biotechnology, and pharmaceutical and life-science research.
