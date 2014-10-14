import sys
from collections import deque, defaultdict


def read_input_file(filename):
    with open(filename) as f:
        return map(str.strip, f.readlines())


def compress_overlap(iterable):
    result = []
    for kmer in iterable:
        result.append(kmer[0])
    result.extend(iterable[-1][1:])
    return result


class DeBruijnGraph:

    def __init__(self, kmerlist):
        self.nodes = defaultdict(list)
        self.incoming = defaultdict(int)
        self.outgoing = defaultdict(int)

        for kmer in kmerlist:
            self.nodes[kmer[:-1]].append(kmer[1:])

        self.__count_incoming_references()
        self.__count_outgoing_references()

    def __count_outgoing_references(self):
        for n in self.incoming:
            self.outgoing[n] = 0  # This is necessary to trap the end node in some cases.
        for n in self.nodes:
            self.outgoing[n] = len(self.nodes[n])

    def __count_incoming_references(self):
        for n in self.nodes:
            self.incoming[n] = 0  # This is necessary to trap the start node in some cases.
        for n in self.nodes:
            for referenced in self.nodes[n]:
                self.incoming[referenced] += 1

    def read_contig(self, start):
        # if not self.is_intermediate_node(start):
        #     print start, "is not an intermediate node!"
        #     print start, '->', ','.join(self.nodes[start])
        if not self.is_intermediate_node(start):
            return deque([start])

        contig = deque([start])
        nextmer = self.nodes[start][0]

        while self.is_intermediate_node(nextmer):
            contig.append(nextmer)
            nextmer = self.nodes[nextmer][0]
            if nextmer == start:
                break  # This indicates that this is a loop back!

        contig.append(nextmer)
        return contig

    def __read_contig_at(self, branch):
        contigs = []
        for nextnode in self.nodes[branch]:
            subcontig = self.read_contig(nextnode)
            subcontig.appendleft(branch)
            contigs.append(subcontig)
        return contigs

    def read_all_contigs(self):
        contigs = []
        for node in self.nodes:
            if self.is_start_node(node) or self.is_multibranch_node(node):
                contigs.extend(self.__read_contig_at(node))
        contigs = map(compress_overlap, contigs)
        return map(''.join, contigs)

    def is_intermediate_node(self, kmer):
        return self.incoming[kmer] == 1 and self.outgoing[kmer] == 1

    def is_multibranch_node(self, kmer):
        return self.outgoing[kmer] > 1 or self.incoming[kmer] > 1

    def is_halt_node(self, kmer):
        return self.outgoing[kmer] == 0

    def is_loop_node(self, kmer):
        return kmer in self.nodes[kmer]

    def print_graph(self):
        for kmer in self.nodes:
            print kmer, '->', ",".join(self.nodes[kmer])

    def is_start_node(self, kmer):
        return self.incoming[kmer] == 0

if __name__ == "__main__":
    graph = DeBruijnGraph(read_input_file(sys.argv[1]))
    print " ".join(graph.read_all_contigs())
