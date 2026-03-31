## Data to Use For This Implementation
This implementation is just the baseline functionality of alignment. It doesn't grab sequences from reference genomes yet, and thus,
you don't need access to reference genomes or any large datasets for that matter. Below I'll provide some example sequences and code you can use
to get the class implementation to work. 

```
# Example seqs
seq1 = 'TACTTAG'
seq2 = 'CACATTAA'

# Multiple alignments example
seq1 = "TTATAAAA"
seq2 = "AAAATTAT"


# Example class instantiation
sw = SmithWaterman(seq1, seq2)

# Example method call for sequence alignment
aligned_seqs = sw.sequence_alignment()

# Parsing and printing alignments
for i, pair in enumerate(aligned_seqs):
    print(f'Optimal alignment {i + 1}:')
    print(pair[0])
    print(pair[1])

```
