# -*- coding: utf-8 -*-
# @Author: Charles Starr
# @Date:   2017-05-21 15:06:01
# @Last Modified by:   Charles Starr
# @Last Modified time: 2017-05-21 15:36:12

def get_strings(file):
#separates the strings from the file and sends them for counting
	fasta = open(file, 'r')

	gc_dic = {}
	
	string_name = ''
	string_sequence = ''
	
	for line in fasta:
		if line[0] == '>':
			if string_name:
				gc_dic[string_name] = gc_content(string_sequence)
				string_sequence = ''
				
			string_name = line[1:]
		else:
			string_sequence += line.rstrip()

	gc_dic[string_name] = gc_content(string_sequence)

	print gc_dic

def gc_content(sequence):
#counts number of GC bases and returns fraction of total
	total_bases = float(len(sequence))
	gc_bases = 0

	for base in sequence:
		if base in 'GC':
			gc_bases += 1

	return gc_bases/total_bases

get_strings('rosalind_gc.txt')