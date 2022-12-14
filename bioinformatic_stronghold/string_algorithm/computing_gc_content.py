"""
# String algorithm 4

A GC content of a DNA string is given by the percentages of G and C in the string.

Given 10 fasta formatted sequences, return id and gc-content with the highest gc content.

Example,
IN: 
    >fasta_1
    ATATC
    >fasta_2
    GGTCA
    >fasta_3
    GGCCT
OUT:
    fasta_3:80.0
"""

class FastaFile:
    """class object for genbank flat
    file
    """

    def __init__(self, file):
        
        self.file = file
        self.body = list()

    def __enter__(self):
        """Database initialization 
        when initialized with 'With'
        """

        self.parse()
 

        return self

    def __exit__(self, exception_type, exception_value, traceback):
        """'With' closurce
        """

        if exception_type is None:
            return True
        else:
            emessage = f"Error type: {exception_type}," \
                    f"Error Message: {exception_value}," \
                    f"Traceback: {traceback}"
            return emessage

    def parse(self):
        """Parse fasta file
        """

        try:
            header = ""
            sequence = ""
            header_count = 0

            # Loop file to read fasta file
            with open(self.file, "r") as f:
                for line in f:
                    if line.strip().startswith(">"):
                        header_count += 1
                        if header_count > 1:

                            # Save fasta format
                            self.body.append(
                                                {
                                                    "description":header,
                                                    "sequence":sequence.upper(),
                                                    "gc":(sequence.upper().count("G")+sequence.upper().count("C"))/len(sequence)
                                                }
                                            )

                            # Reset intermediate result
                            header_count = 1
                            header = ""
                            sequence = ""

                        header += line.strip().strip(">")
                    else:
                        sequence += line.strip("\n").strip("\t").strip()

                # Save fasta format
                if header:
                    self.body.append(
                                        {
                                            "description":header,
                                            "sequence":sequence.upper(),
                                            "gc":(sequence.upper().count("G")+sequence.upper().count("C"))/len(sequence)
                                        }
                                    )
        except Exception as e:
            msg = f"COULD NOT PARSE {self.file} | {type(e).__name__}, {e.args}, LINE AT: {e.traceback.tb_lineno}"
            print(msg)
    
    def collect(self):
        """Collect information
        """

        return self.body

def highest_gc_v1(fasta_path:str) -> str:
    """Calculate GC content of each sequence 
    and extract sequence header and GC percentage 
    of one with the highest GC content

    Args:
        fasta_path: path to fasta file

    Returns:
        string({fasta_header}\n{gc_content})
    """

    with FastaFile(fasta_path) as fa:
        fasta_entries = fa.collect()

    highest_gc = sorted(fasta_entries, key= lambda x: x["gc"], reverse=True)[0]
    
    return f"{highest_gc['description']}: " \
           f"{highest_gc['gc'] * 100}"