from data_readers import get_fasta
import sys

def parse_ref(seq_file, gff_file, seq_id):
    """
    Parses a reference genome based of it's RefSeq ID and returns the sequence associated with it
    @param seq_file: Reference genome to parse
    @param gff_file: GFF annotation file to use
    @param seq_id: RefSeq ID to look for in the GFF file
    @return: Sequence of interest
    """
    for name, seq in get_fasta(seq_file):
        if len(seq) == 0:
            print(f"{seq_file} is not a valid reference file")
            sys.exit()
        with open(gff_file, mode='r', encoding='utf-8') as file:
            for i, gff_entry in enumerate(file):
                gff_split = gff_entry.split(";")
                id_split = gff_split[0].split("\t")
                if id_split[len(id_split) - 1] == f'ID={seq_id}':
                    seq_start = int(id_split[3])
                    seq_end = int(id_split[4])
                    return seq[seq_start:seq_end + 1]


    print(f'{seq_id} not found in the gff file provided, ensure that the ID is both correct and associated with the right reference files')
    sys.exit()


def find_location(seq1: str = None, seq2: str = None, alignment1: str = None, alignment2: str = None):
    """
    Finds the start location of sequence alignments in the original sequences
    @param seq1: First sequence to search
    @param seq2: Second sequence to search
    @param alignment1: First alignment to use
    @param alignment2: Second alignment to use
    @return: Where to alignments start in both sequences
    """

    alignment1_run = alignment1.replace('-', "")
    alignment2_run = alignment2.replace('-', "")

    alignment1_start = seq1.find(alignment1_run, 0, len(seq1) + 1)
    alignment2_start = seq2.find(alignment2_run, 0, len(seq2) + 1)

    return alignment1_start, alignment2_start
