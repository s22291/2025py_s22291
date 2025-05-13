import random

length = int(input("Enter the sequence length: "))
id = input("Enter the sequence ID: ")
description = input("Provide a description of the sequence: ")
name = input("Enter your name: ")

sequence = []
a_count =0
c_count =0
t_count =0
g_count =0

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
a_perc = a_count/len(sequence) * 100
c_perc =c_count/len(sequence) * 100
t_perc =t_count/len(sequence) * 100
g_perc =g_count/len(sequence) * 100
gc_cont = (c_count+g_count)/(t_count+a_count)*100

sequence.insert(random.randint(0,len(sequence)),name)
sequence = "".join(sequence)

f=open(id+".fasta","w")
fasta_content = "> "+id+ " " + description + "\n" + sequence
f.write(fasta_content)

print("Sequence statistics\n"
      f"A: {a_perc:.1f}\n"
      f"C: {c_perc:.1f}\n"
      f"T: {t_perc:.1f}\n"
      f"G: {g_perc:.1f}\n"
      f"%GC: {gc_cont:.1f}"
      )