from SmithWaterman import SmithWaterman

# Tests the alignment algorithm on some simple example sequences to ensure it's working properly

# Example seqs
seq1 = 'TACTTAG'
seq2 = 'CACATTAA'

# Multiple alignments example
# seq1 = "TTATAAAA"
# seq2 = "AAAATTAT"


# Example class instantiation
sw = SmithWaterman(seq1, seq2)

# Example method call for sequence alignment
aligned_seqs = sw.sequence_alignment()

# Parsing and printing alignments
for i, pair in enumerate(aligned_seqs):
    print(f'Optimal alignment {i + 1}:')
    print(pair[0])
    print(pair[1])
    
