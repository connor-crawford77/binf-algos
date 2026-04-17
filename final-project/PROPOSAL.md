# Project Title
Exploratory Targeted Nucleotide Sequence Alignment

# Research Question
What:
Given the genomes of two organisms and a specified sequence/gene of interest, what are the similarities/differences in their nucleotide sequences, and how significant are they?

Why:
Sequence alignment is a very important tool in biological research. It allows us to compare the composition of nucleotide and amino acid sequences to infer important structural and functional characteristics of the molecules they represent. The goal of this project will be to report on the sequence similarity of any two specified regions of two different organisms’ genomes. 
While there are many sequence alignment tools already out there, and possibly some that carry out this exact function, I thought it would be interesting to make a tool that can do sequence alignment based on specified regions of any two genomes. Tools like BLAST only report back the most similar sequences, but what if you are just as interested in the differences as you are in the similarities? This tool, hypothetically, will let you do some basic exploratory analysis on any two genomes that you’re interested in, regardless of whether they are similar or not.

# Algorithm and Algorithm Class

-	Class: Dynamic Programming (Pairwise alignment)

-	Type: Either Needleman-Wunsch or Smith-Waterman


-	This class is a good fit for this question because it can effectively score alignments without being too computationally demanding. One approach to scoring sequence alignments could be to score every possible alignment between two sequences, but as sequences get larger, this becomes impractical computationally. Dynamic programming algorithms provide a framework to avoid this while still picking the best alignments.


# Data Plan
-	I plan to use publicly available reference genomes (FASTA) and their annotation files (GTF or GFF) from databases like NCBI and UCSC.

-	The data will be nucleotide data from reference genome assemblies and their annotation files.


-	The initial “prototype data” to test the genome parsing will be a simple bacterial genome, like E. coli or B. subtilis, along with a well-known gene. To test the alignment, the initial two sequences will be highly conserved genes between related organisms, like the ribosomal rRNA genes. Both of these data sets represent the same types of data that will eventually be used, just at a smaller scale in the case of the bacterial genome, and with a known expected output for the rRNA genes (high conservation means we should get a high alignment score).



# Success Criteria

-	Success for this project will be at a minimum a program that reports how similar two sequences are, given input reference genomes and specified locations.

-	Additionally, it should report what positions are most similar and which are most different, possibly with a short explanation of how that was determined.

-	If there is time and it’s reasonable, I’d like to add features for genes that encode proteins. Maybe, along with nucleotide sequence comparison, it could produce the amino acid sequence for each gene and give an interesting report on its composition, maybe an amino acid similarity score too. It might be interesting to compare the similarity scores of two genes and their amino acid sequences.


-	Checking the accuracy of the alignment will be done with highly conserved sequences across species, like rRNA genes. If the rRNA genes of, say, humans and chimps don’t get a high sequence similarity score, then I’ll know something is going wrong.

# Pitfall Scan
1.	Different organizations use different annotations for their reference genomes, despite the sequences being the same. The program will either need to account for this and adjust based on the reference input or only use one type of annotation style. If the program tries to find a sequence based on an annotation it can’t recognize, it will break.

2.	The algorithm will need something like a lookup table matching each annotation (probably gene name and feature type) to its sequence in the reference. This seems like a lot of computational overhead, especially if it has to occur every time the program is run. I’m not sure if there is a way to efficiently solve this problem, but a strategy to mitigate it could be to create tables for select genomes that could be automatically loaded in, but that would leave out the option for loading in a genome that the program hasn’t already accounted for. I’ll have to see if there are efficient ways to deal with this.


3.	Although dynamic programming is better than the brute force approach at mitigating runtime and memory problems, if the sequences are long enough, the program may run into these issues, depending on the environment it’s used in. It might be necessary to put a cap on the sequence length that can be used to limit this problem. If this does become a problem, it will be important to detect the max sequence length limit that can be used – I’m not sure what the best method for this would be, but it will certainly be important to figure it out – if I don’t account for it, the program could easily blow up when someone else tries to use it.


# Initial Sketch of Repository Structure

final-project 
  |
   - main_program.py
   - readme.md
   - utils
       |
        - utils.py
   - tests
       |
        - tests.py
