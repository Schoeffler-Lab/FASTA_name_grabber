# FASTA_name_grabber
Re-format the headers of FASTA files of amino acid sequences; return reformatted FASTA and a formatted list of names and gene IDs


This python script will take a FASTA format set of amino acid sequences with headers in JGI format. It will re-format the headers as follows:

>Genus_species_geneID

It will return a FASTA format file with the re-formatted headers and a list of species names and gene IDs.

To use this script:
1) Edit the name of the FASTA file (the input file).
2) Edit the name of the output file with the list of names.
3) Edit the name of the output FASTA file
4) Run as follows, via the command line: >python name_grabber_jgiformat_public.py

KNOWN ISSUES:
1) We're casual coders. This script is not perfect or elegant, but you can edit it at will to make it so. 
2) If the species name contains three separate words, the script only returns the first two. This can be an issue for some species. 
3) If the header lists the scaffold designation before the species name, the script returns the scaffold designation before the species name.

Script author:
Allyn Schoeffler, Ph.D.
Assistant Professor
Department of Chemistry & Biochemistry
Loyola Univeristy New Orleans
ajschoef@loyno.edu
(Please note: Our spam filters are aggressive. Lack of response might mean I never got your email.)
