#charles
#5/18/2017

def reverse_transcribe(file):
#takes a DNA sequence and outputs the reverse compliment
	template = open(file, 'r')

	complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G', '\n':''}

	reverse_complement = ''

	for base in template.read()[::-1]:
		reverse_complement += complements[base]

	outfile = open('reverse_complement.txt', 'w')

	outfile.write(reverse_complement)

reverse_transcribe('rosalind_revc.txt')
