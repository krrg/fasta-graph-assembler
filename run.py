__author__ = 'krr428'

import fasta_reader
import seq_splitter
import metrics
from debruijn import DeBruijnGraph
from collections import defaultdict
import sys
import pygal
from pygal.style import BlueStyle




if __name__ == "__main__":

    fasta_sequences = fasta_reader.read_input_file(sys.argv[1] if len(sys.argv) > 1 else "example.data.fasta")
    klen = int(sys.argv[2])

    # totals = []

    # for klen in xrange(10, 80):
    #     complete_kmer_list = fasta_to_kmers(fasta_sequences, klen)
    #     supported_kmers = get_frequent_kmers(complete_kmer_list, 2)
    #
    #     contigs_result = DeBruijnGraph(set(supported_kmers)).read_all_contigs()
    #     contigs_result = sorted(contigs_result, key=lambda contig: len(contig))
    #
    #     metric = metrics.ContigMetrics(contigs_result)
    #
    #     totals.append([
    #          klen,
    #          metric.mean_contig_size(),
    #          metric.largest_contig_size(),
    #          metric.n_50(),
    #          metric.total_contigs()
    #     ])

    # chart = pygal.Line(style=BlueStyle)
    # chart.title = 'Kmer Length vs Largest Contig'
    # chart.x_labels = map(str, xrange(10, 80))
    # print chart.x_labels
    # chart.add('Largest Contig', [x[2] for x in totals])
    # chart.render_to_file("outputs/kmer_length_comparison.svg")

    complete_kmer_list = fasta_to_kmers(fasta_sequences, klen)
    supported_kmers = get_frequent_kmers(complete_kmer_list, 2)

    contigs_result = DeBruijnGraph(set(supported_kmers)).read_all_contigs()
    contigs_result = sorted(contigs_result, key=lambda contig: len(contig))

    output_filename = determine_out_file(sys.argv[1], klen)
    write_output_file(contigs_result, output_filename)
    print "Output written to", output_filename
