#!/usr/bin/env python3

from smithwaterman import smith_waterman
from typing import List, Tuple, Dict
import numpy as np

def read_fasta(filename: str) -> Dict[str, str]:
    # Empty dict to store the sequences where key is sequence ID and value are sequences
    sequences    = {}
    # This will store the sequence name
    current_name = None
    # This will store the sequence
    current_seq  = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()

            if line.startswith('>'):
                # Save the previous sequence before starting new sequence
                if current_name is not None:
                    # Save the completed sequences into the dictionary
                    sequences[current_name] = ''.join(current_seq)
                # Get the sequence ID after >
                current_name = line[1:].split()[0]
                # Reset for new sequence
                current_seq  = []
            else:
                # the new sequence line append to current sequence
                current_seq.append(line)

        # Save the last sequence line in the file
        if current_name is not None:
            sequences[current_name] = ''.join(current_seq)

    return sequences

def build_distance_matrix(sequences: Dict[str, str]) -> Tuple[np.ndarray, List[str]]:
    # Get the key sequence IDs list stored in the sequences dictionary
    labels = list(sequences.keys())
    # Number of total sequences
    n = len(labels)

    # Initialize a matrix with n rows x n columns with 0s
    matrix = np.zeros((n, n))

    # Outer loop which goes through each sequence as the first sequence in the pair
    for i in range(n):
        # Inner loop to avoid duplicate pairs
        for j in range(i + 1, n):

            # Get normalized similarity scores from smith waterman algorithm
            sim = smith_waterman(sequences[labels[i]], sequences[labels[j]])

            # Convert similarity to distance scores where closer to 0 means more similar
            dist = 1 - sim

            # Compute both sides of the matrix distance(i,j) == distance(j,i)
            matrix[i][j] = dist
            matrix[j][i] = dist

    # Return numpy array which is distance matrix and labels list which is sequence ID
    return matrix, labels


if __name__ == "__main__":
    # read sequences from fasta file
    sequences = read_fasta("data/lafayette_SARS_RT.fasta")

    # build distance matrix
    mat, ids = build_distance_matrix(sequences)

    # print distance matrix
    print("\nDistance matrix:")
    print(f"{'':>12}", end="")
    for id in ids:
        print(f"{id:>12}", end="")
    print()
    for i, id in enumerate(ids):
        print(f"{id:>12}", end="")
        for j in range(len(ids)):
            print(f"{mat[i][j]:>12.4f}", end="")
        print()
