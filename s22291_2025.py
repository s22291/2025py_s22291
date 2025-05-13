# This program generates a random DNA sequence in FASTA format.
# It calculates the percentage of each nucleotide and the CG/AT ratio.
# The sequence includes a user name inserted randomly (excluded from stats).
# Results are saved to a .fasta file with the proper header format.
 
 
import random
 
# Ask the user for the DNA sequence length
length = int(input("Enter the sequence length: "))
 
# Ask the user for the ID
id = input("Enter the sequence ID: ")
 
# Ask the user for the description
description = input("Provide a description of the sequence: ")
 
# Ask the user for the name
name = input("Enter your name: ")
 
sequence = []
a_count =0
c_count =0
t_count =0
g_count =0
 
# Loop for generating random DNA sequence and counting nucleotide statistics
for i in range(length):
    nuc=random.choice(["A","C","T","G"])
    if nuc=='A':
        a_count+=1
    elif nuc=='C':
        c_count+=1
    elif nuc=='T':
        t_count+=1
    else:
        g_count+=1
    sequence.append(nuc)
 
# Calculating nuclueotide statistics
a_perc = a_count/len(sequence) * 100
c_perc =c_count/len(sequence) * 100
t_perc =t_count/len(sequence) * 100
g_perc =g_count/len(sequence) * 100
gc_cont = (c_count+g_count)/(t_count+a_count)*100
 
#Adding the name randomly in the sequence
sequence.insert(random.randint(0,len(sequence)),name)
 
#Joining the whole sequence as a string
sequence = "".join(sequence)
 
# Open a new FASTA file named after the sequence ID for writing
# Original
#f=open(id+".fasta","w")
# Modified, added encoding for better compatibility across systems
f = open(id + ".fasta", "w", encoding="utf-8")
 
# Then create the FASTA-format content: header line with ID and description, and the DNA sequence
# ORIGINAL:
# str = "> " + id + " " + description + "\n" + sequence
# MODIFIED (renamed to avoid overwriting Python keyword and for clarity):
fasta_content = "> " + id + " " + description + "\n" + sequence
 
#Saving the file
f.write(fasta_content)
 
#Printing sequence statistics
# ORIGINAL:
# print("A:", a_perc)
# MODIFIED (formatted output to show percentage with 1 decimal for cleaner display):
print("Sequence statistics\n"
      f"A: {a_perc:.1f}\n"
      f"C: {c_perc:.1f}\n"
      f"T: {t_perc:.1f}\n"
      f"G: {g_perc:.1f}\n"
      f"%GC: {gc_cont:.1f}"
      )
 