__author__ = 'krr428'

import fasta_reader
from fasta_to_contigs import FastaContigConverter, ContigIO
import sys


if __name__ == "__main__":

    fasta_sequences = fasta_reader.read_input_file(sys.argv[1])
    klen = int(sys.argv[2])

    contigs_result = FastaContigConverter.fasta_to_contigs(fasta_sequences, klen)

    output_filename = ContigIO.determine_out_file(sys.argv[1], klen)
    ContigIO.write_output_file(contigs_result, output_filename)

    print "Output written to", output_filename
