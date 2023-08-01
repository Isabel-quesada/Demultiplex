#!/usr/bin/env python


import gzip
import argparse
import bioinfo
import matplotlib.pyplot as plt

def get_args(): 
    parser = argparse.ArgumentParser(description="Setting global variables")
    parser.add_argument("-f", "--file_name", help="to specify the filename", type = str, required=True)
    parser.add_argument("-l", "--read_length", help="to specifiy the read length", type = int, required=True)
    parser.add_argument("-o", "--output", help="to specifiy the filename for the plot")
    return parser.parse_args()

# set global variables
args = get_args()
file_name = args.file_name
read_length = args.read_length
output = args.output

quality_scores: list = [0]*read_length #generate an empty list


# with gzip.open(file_name, mode='rt') as fh: 
with gzip.open(file_name, "rt") as fh: 
    num_lines = 0
    for line in fh: 
        num_lines+=1 #add one to the counter as it reads each line in the file
        line=line.strip('\n')
        if num_lines%4 == 0: #quality score line
            for base, char in enumerate(line): 
                quality_scores[base]+=bioinfo.convert_phred(char)

num_records = int(num_lines/4) #calculate the number of records in the file

for i in range(len(quality_scores)): 
    quality_scores[i] = quality_scores[i]/num_records #calculate the mean quality score at each base
    # print(f"{i}\t{quality_scores[i]}") #print base pair 'tab' mean quality score


plt.bar(range(read_length), quality_scores)
plt.xlabel("Base Position")
plt.ylabel("Mean Quality Score")
plt.title("Mean qscore at each base")
plt.savefig(output)