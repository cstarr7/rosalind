# -*- coding: utf-8 -*-
# @Author: Charles Starr
# @Date:   2017-05-17 23:04:47
# @Last Modified by:   Charles Starr
# @Last Modified time: 2017-05-17 23:51:34

def count_bases(filename):
#opens a textfile with a dna string and counts the bases
	f = open(filename, 'r')

	bases = {'A':0, 'C':0, 'G':0, 'T':0}

	for base in f.read():
		if base in 'ATCG':
			bases[base] += 1

	print bases


count_bases('rosalind_dna.txt')