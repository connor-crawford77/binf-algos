## Recap Of Project

Question: Given the genomes of two organisms and a specified sequence/gene of interest, what are similarities/differences in their nucleotide sequences?

Algorithm and algorithm class: Dynamic programming - Smith-Waterman for local alignment.

Data: Nucleotide sequence data from reference genomes.

## Inputs, Outputs, Assumptions

Inputs: Reference Genomes in FASTA format, annotation features in GFF format, name of the GFF locations to compare from both genomes (this should be in RefSeq format).

Outputs: Most optimal local alignment of the two sequences, along with regions along the sequences where the alignment occurs.

## Detailed Pseudocode

```
first we need to access the sequences from the fasta file based on the names from the gff file 
this could be a good use case for the bamnostic package we used earlier in the term
def get_seqs(seq_file, gff_file):
  1. create a data structure to store seqs
  2. access the seqs in the fasta file
  3. get the seqs associated with the gff name annotation
  4. store and return them in a list

we'll need a function to calculate the score of each postion in the scoring matrix
def cal_score(matrix, seq1, seq2, i, j, match, mismatch, gap):
  this function will calculate the score of position ij in the matrix based on upper-left, up, and left-neighbors and keep track of where it came from in the matrix
  diag_score = upper-left position score + (match or mismatch)
  up_score = up position score + gap
  left_score = left position score + gap
  score = max(0, diag_score, up_score, left_score)
  traceback = position where max score came from (either the very start of the matrix, a diagonal position, an up position, or a left position.
  
  return score and traceback
  
we'll also need a function that find the max scores from our matrix, so we'll know where to start out traversal(s) from.
def max_scores(matrix):
  max_score = max score value in the matrix
  max_positions = positions in the matrix where the value equal to the max
  return positions as a tuple (i,j)

function to traceback our path through the matrix given a starting position
def traceback(seq1, seq2, traceback_matrix, maximum_position):
  define end, diag, up, and left moves
  define our current row and current column based on the maximum position
  current_move = teaceback_matrix[row][column]
  
  while our current move isn't an end move:
    if current_move == DIAG:
                aligned_seq1 = seq1[current_col] + aligned_seq1
                aligned_seq2 = seq1[current_row] + aligned_seq2
                current_row -= 1
                current_col -= 1
            elif current_move == UP:
                aligned_seq1 = "-" + aligned_seq1
                aligned_seq2 = seq2[current_row] + aligned_seq2
                current_col -= 1
            elif current_move == LEFT:
                aligned_seq1 = seq1[current_row] + aligned_seq1
                aligned_seq2 = "-" + aligned_seq2
                current_col -= 1
  return the aligned_seqs
  

finally, our smith waterman function to pull it together
def smith_waterman(seq1, seq2, match=1, mismatch=-1, mismatch=-2):
  initialize the score_matrix and traceback_matrix based on the length of the seqs
  
  for each row in the matrix:
    for each column in the matrix:
      score and traceback vals = cal_score(matrix, seq1, seq2, i, j, match, mismatch, gap)
      update matrices with scores and traceback vals
      
  find max scores in the matrix
  scores = max_scores(score_matrix)
  
  for score in scores:
    aligned_seqs = traceback(seq1, seq2, traceback_matrix, score)
    store each pair of aligned seqs as tuples in a list
  
  return the alignments
```





## Complexity and Bottlenecks

- as the two sequences being compared grow in size so does the time and space complexity of the algorithm O(mn). As the algorithm is currently defined, it won't be efficient as sequences get sufficiently long. Fortunately, most gff annotations of interest, specifically genes, shouldn't be large enough to overwhelm the algorithm. 

- Vectorization methods with numpy could speed up the time complexity of the algorithm but I worry space complexity will still be too much to overcome past a certain point - currently I'm not sure what the best ways for dealing with this would be.


  ## Validation and Testing Plan

- Initial tests will be on small local alignments where I know the best alignments e.g. ATAT,  ATATT.
  
- To stress test the capacity of the program I will synthetically create random sequences of increasing length - track memory usage by the program - and exit when it reaches a certain threshold. I can use this to report sequence lengths at which the memory threshold was reached.

- Can test functions with unit tests using pytest module:  can make assertions for functions like cal_score and traceback that test whether the output of the functions equals a known output (like known optimal sequence alignments for simple sequences where we can manually create the matrix and alignment for testing purposes).

## Updated Pitfalls and Risk Log

- Different annotation formats: different organizations use different annotation styles for their ref genomes. I think to start I'm going to limit the program to just use refseq formats and have it identify/report if the genome input is in a different format. If I have enough time I might be able get it to accept different formats but to start I just want to focus on one.

    

- Lookup table overhead: initially I was worried about having to keep an entire lookup table in memory for each reference genome in use and their annotations. I think I can use bamnostic functionality to avoid doing this. If not bamnostic I might be able to do some simple parsing using the genome locations of a given annotation in the gff file, but storing everything in memory should not be needed.

  
- Memory and runtime, which I initially identified as a pitfall initially, is what I think remains as the most prominent issue. As I mentioned above I'm going to try and diagnose this through synthetic sequence generation and memory use logging. I want to initially identify sequence lengths that max out memory and then explore optimization methods (like vectorization) from there. 
