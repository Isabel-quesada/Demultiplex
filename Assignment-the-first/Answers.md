# Assignment the First

## Part 1
1. Be sure to upload your Python script. Provide a link to it here: /projects/bgmp/iquesada/bioinfo/Bi622/Demultiplex/Assignment-the-first/part1.py

| File name | label | Read length | Phred encoding |
|---|---|---|---|
| 1294_S1_L008_R1_001.fastq.gz | read 1 | 101 | Phred 33 |
| 1294_S1_L008_R2_001.fastq.gz | index 1 | 8 | Phred 33 |
| 1294_S1_L008_R3_001.fastq.gz | index 2 | 8 | Phred 33 |
| 1294_S1_L008_R4_001.fastq.gz | read 2 | 101 | Phred 33 |

2. Per-base NT distribution
    i. Use markdown to insert your 4 histograms here.
       ![https://github.com/Isabel-quesada/Demultiplex/blob/master/Assignment-the-first/R1_histogram.png](R1_histogram)
       ![https://github.com/Isabel-quesada/Demultiplex/blob/master/Assignment-the-first/R2_histogram.png](R2_histogram)
       ![https://github.com/Isabel-quesada/Demultiplex/blob/master/Assignment-the-first/R3_histogram.png](R3 histogram)
       ![https://github.com/Isabel-quesada/Demultiplex/blob/master/Assignment-the-first/R4_histogram.png](R4 histogram)
   
   ii. Q30 is a good quality score cutoff for biological read pairs because the probability of an incorrect base is very low (1 in 1000).          The average quality scores per base position were higher than Q30. For index reads it might be better to use a lower quality score          cutoff, maybe around Q20. Since the length of index reads are only 8bp we do not need as low of a probability of an incorrect base          when compared to the biological reads. 
  iii. index1 (R2): 3976613
       zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz | grep -A 1 ^"@" | grep -v ^"@" | grep -v ^"--" | grep -c "N"

       index2 (R3): 3328051
       zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz | grep -A 1 ^"@" | grep -v ^"@" | grep -v ^"--" | grep -c "N"
       
## Part 2
1. Define the problem
2. Describe output
3. Upload your [4 input FASTQ files](../TEST-input_FASTQ) and your [>=6 expected output FASTQ files](../TEST-output_FASTQ).
4. Pseudocode
5. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement
