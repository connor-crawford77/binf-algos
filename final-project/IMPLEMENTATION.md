## Project Snapshot
Question:  

Given the genomes of two organisms and a specified sequence/gene of interest, what are similarities/differences in their nucleotide sequences?

Algorithm:  

Dynamic Programming - Smith-Waterman for local alignment

Current Implementation Status:  

Smith-Waterman Class that performs alignment is up and working

## What is Implemented

The script that will perform the local alignments on any given two sequences is running.
As it's currently implemented it's functionality is the same as the alignment algorithm we developed in our
class project on alignment. However, I have converted it to a class implementation of that algorithm,
which deviates from the purely function based pseudocode I had developed. I did this to make the
alignment functionality more flexible and reusable when developing the final version of the 
program (grabbing genome sequences, performing alignmnet, and other added functionality like
location reporting). Developing alignment as a class makes it very easy to import and use in different script,
and will certainly make the logic of the main program easier to understand and debug.  

What is not developed yet is the reference genome parsing and sequence alignment reporting. I wanted
to get the alignment functionality straightened away first since it is the core functionality and because
we had already done the algorithm in class. This setup also makes it easy to go in and tweak the alignment
algorithm if necessary once I start to build the rest of the program.


## Prototype Demo Description

In the data/README.md file I have laid out some example code for doing minimal prototype runs
with this code. All that's needed is two simple sequences, I have provided a couple, but you could
use any two sequences you want so long as you define them properly. Next, you just have to create a ```SmithWaterman```
class object, passing in your sequence and the match, mismatch, and gap scores you want it to use (optional, default vals are 1, -1, -1).
Once you've created the object you just have to call the ```.sequence_alignment()``` method on the object and all the optimal alignments
will be returned as a list of tuples. I've also provided example code for unpacking that data structure
and observing all the alignments found.  

If you run the second example that has multiple optimal alignments with the provided code you should expect to see
this printed to your console:

```
Optimal alignment 1:
TTAT
TTAT
Optimal alignment 2:
AAAA
AAAA
```


## Data Documentation
The test data are simple nucleotide sequences where optimal alignments can easily be inferred
with an eye test.

In the above example the two sequences are TTATAAAA, and AAAATTAT
We can clearly see that the first four nucleotides of the first sequence line up with the last four sequences of
the second sequence, and the last four nucleotides of the first sequence line up with the first four nucleotides of the second sequence.
Therfore, since we are doing local alignment, we should expect to see those two stretches of the sequences as two optimal alignments since there is no
where else in the two sequences where we see a stretch of four our more nucleotides match exactly, and this is what we see from this class.




