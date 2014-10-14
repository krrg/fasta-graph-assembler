__author__ = 'krr428'


def get_kmers_from(dnaseq, klen):
    result = []
    for i, j in zip(xrange(0, len(dnaseq)), xrange(klen, len(dnaseq) + 1)):
        result.append(dnaseq[i:j])
    return result

