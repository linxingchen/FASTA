# this script is for the rename of fasta sequence header,
# with three input files, the first one has two columns (old
# name \t new name), the second one is fasta file, and the
# renamed fasta file.

import sys
from Bio import SeqIO

# old name - new name dictionary
name_dict = {}

name = open(sys.argv[1], 'r')
for line in name:
    line = line.strip()
    line = line.split('\t')
    name_dict[line[0]] = line[1]

name.close()

# header and sequence dictionary
fasta_dict = {}
fasta = open(sys.argv[2], 'r')
for line in SeqIO.parse(fasta, 'fasta'):
    header = str(line.id).strip()
    seq = str(line.seq).strip()
    fasta_dict[header] = seq

fasta.close()

# writing renamed fasta file
out = open(sys.argv[3], 'w')

for key in name_dict.keys():
    if key in fasta_dict.keys():
        out.write(">" + name_dict[key] + "\n")
        out.write(fasta_dict[key] + '\n')
