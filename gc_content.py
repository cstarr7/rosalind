# -*- coding: utf-8 -*-
# @Author: Charles Starr
# @Date:   2017-05-21 15:06:01
# @Last Modified by:   Charles Starr
# @Last Modified time: 2017-05-21 15:16:53

def get_strings(file):

	fasta = open(file, 'r')

	gc_dic = {}

	for line in fasta:
		print line
		if line[0] == '>':
			gc_dic[line[1:]] = 0.0
			string = fasta.readline()
			print string


get_strings('test.txt')