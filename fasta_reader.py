
def read_input_file(fastafile):
    with open(fastafile) as f:
        lines = map(str.strip, f.readlines())
        result = []
        single_read = []
        for line in lines:
            if line == "":
                continue
            elif line[0] == '>':
                if len(single_read) > 0:
                    result.append("".join(single_read))
                    single_read = []
            else:
                single_read.append(line)
        return result


if __name__ == "__main__":
    print read_input_file("example.data.fasta")


