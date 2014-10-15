__author__ = 'krr428'

import fasta_reader
import seq_splitter
import metrics
from debruijn import DeBruijnGraph
from collections import defaultdict
import sys
import pygal
from pygal.style import BlueStyle


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
    # klen = int(sys.argv[2])

    totals = []

    for klen in xrange(10, 80):
        complete_kmer_list = fasta_to_kmers(fasta_sequences, klen)
        supported_kmers = get_frequent_kmers(complete_kmer_list, 2)

        contigs_result = DeBruijnGraph(set(supported_kmers)).read_all_contigs()
        contigs_result = sorted(contigs_result, key=lambda contig: len(contig))

        metric = metrics.ContigMetrics(contigs_result)

        totals.append([
             klen,
             metric.mean_contig_size(),
             metric.largest_contig_size(),
             metric.n_50(),
             metric.total_contigs()
        ])

        chart = pygal.Bar(style=BlueStyle)
        chart.title = 'Kmer Length vs Largest Contig'
        chart.x_labels = map(str, [x[0] for x in totals])
        chart.add('Largest Contig', [x[2] for x in totals])
        chart.render_to_file("outputs/kmer_length_comparison.svg")

        # output_filename = determine_out_file(sys.argv[1], klen)
        # write_output_file(contigs_result, output_filename)
        # print "Output written to", output_filename
