# Final Reflection

## What Went Right
- Class implementation of the Smith-Waterman algorithm made integrating the alignment functionality into the main script very easy, all that was needed was initialization
  of the class with the sequences, and then a call of the `.sequence_alignment()` method.
- Reference genome data was very accessible. Getting the reference genome files through NCBIs website is a pretty painless process, and all the data you need to run the
  program can be found there.
- Consistent GFF formatting made accessing Sequence IDs straightforward, you can always look in the same spot on a line in GFF file for this value, and if it's a properly
  formatted GFF, it will be there.
- Command line argument parser ended up fitting in perfectly with the goals of this program, meaning you don't have to make any code to run the components of the program,
  you can just download the files, set up the environment, and give it the data.

## What Went Wrong
- The initial implementation of my `matrix_population()` called the `cal_score()` method on every row and column of the `scoring_matrix` which led to some negative indexing
  issues that stumped me for quite a while. Mainly because you can still get the alignment to run sometimes with the negative indices, but the matrices that it creates in the
  process don't make any sense. Eventually I figured out I was calling this method on rows and columns that it shouldn't be, and once I skipped them, the functionality
  was restored.
- If I started over I would give myself more time to try and optimize the main algorithm. The implementation works now as is, but it's pretty slow, even for sequences
  that around 5,000 bp. I understimated the time it would take to pull all the moving parts together to get the whole program to work, and that admittedly left me
  with less time to work on this.


## Algorithmic Lessons
- This algorithm, in it's functionality, fit the problem at hand perfectly. The goal was to produce local optimal alignments between two sequences, which it does.
  However, I don't think it's very practical for large sequences, even with optimized performance. Eventually, filling out an entire scoring and traceback matrix across
  the entirety of two sequences becomes too computational demanding to be practical. It makes sense now why tools like BLAST do a seed search before starting the alignment
  process. Fortunately, the use case for this program is smaller sequences, for the most part - but even still there are some large genes out there that won't perform well
  with this current implementation. I guess a good question that extends from this, that I don't have the answer for, is at what point do you switch from full sequence alignment
  (under the assumption you've optimized the Smith-Waterman algorithm) to a heuristic based search like BLAST? I guess this would also depend on the length of the two sequences,
  if both are of equal length I imagine you couldn't use a BLAST like approach, so it may not be appropriate given the goal of this program.
- This algorithm performs essentially the same way as presented in lecture, and as implemented in the project, just done on a larger sequence size scale. It was cool to see
  it operate on real examples.

  ## Future Directions
- My first order of action would be to figure out how to perform vector operations on the matrices as opposed to for loops as it's currently implemented. This is something
  I wanted to get to but didn't have time and I'm sure would speed up the algorithm.
- More extensive testing. I made sure to run a few simple examples on the aligner, and tested out run-time performance to estimate what kind of sequences can be used, but I don't have
  thorough testing implemented. I also don't have explicit testing to ensure that the parsing is accurate, just manual checks I did along the way (checking that the right seqid and genomic
  locations were found). I'm banking on the RefSeq file formats being consistent for that, but I should have more extensive tests.
- It might be kind of neat to create a multiple sequence aligner off this same concept. You could, hypothetically, have an initial alignment with a similar process to what
  is done here then use one of the alignments created to build out with additional sequences.


