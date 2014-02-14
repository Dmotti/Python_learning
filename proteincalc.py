#! /usr/bin/env python

AminoDict={
'A':8,
'R':1,
'N':1,
'D':1,
'C':1,
'Q':1,
'E':1,
'G':7,
'H':1,
'I':1,
'L':1,
'K':1,
'M':1,
'F':1,
'P':1,
'S':1,
'T':1,
'W':2,
'Y':1,
'V':1,
'X':0,
'-':0,
'*':0,
}

ProteinSeq = "FDILSATFTYGNR"
for AminoAcid in ProteinSeq:
	print AminoAcid
