from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import os
import csv
import glob
import sys
def translate (seq,frame):
	seqf=""
	
	if frame==1:
		
		seqf=seq
	
	
	
	if frame==2:
	
		seqf=seq[1:]
	
	
	if frame==3:
		seqf=seq[2:]
	
	
	
	if frame==-1:
	
		seqf=seq.reverse_complement()
	
	
	if frame == -2:
		seqf=seq.reverse_complement()[1:]
	
	
	
	if frame==-3:
		seqf=seq.reverse_complement()[2:]
	
	if len(seqf)%3:
		mod=len(seqf)%3
		seqf=seqf[:-mod]

	return seqf.translate()



dico={}
listeframe=[1,2,3]



			

with open(sys.argv[1],'w') as out_file:
	for seq_record in SeqIO.parse(sys.argv[2], "fasta"):
				for iter in listeframe:	
					tempo=translate(seq_record.seq,iter)
					iter2=0
					#tempo=tempo.replace("X","*")
					for elem in tempo.split("*"):
						if len(elem) > 7:
							iter2+=1
						
							seq_record2=SeqRecord(elem,id=seq_record.id.split(" ")[0]+"_"+str(iter)+"_ORF"+str(iter2),description=seq_record.id.split(" ")[0]+"_"+str(iter)+"_ORF"+str(iter2),name=seq_record.id.split(" ")[0]+"_"+str(iter)+"_ORF"+str(iter2))
							out_file.write(seq_record2.format("fasta"))
							print seq_record2

