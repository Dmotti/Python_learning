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
print "A: %.1f" % (100 * NumberA / SeqLength)
print "C: %.1f" % (100 * NumberC / SeqLength)
print "G: %.1f" % (100 * NumberG / SeqLength)
print "T: %.1f" % (100 * NumberT / SeqLength)

# Calculating primer melting points with different formulas by length

TotalStrong = NumberG + NumberC
TotalWeak = NumberA + NumberT

if SeqLength >= 14:
	#formula for sequences > 14 nucleotides long
	MeltTempLong = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
	print "Tm Long (>14): %.1f C" % (MeltTempLong)
else:
	#formula for sequences less than 14 nucleotides long
	MeltTemp = (4 * TotalStrong) + (2 * TotalWeak)
	print "Tm Short: %.1f C" % (MeltTemp)
