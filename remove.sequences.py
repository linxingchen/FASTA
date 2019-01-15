
import sys
from Bio import SeqIO


# Function to check if a nucleotide sequence contains other element excluding A, T, C, G.
def check_dna(dna):
    bp = list()
    for letter in dna:
        bp.append(letter)
        return set(dna) <= {'A', 'T', 'C', 'G', 'N'}


# header and sequence dictionary
fasta_dict = {}
fasta = open(sys.argv[1], 'r')
for line in SeqIO.parse(fasta, 'fasta'):
    header = str(line.id).strip()
    seq = str(line.seq).strip()
    fasta_dict[header] = seq

fasta.close()


# remove target = rt
my_rt = open(sys.argv[2], 'r')

target_id = []

for line in my_rt:
    if line.startswith('>'):
        line = line.strip().split('>')
        target_id.append(line[1])
    elif check_dna(line.strip()):
        pass
    else:
        line = line.strip().split()
        target_id.append(line[0])


# write not removed sequence in fasta format
output = open(sys.argv[3], 'w')

removed_id = list()
not_found_target = list()

for item in target_id:
    if item in fasta_dict.keys():
        removed_id.append(item)
    else:
        not_found_target.append(item)

for scaffold in fasta_dict.keys():
    if scaffold not in target_id:
        print(">" + scaffold, file=output)
        print(fasta_dict[scaffold], file=output)


# print a summary on the screen
print('')
print("*********************************************************************************")
print("Done! " + str(len(set(removed_id))) + " non-redundant targets have been removed!")

if len(not_found_target) > 0:
    print("Note: " + str(len(not_found_target)) +
          " non-redundant targets could not been found in the input fasta file!")

print("*********************************************************************************")
print('')
