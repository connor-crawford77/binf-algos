import numpy as np


class SmithWaterman:
    """
    Class that contains all the attributes and methods to perform Smith Waterman local sequence alignment on a pair of sequences.
    """

    def __init__(self, seq1, seq2, match=1, mismatch=-1, gap=-1):
        """
        Defines the attributes of the class
        seq1: First sequence to use in the alignment
        seq2: Second sequence to use in the alignment
        match: Match score to use
        mismatch: Mismatch penalty to use
        gap: Gap penalty to use
        """

        self.seq1 = seq1
        self.seq2 = seq2
        self.match = match
        self.mismatch= mismatch
        self.gap = gap
        # Scoring and traceback matrices initialized based on the length of the provided seqs
        self.scoring_matrix = np.zeros((len(self.seq1) + 1, len(self.seq2) + 1), dtype=np.int8)
        self.traceback_matrix = np.zeros((len(self.seq1) + 1, len(self.seq2) + 1), dtype=np.int8)
        # Define pointers to use throughout the class - refer to where a score came from
        self.end = 0
        self.diag = 1
        self.up = 2
        self.left = 3


    def cal_score(self, i, j):
        """
        Class method that calculates the max alignment score for given positions of two sequences and finds where the max score came from
        i: Position in sequence 1
        j: Position in sequence 2
        return: The max alignment score for that position and where it came from
        """

        if self.seq1[i - 1] == self.seq2[j - 1]:
            diag_score = int(self.scoring_matrix[i - 1, j - 1]) + self.match
        else:
            diag_score = int(self.scoring_matrix[i - 1, j - 1]) + self.mismatch
        up_score = int(self.scoring_matrix[i - 1, j]) + self.gap
        left_score = int(self.scoring_matrix[i, j - 1]) + self.gap

        score = max(0, diag_score, up_score, left_score)
        if score == 0:
            traceback = self.end
            return score, traceback
        elif diag_score == score:
            traceback = self.diag
            return score, traceback
        elif up_score == score:
            traceback = self.up
            return score, traceback
        elif left_score == score:
            traceback = self.left
            return score, traceback


    def max_scores(self):
        """
        Method to find the locations of the maximum values in the scoring matrix. These are the indices to be used as a starting point in the traceback.

        return: Max score value and it's locations in the scoring matrix
        """

        max_score = self.scoring_matrix.max()
        indices = np.where(self.scoring_matrix == max_score)
        index_pairs = np.asarray(indices).T

        return max_score, index_pairs


    def traceback(self, maximum_position):
        """
        Method that finds the optimal local sequence alignment given the position
        maximum_position: Position to start in the traceback matrix
        return: The optimal sequence alignment
        """

        current_row, current_col = maximum_position
        aligned_seq1 = ""
        aligned_seq2 = ""
        while self.traceback_matrix[current_row][current_col] != self.end:
            current_move = self.traceback_matrix[current_row][current_col]
            if current_move == self.diag:
                aligned_seq1 = self.seq1[current_row - 1] + aligned_seq1
                aligned_seq2 = self.seq2[current_col - 1] + aligned_seq2
                current_row -= 1
                current_col -= 1
            elif current_move == self.up:
                aligned_seq1 = self.seq1[current_row - 1] + aligned_seq1
                aligned_seq2 = "-" + aligned_seq2
                current_row -= 1
            elif current_move == self.left:
                aligned_seq1 = "-" + aligned_seq1
                aligned_seq2 = self.seq2[current_col - 1] + aligned_seq2
                current_col -= 1

        return aligned_seq1, aligned_seq2


    def matrix_population(self):
        """
        Methods that populates the scoring and traceback matrices with the appropriate values and calls the max_scores method to get the best score and their indices.
        return: Max score of the scoring matrix and the indices it occurs at.
        """

        i = 1
        j = 1
        # Make sure we're not going out of the range of any sequences since they can have differing lengths
        while i <= len(self.seq1):
            while j <= len(self.seq2):
                self.scoring_matrix[i][j], self.traceback_matrix[i][j] = self.cal_score(i, j)
                j += 1
            j = 1
            i += 1

        max_score, indices = self.max_scores()

        return max_score, indices


    def sequence_alignment(self):
        """
        Method that calls the matrix_population method to get fill the matrices and get the locations of the optimal alignments
        amd calls the traceback method on each optimal alignment location to get the final aligned sequences.
        return: All optimal local alignments of the two sequences.
        """

        score, indices = self.matrix_population()
        aligned_seqs = []
        for position in indices:
            aligned_seq1, aligned_seq2 = self.traceback(position)
            aligned_seqs.append((aligned_seq1, aligned_seq2))

        return aligned_seqs
