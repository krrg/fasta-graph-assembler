import sys


class ContigMetrics:

    def __init__(self, contigs):
        self.contigs = sorted(contigs, key=len)
        self.contig_lengths = sorted(map(len, self.contigs))

    def mean_contig_size(self):
        return sum(self.contig_lengths) / float(len(self.contigs))

    def total_contigs(self):
        return len(self.contigs)

    def largest_contig_size(self):
        return self.contig_lengths[-1]

    def n_50(self):
        templist = []
        for contig_len in self.contig_lengths:
            templist.extend([contig_len]*contig_len)
        return templist[len(templist) / 2]


def read_input_file(filename):
    with open(filename) as f:
        return map(str.strip, f.readlines())


if __name__ == "__main__":
    lines = read_input_file(sys.argv[1])
    
    metrics = ContigMetrics(lines)

    print "Average (mean) contig size:"
    print metrics.mean_contig_size()
    print
    print "N-50:"
    print metrics.n_50()
    print
    print "Total contigs generated:"
    print metrics.total_contigs()
    print
    print "Largest contig size:"
    print metrics.largest_contig_size()
    print

