#!/bin/bash

# Reproducible E. coli AMR comparative genomics workflow

set -e

K12="data/raw/GCF_000005845.2_ASM584v2_genomic.fna"
AR0346="data/raw/ar0346/ar0346.fna"

echo "=== E. coli AMR Comparative Genomics Workflow ==="

echo "[1/4] Genome quality assessment with QUAST..."
quast.py "$K12" -o results/qc/k12_quast
quast.py "$AR0346" -o results/qc/ar0346_quast

echo "[2/4] Genome annotation with Bakta..."
bakta "$K12" \
    --output results/annotation/k12_bakta_v3 \
    --prefix ecoli_k12 \
    --force

bakta "$AR0346" \
    --output results/annotation/ar0346_bakta \
    --prefix ecoli_ar0346 \
    --force

echo "[3/4] AMR detection with AMRFinderPlus..."
amrfinder \
    -n "$K12" \
    -o results/amr/k12_amrfinder.tsv

amrfinder \
    -n "$AR0346" \
    -o results/amr/ar0346_amrfinder.tsv

echo "[4/4] Workflow complete."

echo "Results:"
echo "  QC:         results/qc/"
echo "  Annotation: results/annotation/"
echo "  AMR:        results/amr/"

