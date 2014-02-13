#! /usr/bin/env python
# This program takes a DNA sequence (without checking)
# and shows its length and the nucleotide composition

DNASeq = "ATGTCTCATTCAAAGCA"
# DNASeq = raw.input("Enter a sequence: ")
DNASeq = DNASeq.upper() # convert to uppercase for .count() function
DNASeq = DNASeq.replace(" ","") # remove spaces

print 'Sequence:', DNASeq


