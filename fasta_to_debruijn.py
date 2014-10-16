__author__ = 'krr428'

import fasta_reader
import seq_splitter
import metrics
from debruijn import DeBruijnGraph
from collections import defaultdict
import sys

class FastaDebruijnConverter:

    def __init__(self):
        pass

    def fasta_to_kmers(self, fasta_reads, klen):
    result = []
    for dnaseq in fasta_reads:
        kmers = seq_splitter.get_kmers_from(dnaseq, klen)
        result.extend(kmers)
    return result

    def get_frequent_kmers(self, kmerlist, minimum_freq):
        frequencies = defaultdict(int)
        for kmer in complete_kmer_list:
            frequencies[kmer] += 1
        return filter(lambda key: frequencies[key] >= minimum_freq, frequencies.iterkeys())

    def determine_out_file(self, infilename, klen):
        return "outputs/" + str(infilename.split('/')[-1]).replace(".fasta", ".{0}.txt".format(klen))

    def write_output_file(self, contigs_result, filename):
        with open(filename, 'w') as f:
            f.write("\n".join(contigs_result))
