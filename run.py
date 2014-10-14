__author__ = 'krr428'

import fasta_reader
import seq_splitter
from debruijn import DeBruijnGraph
import sys

if __name__ == "__main__":

    seqs = fasta_reader.read_input_file(sys.argv[1] if len(sys.argv) > 1 else "example.data.fasta")

    complete_kmer_list = []

    for dnaseq in seqs:
        kmers = seq_splitter.get_kmers_from(dnaseq, klen=8)
        complete_kmer_list.extend(kmers)

    # print "\n".join(DeBruijnGraph(complete_kmer_list).read_all_contigs())
    print "\n".join(sorted(DeBruijnGraph(seqs).read_all_contigs()))