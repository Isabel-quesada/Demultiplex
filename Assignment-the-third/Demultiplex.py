#!/usr/bin/env python

import argparse
import gzip


def get_args(): 
    parser = argparse.ArgumentParser(description="Setting global variables")
    parser.add_argument("-f1", "--file1", help="to specify the filename", type = str, required=True)
    parser.add_argument("-f2", "--file2", help="to specify the filename", type = str, required=True)
    parser.add_argument("-f3", "--file3", help="to specify the filename", type = str, required=True)
    parser.add_argument("-f4", "--file4", help="to specify the filename", type = str, required=True)
    return parser.parse_args()

# set variables for input files
args = get_args()
file1 = args.file1
file2 = args.file2
file3 = args.file3
file4 = args.file4

#test files
# file1 = "/projects/bgmp/iquesada/bioinfo/Bi622/Demultiplex/TEST-input_FASTQ/test_R1.fastq"
# file2 = "/projects/bgmp/iquesada/bioinfo/Bi622/Demultiplex/TEST-input_FASTQ/test_R2.fastq"
# file3 = "/projects/bgmp/iquesada/bioinfo/Bi622/Demultiplex/TEST-input_FASTQ/test_R3.fastq"
# file4 = "/projects/bgmp/iquesada/bioinfo/Bi622/Demultiplex/TEST-input_FASTQ/test_R4.fastq"

#files to run
# file1 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz"
# file2 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz"
# file3 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz"
# file4 = "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz"

#creating lists of empty strings to store one record in each file in the while True loop
R1_rec = ["","","",""]
R2_rec = ["","","",""]
R3_rec = ["","","",""]
R4_rec = ["","","",""]

#initializing empty dictionaires to serve as a counter for number of occurrences
matched_dict = {}
hopped_dict = {}
unknown_total = 0
total_records = 0

#creating a list of all 24 indexes used for sequencing
index_file = "/projects/bgmp/shared/2017_sequencing/indexes.txt"
with open(index_file, "r") as fh: 
    indexes=[]
    i = 0
    for line in fh: 
        i+=1
        line=line.strip()
        if i>1: 
            indexes.append(line.split('\t')[4])

def rev_comp(seq) -> str: 
    '''Returns the reverse compliment of the sequence line'''
    comp_base = {"A": "T", "a":"T", "T": "A", "t":"A", "G":"C", "g":"C", "C":"G", "c":"G", "N":"N", "n":"N"}
    rev_comp_seq = ""
    rev_seq = seq[::-1] #reverse the order of the string
    for base in rev_seq: 
        rev_comp_seq+=comp_base[base]
    return rev_comp_seq

# creating a dictionary that will hold output files. Loop through indexes list and create 2 files per index. Output 48 *.fq files
output_files = {}
for index in indexes: 
    fh1 = open(index + "_R1.fq","w")
    fh2 = open(index + "_R2.fq","w")
    output_files[index]=[fh1,fh2]
# opening 4 files as write
ur1 = open("unknown_R1.fq", "w")
ur2 = open("unknown_R2.fq", "w")
hr1 = open("hopped_R1.fq", "w")
hr2 = open("hopped_R2.fq", "w")

with (gzip.open(file1, "rt") as R1, gzip.open(file2, "rt") as R2, gzip.open(file3, "rt") as R3, gzip.open(file4, "rt") as R4): 
    while True: 
        R1_rec[0] = R1.readline().strip()
        if R1_rec[0] == "": 
            #EOF
            break
        R1_rec[1] = R1.readline().strip()
        R1_rec[2] = R1.readline().strip()
        R1_rec[3] = R1.readline().strip()
        R1_header = R1_rec[0]

        R2_rec[0] = R2.readline().strip()
        R2_rec[1] = R2.readline().strip()
        R2_rec[2] = R2.readline().strip()
        R2_rec[3] = R2.readline().strip()
        index1 = R2_rec[1].upper() #setting this variable for readability

        R3_rec[0] = R3.readline().strip()
        R3_rec[1] = R3.readline().strip()
        R3_rec[2] = R3.readline().strip()
        R3_rec[3] = R3.readline().strip()
        index2_rev = rev_comp(R3_rec[1]).upper() #setting this variable for readability

        R4_rec[0] = R4.readline().strip()
        R4_rec[1] = R4.readline().strip()
        R4_rec[2] = R4.readline().strip()
        R4_rec[3] = R4.readline().strip()
        R4_header = R4_rec[0]

        #alternate way to readline(): 
        # r3_header = R3.readline().strip()
        # r3_seq = R3.readline().strip()
        # r3_plus = R3.readline().strip()
        # r3_qual = R3.readline().strip()

        # r4_header = R4.readline().strip()
        # r4_seq = R4.readline().strip()
        # r4_plus = R4.readline().strip()
        # r4_qual = R4.readline().strip()

        new_header_R1 = R1_header + "_" + index1 + "-" + index2_rev
        new_header_R4 = R4_header + "_" + index1 + "-" + index2_rev

        # checking for unknown and if the indexes are in the known index list
        if "N" in index1 or "N" in index2_rev or index1 not in indexes or index2_rev not in indexes:
            ur1.write(new_header_R1 + '\n' + R1_rec[1] + '\n' + R1_rec[2] + '\n' + R1_rec[3] + '\n')
            ur2.write(new_header_R4 + '\n' + R4_rec[1] + '\n' + R4_rec[2] + '\n' + R4_rec[3] + '\n')
            unknown_total+=1
        # checking if indexes matched
        elif index1==index2_rev: 
            output_files[index1][0].write(new_header_R1 + '\n' + R1_rec[1] + '\n' + R1_rec[2] + '\n' + R1_rec[3] + '\n')
            output_files[index1][1].write(new_header_R4 + '\n' + R1_rec[1] + '\n' + R1_rec[2] + '\n' + R1_rec[3] + '\n')
            key = index1
            if key not in matched_dict: 
                matched_dict[key]=1
            else: 
                matched_dict[key]+=1
        # R2 and R3 are unmatched (index-hopped)
        elif index1 != index2_rev:
            hr1.write(new_header_R1 + '\n' + R1_rec[1] + '\n' + R1_rec[2] + '\n' + R1_rec[3] + '\n')
            hr2.write(new_header_R4 + '\n' + R4_rec[1] + '\n' + R4_rec[2] + '\n' + R4_rec[3] + '\n')
            key = index1 + "-" + index2_rev
            if key not in hopped_dict: 
                hopped_dict[key]=1
            else: 
                hopped_dict[key]+=1
        else:
            raise Exception("Impossible") 

        total_records+=1 #counter for the number of records (samples)
        #re-set the lists back to empty strings
        R1_rec = ["","","",""]
        R2_rec = ["","","",""]
        R3_rec = ["","","",""]
        R4_rec = ["","","",""]
        

#sum the total number of occurrences for each situation to use later when calculating the overall percentages
matched_occurrences = matched_dict.values()
total_matched = sum(matched_occurrences)

hopped_occurrences = hopped_dict.values()
total_hopped = sum(hopped_occurrences)


#creating the output file that contains the data for matched indexes. Includes index, number of occurrences, and percentage of reads. 
with open("matched_output.tsv", "w") as file: 
    file.write("Matched Indexes" + "\t" + "Number of Occurrences" +"\t"+ "Percentage of Reads" + "\n")
    for i in matched_dict: 
        percent_reads = (matched_dict[i]/total_records) * 100
        file.write(i + "\t" + str(matched_dict[i]) + "\t" + str(percent_reads) + "%" + "\n")

# with open("matched_output.tsv") as temp: 
#     print(temp.read())


#creating the output file that contains the data for hopped indexes. Includes hopped index-pair, number of occurrences, and percentage of reads. 
with open("hopped_output.tsv", "w") as file: 
    file.write("Hopped Index-Pair" + "\t" + "Number of Occurrences" +"\t"+ "Percentage of Reads" + "\n")
    for i in hopped_dict: 
        percent_reads = (hopped_dict[i]/total_records) * 100
        file.write(i + "\t" + str(hopped_dict[i]) + "\t" + str(percent_reads) + "%" + "\n")
# with open("hopped_output.tsv") as temp: 
#     print(temp.read())

#creating the output file that contains the overall data for hopped, unknown, and matched.
with open("overall_output.tsv", "w") as file: 
    percent_matched = (total_matched/total_records)*100
    percent_hopped = (total_hopped/total_records)*100
    percent_unknown = (unknown_total/total_records)*100
    file.write("Overall Amount" + "\n" + "Matched" + "\t" + str(percent_matched) + "%" + "\n" + "Hopped" + "\t" + str(percent_hopped) + "%" + "\n" + "Unknown" + "\t" + str(percent_unknown) + "%")
# with open("overall_output.tsv") as temp: 
#     print(temp.read())
