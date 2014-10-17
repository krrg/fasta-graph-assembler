fasta-graph-assembler
=====================


## Directory Structure
The `data` directory contains all of the input FASTA files for this project.

The `output` directory contains the output from running the assembler on the sequences in the data directory.  Each file
has the same prefix as the data file it came from, plus the kmer length used in the assembly.

The `metrics` directory contains the output from running the metrics.py script on the files in the output directory.
  Each metric file contains information about a corresponding output file
  
1.  Average contig length
2.  N-50 
3.  Total contigs returned
4.  Largest contig size.

## Running the Program

The assembler itself can be run using the `run.py` script:

    python run.py [INPUT FILE] [KMER-LENGTH]
    
For instance:

    python run.py data/example.data.fasta 17
    
This will read in the `data/example.data.fast` file, split each read into 17-mers, and then run the assembler.  The resulting contigs
from the assembler will be output, one per line, to the `outputs` directory, under the name `example.data.17.txt`, in order of 
increasing length. 

To see a listing of metrics for the output file, use the `metrics.py` script:

    python run.py outputs/example.data.17.txt
    
This will output a listing of metrics about the generated contigs in the output file.  





