## Project Overview 

- The research question: 

    Given two reference genomes, their associated GFF annotations files, and two sequences of interest within the genome - what are the most optimal local sequence alignments?

- The chosen algorithm and class:

  Smith-Waterman - Dynamic Programming

- The type of data and main outputs:

  Input: Two RefSeq reference genomes at most (although one can be used), two RefSeq GFF files associated with the provided reference genomes at most (although one can be used), and two sequence       IDs that can be parsed from the GFF files to get locations to use to grab the sequences from the genomes.

  Output: A single alignments.txt file that contains all the optimal local alignments found between the two sequences, along with where the alignments start in the original sequences.

## Installation/Setup
1. Have a downloaded version of Python (3.11.7 or higher) preferably in an IDE like PyCharm or VSCode.
2. Install numpy if not already installed into your environment via pip : `pip install numpy`.
3. Make sure all essential scripts are downloaded into your working directory, these include: `SmithWaterman.py`, `main.py`, `alignment_utils.py`, and `data_readers.py`.
4. You should be ready to go!

## Quick Start
- Once your environment is set up you can run a command like the following in your terminal (make sure you point your computer toward the path where your environment/working directory is - you may need to change main.py in this command to `path/to/main.py`  depending on where you are running the command from):
  
  `python3 main.py --infile_ref1_fna "GCF_000005845.2_ASM584v2_genomic.fna" --infile_ref2_fna "GCF_000006945.2_ASM694v2_genomic.fna" --infile_gff1 "ecoli_genomic.gff" --infile_gff2      "salmonella_genomic.gff" --seq1_id "gene-b3851" --seq2_id "gene-STM0219"`

- `--infile_ref1_fna` and `--infile_ref2_fna` are the two reference genome files. These files will need to be downloaded based on what species/genomes you are interested in. You can find how to get these files in the data/README.md. If you want to use the files used in this command, use the prefixes to the file names in your genome search and it should bring you right to the correct page (e.g., GCF_000005845.2_ASM584v2 ). Make sure the files are moved to your working directory.

- `--infile_gff1` and `--infile_gff2` are the two GFF annoation files. Similarly two the reference genomes, you will need to download these files. You can do this at the same time you download your references, this is included in the instructions in data/README.md. Once again, make sure the files are moved to your working directory.`

- `--seq1_id` and `--seq2_id` are the RefSeq IDs for the two sequences you are interested in, this is where you get to play around with whatever sequences you are interested in. These sequences can be genes, introns, exons, rna, whatever you want - you just have to make sure they are a valid sequence IDs somewhere in your reference genomes. The examples I give are genes and take the form of "gene-(insert gene ID)", but the IDs can be pretty variable so make sure you double check them. It might take a little research to find these. A relatively easy way to do this for genese is via NCBIs "Gene" search, which is located in the same place as it's Genome search that I provided instructions for in the data/README.md. You can specify the Taxon, and description of a gene you're interested in like "16s ribosomal RNA". This search will give you the number for the "Gene ID" which can be used in a quick command F of your GFF file - the Seq ID this program requires will be the first entry of the semi-colon delimited string in the line the "Gene ID" is located and will appear as "ID=seq ID".

## Expected Output
- In your working directory the program will produce an alignments.txt file with optimal local alignments. If run correctly the output should look something like:

  ```
  Optimal Alignment 1

  Alignments

  First alignment starts in position ## of sequence abc

  Second alignment starts in position ## of sequence def

  ...

  ```
  for each optimal alignment.


## Usage and Options
- The main script for this program is `main.py`.  It gathers the arguments required to run the program from the user, parses the genome for the sequences, runs sequence alignment, and then writes all optimal local alignments to a txt file. It uses `alignment_utils.py` to parse the genome and grab the sequences which uses tools from the `data_readers.py` utility script provided earlier in the semester by Marcus. `SmithWaterman.py` is then used to align the two sequences and `alignment_utils.py` is used once again used to find alignment location in the original sequences. Finally, the output is written to `alignments.txt` which will be written in your working directory.

- Additonaly to the use case I originally provided, you can also compare two genes within the same genome if that's what you are interested in. Following the example from above, you could compare two genes in the `GCF_000005845.2_ASM584v2` (Escherichia coli K-12) genome with the following command:

  `python3 main.py --infile_ref1_fna "GCF_000005845.2_ASM584v2_genomic.fna" --infile_ref2_fna "GCF_000005845.2_ASM584v2_genomic.fna" --infile_gff1 "ecoli_genomic.gff" --infile_gff2 "ecoli_genomic.gff" --seq1_id "gene-b3348" --seq2_id "gene-b3356"`

- All arguments defined are required for the program to run.


## Limitations and Assumptions
- Assumptions:

  The most important assumption of this tool is that you are using RefSeq reference files to create alignments, if you are not, the program will fail. This would likely be an easy limitation to overcome by adding a GenBank parsing, and having conditionals that check file type, but I did not have time add this. Additionally the Sequence IDs must be those associated with "ID=" in the GFF which is very specific, and can be somewhat of a pain to figure out. Allowing something like "Gene ID" (just the numeric identified for a gene) or for any other type of sequence would probably make it easier to find valid IDs for the sequences of interest.

- Limitations:

  This tool is not optimized for speed or limiting memory use, which dampens it's capacity to do alignment with larger genomes and sequences. On my PC it takes about 8-9 minutes to do alignments between two sequences in the 25,000-35,000 bp range. The two genomes the example sequences are run on are E. coli and Salmonella enterica, which are two smaller genomes with relatively small sequences on average. This program is probably best for exploratory analysis on these types of genomes as currently implemented. Additionally, this is not a tool that is designed to report significance of alignment or any functional relationships between aligned sequences (although that second part would be cool) - It is simply meant to report valid local alignments between two sequences. It should only be used as a starting point to explore similarities and differences between sequences of interest.
