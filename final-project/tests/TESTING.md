## Tests
This directory contains two scripts:

1. `test.py` used to check the Smith-Waterman aligner on simple sequences where optimal local alignments are known.
2. `runtime_tester.py` which generates two sequences of increasing length, and times how long the alignment takes on them.

`test.py` checks an example that is known to have one optimal alignment, and a second example that is know to have more than
one alignment to ensure that the `SmithWaterman` class will produce the right alignments, and multiple local alignments if they
are present. Both cases perform as expected.

`runtime_tester.py` is less a test of validity and more a test of "what can this program reasonably handle?". Around 25,000 to 30,000 bp sequences
is when memory complexity starts to become too much and the program slows. However, this was just tested on my local pc, if you are on a cluster or the cloud
and have a lot of memory to work with you might be able to get alignments with larger sequences to work - just understand that if you are examining
sequences that are very large this tool might not be best suited for your needs.
