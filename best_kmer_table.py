__author__ = 'krr428'

import fasta_reader
from fasta_to_contigs import FastaContigConverter, ContigIO
from metrics import ContigMetrics
import sys
import pygal
from pygal.style import BlueStyle


if __name__ == "__main__":

    reads = fasta_reader.read_input_file('data/real.error.large.fasta')

    for klen in xrange(10, 32):
        contigs = FastaContigConverter.fasta_to_contigs(reads, klen=klen)
        metrics = ContigMetrics(contigs)
        print klen, '&', metrics.total_contigs(), '&', metrics.n_50(), '&', metrics.largest_contig_size(), '\\\\'


