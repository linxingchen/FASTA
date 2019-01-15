# By providing a one-column list of sequence ID (with or without ">") and a .fasta/.fas/.fa file with sequences
# inside, this script could extract the listed sequences, and report summary information.


import sys
from Bio import SeqIO
import os

# target dictionary
target_id = list()

my_target = open(sys.argv[1], 'r')
for line in my_target:
    if line.startswith('>'):
        line_1 = line.strip().split('>')
        target_id.append(line_1[1])
    elif line.startswith('>') is False:
        line_2 = line.strip()
        target_id.append(line_2)

my_target.close()

# header and sequence dictionary
fasta_dict = {}
fasta = open(sys.argv[2], 'r')
for line in SeqIO.parse(fasta, 'fasta'):
    header = str(line.id).strip()
    seq = str(line.seq).strip()
    fasta_dict[header] = seq

fasta.close()

# print the targeted sequence in fasta format
total = list()
target_fasta = open(sys.argv[3], 'w+')
for scaffold in fasta_dict.keys():
    if scaffold in target_id:
        total.append(scaffold)
        print(">" + scaffold, file=target_fasta)
        print(fasta_dict[scaffold], file=target_fasta)

target_fasta.close()

# print summary information to the screen
not_found = open('Targets_not_retrieved.txt', 'w')
print("The sequence / These sequences could not be found in the input .fasta/.fas/.fa file", file=not_found)
print("************************************************************************************************************")
print("Done! You have " + str(len(target_id)-len(set(target_id))) + " replicate targets!")
print("You retrieved " + str(len(total)) + " out of " + str(len(set(target_id))) + " non-replicate targets!")


# print information of not extracted ones if detected
no = []
for seq in set(target_id):
    if seq not in fasta_dict.keys():
        print(seq, file=not_found)
        no.append(seq)

if len(no) > 0:
    print("Check 'Targets_not_retrieved.txt' for not retrieved ones.")
    not_found.close()
else:
    os.system('rm Targets_not_retrieved.txt')

print("************************************************************************************************************")
