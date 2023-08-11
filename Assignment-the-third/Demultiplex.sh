#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=compute
#SBATCH --mail-user=iquesada@uoregon.edu
#SBATCH --mail-type=ALL
#SBATCH --cpus-per-task=1
#SBATCH --mem=16GB

conda activate bgmp_py311

file1="/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz"
file2="/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz"
file3="/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz"
file4="/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz"

/usr/bin/time -v ./Demultiplex.py -f1 $file1 -f2 $file2 -f3 $file3 -f4 $file4
