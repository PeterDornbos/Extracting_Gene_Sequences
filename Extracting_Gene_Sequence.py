#########################################################################################
# Filename: 	Extracting_Ahr_GeneSequence.py
# Written by: 	Peter Dornbos
#				Graduate Assistant				
#				Integrative Toxicology Program
#				Department of Biochemistry & Molecular Biology
#				Michigan State University
#
# Prepared: 	June 2, 2016
#
# Purpose: Pulling the Ahr gene sequence out 
#########################################################################################

import csv as csv
import sys
import subprocess
import os


with open('chromosome12', 'rU') as data_a: #open .txt file containing chromosome12 and count lines
	 lines_a = sum(1 for _ in data_a) 
data_a.close()

line_a = []


with open('chromosome12', 'rU') as file1: #set file to append the nucleotides as a list
		data = csv.reader(file1, delimiter='\t')
		for row in data:
				line_a.append(row[0])
				
							
with open('a.txt', 'w') as file_a: #write a temporary file with nucleotides as list in range of the lines counted in the first block of code
	for a in range (1,lines_a):
		file_a.write(line_a[a])

aa = []

with open('a.txt', 'rU') as aaa: #read temp file
	aa = aaa.readlines()

aaaa = str(aa[0]) #define new variable as string containing all nucleotides in the chromosome as a vertical list (i.e. row 1 = first nucleotide in chromosome, etc. )


with open('Ahr_Gene_Sequence.txt', 'w') as outfile1: #Output the sequence within a specified range at a .txt file 
	for a in range (34497979,36534989): 			 #Set a conservative range to be sure the proper gene is included
				outfile1.write(aaaa[a])
				
			

os.remove('a.txt') #remove temp file from directory



 					

 					
 					