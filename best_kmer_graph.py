__author__ = 'krr428'

import fasta_reader
from fasta_to_contigs import FastaContigConverter, ContigIO
from metrics import ContigMetrics
import sys
import pygal
from pygal.style import BlueStyle


def create_metric_chart(points):

    xtitle = 'Kmer Length'
    ytitle = 'N50'
    xy_chart = pygal.XY(style=BlueStyle, x_title=xtitle, y_title=ytitle, show_legend=False)
    xy_chart.add('N50', points)
    xy_chart.render_to_file('outputs/chart5.svg')


if __name__ == "__main__":

    reads = fasta_reader.read_input_file(sys.argv[1])

    points = []  # XY Coordinates

    for klen in xrange(2, 35):
        contigs = FastaContigConverter.fasta_to_contigs(reads, klen=klen)
        metrics = ContigMetrics(contigs)
        points.append((klen, metrics.largest_contig_size()))

    create_metric_chart(points)

