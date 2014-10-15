__author__ = 'krr428'

import fasta_reader
import seq_splitter
from debruijn import DeBruijnGraph
from collections import defaultdict
import sys


def fasta_to_kmers(fasta_reads, klen):
    result = []
    for dnaseq in fasta_reads:
        kmers = seq_splitter.get_kmers_from(dnaseq, klen)
        result.extend(kmers)
    return result


def get_frequent_kmers(kmerlist, minimum_freq):
    frequencies = defaultdict(int)
    for kmer in complete_kmer_list:
        frequencies[kmer] += 1
    return filter(lambda key: frequencies[key] >= minimum_freq, frequencies.iterkeys())


def determine_out_file(infilename, klen):
    return "outputs/" + str(infilename.split('/')[-1]).replace(".fasta", ".{0}.txt".format(klen))


def write_output_file(contigs_result, filename):
    with open(filename, 'w') as f:
        f.write("\n".join(contigs_result))

if __name__ == "__main__":

    fasta_sequences = fasta_reader.read_input_file(sys.argv[1] if len(sys.argv) > 1 else "example.data.fasta")
    klen = int(sys.argv[2])

    complete_kmer_list = fasta_to_kmers(fasta_sequences, klen)
    supported_kmers = get_frequent_kmers(complete_kmer_list, 2)

    contigs_result = DeBruijnGraph(set(supported_kmers)).read_all_contigs()
    contigs_result = sorted(contigs_result, key=lambda contig: len(contig))

    output_filename = determine_out_file(sys.argv[1], klen)
    write_output_file(contigs_result, output_filename)
    print "Output written to", output_filename
