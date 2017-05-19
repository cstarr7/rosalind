# -*- coding: utf-8 -*-
# @Author: Charles Starr
# @Date:   2017-05-18 22:03:44
# @Last Modified by:   Charles Starr
# @Last Modified time: 2017-05-18 22:14:17


def transcribe(file):

	template = open(file, 'r')

	rna = ''

	for dna in template.read():
		if dna == 'T':
			rna += 'U'
		else:
			rna += dna

	transcript = open('transcript.txt', 'w')

	transcript.write(rna)

transcribe('rosalind_rna.txt')
