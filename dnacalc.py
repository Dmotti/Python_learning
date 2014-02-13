#! /usr/bin/env python
# This program takes a DNA sequence (without checking)
# and shows its length and the nucleotide composition

DNASeq = "ATGTCTCATTCAAAGCA"
# DNASeq = raw.input("Enter a sequence: ")
DNASeq = DNASeq.upper() # convert to uppercase for .count() function
DNASeq = DNASeq.replace(" ","") # remove spaces

print 'Sequence:', DNASeq

# below are nested functions: first find the length, then make it float
SeqLength = float(len(DNASeq))

# SeqLength = (len(DNASeq))
print "Sequence Length: ", SeqLength

NumberA = DNASeq.count('A')
NumberC = DNASeq.count('C')
NumberG = DNASeq.count('G')
NumberT = DNASeq.count('T')
# Calculate percentage and output to 1 decimal

