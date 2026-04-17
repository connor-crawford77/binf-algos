from SmithWaterman import SmithWaterman
import argparse



from alignment_utils import parse_ref, find_location

def main() -> None: # pragma: no cover
    """
    Script driver
    @return: None
    """

    args = get_cli_args()
    seq_file1 = args.INFILE_REF1_FNA
    seq_file2 = args.INFILE_REF2_FNA
    gff_file1 = args.INFILE_GFF1
    gff_file2 = args.INFILE_GFF2

    seq_id1 = args.SEQ1_ID
    seq_id2 = args.SEQ2_ID

    seq1 = parse_ref(seq_file1, gff_file1, seq_id1)
    seq2 = parse_ref(seq_file2, gff_file2, seq_id2)


    sw = SmithWaterman(seq1, seq2)
    aligned_seqs = sw.sequence_alignment()

    outfile = 'alignments.txt'
    with open(outfile, 'w', encoding='utf-8') as file:
        for i, alignment in enumerate(aligned_seqs):
            file.write(f'Optimal Alignment {i + 1}\n')
            file.write(f'{alignment[0]}\n')
            file.write(f'{alignment[1]}\n')
            start1, start2 = find_location(seq1, seq2, alignment[0], alignment[1])
            file.write(f'First alignment starts in position {start1} of sequence {seq_id1}\n')
            file.write(f'Second alignment starts in position {start2} of sequence {seq_id2}\n\n')



def get_cli_args() -> argparse: # pragma no cover
    """
    Get argparse instance, client arguments to run the program
    @return: instance of argparse arguments
    """

    parser = argparse.ArgumentParser(description='Provide two reference genome FASTA files and there gff annotation files,'
    'along with the RefSeq sequence IDs of two sequences to generate local sequence alignment')

    parser.add_argument('--infile_ref1_fna',
                        dest='INFILE_REF1_FNA',
                        type=str,
                        help='First reference genome to parse',
                        required=True)

    parser.add_argument('--infile_ref2_fna',
                        dest='INFILE_REF2_FNA',
                        type=str,
                        help='Second reference genome to parse',
                        required=True)

    parser.add_argument('--infile_gff1',
                        dest='INFILE_GFF1',
                        type=str,
                        help='First gff file to parse, should be annotations for the first reference genome',
                        required=True)

    parser.add_argument('--infile_gff2',
                        dest='INFILE_GFF2',
                        type=str,
                        help='Second gff file to parse, should be annotations for the second reference genome',
                        )

    parser.add_argument('--seq1_id',
                        dest='SEQ1_ID',
                        type=str,
                        help='RefSeq Sequence ID for the first sequence to perform alignment with, should belong to first reference genome',
                        required=True)

    parser.add_argument('--seq2_id',
                        dest='SEQ2_ID',
                        type=str,
                        help='RefSeq Sequence ID for the second sequence to perform alignment with, should belong to the second reference genome')

    return parser.parse_args()


if __name__ == "__main__":
    main()
