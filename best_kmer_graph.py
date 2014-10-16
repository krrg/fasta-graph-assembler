__author__ = 'krr428'

import fasta_reader
from fasta_to_contigs import FastaContigConverter, ContigIO
from metrics import ContigMetrics
import sys
import pygal
from pygal.style import BlueStyle


def create_metric_chart(points):
    xy_chart = pygal.XY(style=BlueStyle, x_title='Kmer Length', y_title='Largest Contig', show_legend=False)
    xy_chart.title = 'Kmer Length vs Largest Contig'
    xy_chart.add('Largest Contig', points)
    xy_chart.render_to_file('outputs/chart2.svg')


if __name__ == "__main__":

    reads = fasta_reader.read_input_file('data/real.error.small.fasta')

    points = []  # XY Coordinates

    for klen in xrange(2, 100):
        contigs = FastaContigConverter.fasta_to_contigs(reads, klen=klen)
        metrics = ContigMetrics(contigs)
        points.append((klen, metrics.largest_contig_size()))

    create_metric_chart(points)

