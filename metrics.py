
import sys

def read_input_file(filename):
    with open(filename) as f:
        return map(str.strip, f.readlines())

if __name__ == "__main__":
    lines = read_input_file(sys.argv[1])
    
    lenlengths = map(len, lines)
    lenlengths = sorted(lenlengths)

    print "Average contig size:"
    print sum(lenlengths) / float(len(lenlengths))
    print 
    print "N-50"
    print lenlengths[len(lenlengths)/2]
    print 
    print "Total contigs returned:"
    print len(lines)
    print
    print "Largest contig size:"
    print lenlengths[-1]

