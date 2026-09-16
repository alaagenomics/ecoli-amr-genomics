#!/bin/bash

# AMRFinderPlus analysis of E. coli K-12 MG1655 and AR Bank #0346

set -e

amrfinder \
  -n data/raw/GCF_000005845.2_ASM584v2_genomic.fna \
  -o results/amr/k12_amrfinder.tsv

amrfinder \
  -n data/raw/ar0346/ar0346.fna \
  -o results/amr/ar0346_amrfinder.tsv
