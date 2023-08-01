import gzip #opens zipped file


def rev_comp(str) -> str: 
    '''Returns the reverse compliment of the sequence line'''
        reverse line 
        create a dictionary and use it to get rev comp 
    return rev comp 
Input: 'AGCT'
Expected output: 'TCGA'

def append_index(str) -> str: 
    '''Adds both index sequences (R2-R3) to the header and returns this str as new_header'''
    open all files for reading #R1,R2,R3,R4
    while True: 
        get header
        get seq 
        new_header_R1 = header(R1) + R2 seq + "-" + R3 rev comp seq
        new_header_R4 = header(R4) + R2 seq + "-" + R3 rev comp seq
    return new_header_R1, new_header_R4
Input: '@header'
Expected output: '@headerAGCT-TCGA'

with open(R1, R2, R3, R4), open files to write(matched,unmatched,unknown) 
    while True: 
        if EOF is an empty string 
            break
        get header
        get seq (for R3 call rev_comp; seq=rev_comp(R3))
        get +
        get qual score 
        seq=rev_comp(R3)

        #checking for unknown
        if seq in R2 or R3 has "N": 
            call append_index 
            unknown_R1.write(record(R1))
            unknown_R4.write(record(R4))

        #create a dict containing all 24 indexes
        #checking if the indexes matched and if the index is in the dictionary.
        elif seq R2==R3 and seq R2 in dict(): 
            call append_index
            write R1 and R4 into file named matched_(index)
        
        #R2 and R3 are unmatched
        else:  
            call append_index
            unmatched.write(record(R1))
            unmatched.write(record(R4))


