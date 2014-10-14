__author__ = 'krr428'

import fasta_reader
import seq_splitter
from debruijn import DeBruijnGraph
from collections import defaultdict
import sys

if __name__ == "__main__":

    seqs = fasta_reader.read_input_file(sys.argv[1] if len(sys.argv) > 1 else "example.data.fasta")

    complete_kmer_list = []

    for dnaseq in seqs:
        kmers = seq_splitter.get_kmers_from(dnaseq, klen=33)
        complete_kmer_list.extend(kmers)

    frequencies = defaultdict(int)

    for kmer in complete_kmer_list:
        frequencies[kmer] += 1

    supported_kmers = filter(lambda kmer: frequencies[kmer] > 1, frequencies.iterkeys())

    print "\n".join(DeBruijnGraph(set(supported_kmers)).read_all_contigs())
    #print "\n".join(sorted(DeBruijnGraph(seqs).read_all_contigs()))
