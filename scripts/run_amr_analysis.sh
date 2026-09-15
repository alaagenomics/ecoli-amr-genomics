#!/bin/bash
# AMRFinderPlus analysis of E. coli AR Bank #0346
INPUT="data/raw/ar0346/ar0346.fna"
OUTPUT="results/amr/ar0346_amrfinder.tsv"
amrfinder -n "$INPUT" -o "$OUTPUT"
