from SmithWaterman import SmithWaterman
import random
import time


def random_seqs(start_len, max_len, alphabet, step):
    """
    Yields two random DNA sequences of increasing length
    """
    for length in range(start_len, max_len + 1, step):
        seq1 = ''.join(random.choices(alphabet, k=length))
        seq2 = ''.join(random.choices(alphabet, k=length))
        yield seq1, seq2


alphabet = ['A', 'T', 'G', 'C']

# example to show functionality of the sequence creation
# for seq1, seq2 in random_seqs(1000, 1000000, alphabet, 1000):
    # print(seq1[0:10])
    # print(seq2[0:10])
    # sw = SmithWaterman(seq1[0:10], seq2[0:10])
    # alignments = sw.sequence_alignment()
    # print(alignments[0][0])
    # print(alignments[0][1])
    # break

for seq1, seq2 in random_seqs(1000, 1000000, alphabet, 5000):
    start_time = time.perf_counter()
    sw = SmithWaterman(seq1, seq2)
    alignments = sw.sequence_alignment()
    end_time = time.perf_counter()
    print(f'Execution time for two random DNA sequences of length {len(seq1)} is: {round(end_time - start_time, 2)} seconds')
    if end_time - start_time > 500:
        break
