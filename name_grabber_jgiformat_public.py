
## Before you begin:
# This is a python script. You'll need to know a bit of python to edit it for your purposes. The comments ('#') should help guide you.
# If you have BLAST results from JGI in plain text format, you can use this script to "grab" a list of the species names.
# The script will output a text file with the names of your genes in a standardized format (Genus_species_ID).
# It is not foolproof! Check your results and use at your own risk.
#IMPORTANT NOTE: This script will not grab species designations. Species with three-word names will cause problems.
# It is not very elegant! We are casual coders. Edit at will, make it better, and share your awesome improvements.
# Run the script by typing 'python name_grabber_jgiformat_public.py' at the command prompt.
#Important note: This script works only with JGI-format FASTA amino acid sequence files

# Within the first set of quotes below (seqfiles), put the name of your FASTA file. 
# They must be in FASTA format. They may be aligned or unaligned.

seqfiles = open('fastafile.fa', 'r')

#The code below creates an output file to store the sequence names.
#You can rename the output file as needed; it is in the first set of quotes.

output_namefile = open('outputnames.txt', 'w')
output_fastafile = open('outputfasta.fa', 'w')

# The function below (sequence_splitter) will create a list of lists
# Each sub-list will be a list of lines,
# The first line being the naming line.

def sequence_splitter(seqfiles):
	list_of_seqlists = []
	for line in seqfiles:
		if '>' in line:
			indseqlist = []
			indseqlist.append(line)
		if '>' not in line:
			indseqlist.append(line)
		if '>' in line and indseqlist != []:
			list_of_seqlists.append(indseqlist)
	return list_of_seqlists


# The function below (indseq_list)  will take each sequence list from the list of lists
# and turn it into a single two-element list.
# The first element will be a string with organism and gene names.
# The second element will be a list of individual amino acids.

def indseq_list(list_of_seqs, seq_index):

        # grab the desired sequence
	starter_sequence = list_of_seqs[seq_index]

        # turn the lines into a list of amino acids
	number_of_lines = len(starter_sequence)
	counter = 1
	seq_list = []
	while counter < number_of_lines:
		stripped_line = starter_sequence[counter].rstrip('\n')
		line_list = list(stripped_line)
		seq_list = seq_list + line_list
		counter = counter + 1

        # The code below reads the name line
	# It splits the name line into its own list, separating strings at spaces.
	# It returns a shortened sequence name
	# including the organism name and gene id (from JGI).
 
	name_line_list = starter_sequence[0].split(' ')
	name_count = 0
	gene_code = name_line_list[0].lstrip('>')
	org_genus = "null"	
	org_species = "null"
	for n in name_line_list:
		if '[' in n:	
			org_genus = name_line_list[name_count].lstrip('[')
			org_species = name_line_list[name_count+1]
		name_count = name_count + 1
	indexcounter = 0

	output_namefile.write(org_genus)
	output_namefile.write(' ')
	output_namefile.write(org_species)
	output_namefile.write(', ')
	output_namefile.write(gene_code)
	output_namefile.write('\n')
	
	seq_name = '_' + org_genus + '_' + org_species + '_' + gene_code
	name_and_seq_list = [seq_name, seq_list]

	output_fastafile.write('>')
	output_fastafile.write(seq_name)
	output_fastafile.write('\n')
	for aa in seq_list:
		output_fastafile.write(aa)
	output_fastafile.write('\n')
	output_fastafile.write('\n')

	return name_and_seq_list

## The code below calls the functions to parse the FASTA file into a dictionary
# First, the 'sequence_splitter' function prepares the data.
# Then, the ind_seq_list function shortens the sequence name and builds a dictionary.
# This dictionary is not used in this code; calling the function, though, causes the writing of the output files.
# you may repurpose the dictionry as needed.

full_seq_list = sequence_splitter(seqfiles)

seq_dictionary = {}
number_of_sequences = len(full_seq_list)
seq_counter = 0
while seq_counter < number_of_sequences:
        seq_name_aa_list = indseq_list(full_seq_list,seq_counter)
        seq_dictionary[seq_name_aa_list[0]] = seq_name_aa_list[1]
        seq_counter = seq_counter + 1


