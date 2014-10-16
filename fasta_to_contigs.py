__author__ = 'krr428'

import fasta_reader
import seq_splitter
import metrics
from debruijn import DeBruijnGraph
from collections import defaultdict
import sys


class FastaContigConverter:

    @staticmethod
    def __fasta_to_kmers(fasta_reads, klen):
        result = []
        for dnaseq in fasta_reads:
            kmers = seq_splitter.get_kmers_from(dnaseq, klen)
            result.extend(kmers)
        return result

    @staticmethod
    def __get_frequent_kmers(kmerlist, minimum_freq):
        frequencies = defaultdict(int)
        for kmer in kmerlist:
            frequencies[kmer] += 1
        return filter(lambda key: frequencies[key] >= minimum_freq, frequencies.iterkeys())

    @staticmethod
    def fasta_to_contigs(fasta_sequences, klen):
        complete_kmer_list = FastaContigConverter.__fasta_to_kmers(fasta_sequences, klen)
        supported_kmers = FastaContigConverter.__get_frequent_kmers(complete_kmer_list, 2)
        contigs_result = DeBruijnGraph(set(supported_kmers)).read_all_contigs()
        contigs_result = sorted(contigs_result, key=lambda contig: len(contig))
        return contigs_result


class ContigIO:

    @staticmethod
    def determine_out_file(infilename, klen):
        return "outputs/" + str(infilename.split('/')[-1]).replace(".fasta", ".{0}.txt".format(klen))

    @staticmethod
    def write_output_file(contigs_result, filename):
        with open(filename, 'w') as f:
            f.write("\n".join(contigs_result))
