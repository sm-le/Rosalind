#################################################
# Fasta file reader
# by smlee

######################
# CUSTOM SCRIPT IMPORT

#############################
# PYTHON NATIVE MODULE IMPORT

class FastaRow():
    """class object for fasta row
    """

    def __init__(self, id, seq):
        self.id = id
        self.seq = seq

class Fasta:
    """class object for fasta formatted file
    """

    def __init__(self, file):
        
        self._file = file
        self.records = list()

    @staticmethod
    def parse(file):
        """Parse fasta file
        """

        try:
            header = ""
            sequence = ""
            header_count = 0

            # Loop file to read fasta file
            with open(file, "r") as f:
                for line in f:
                    if line.strip().startswith(">"):
                        header_count += 1
                        if header_count > 1:

                            # Save fasta format
                            record = FastaRow(header, sequence.upper())
                            yield record
                            
                            # Reset intermediate result
                            header_count = 1
                            header = ""
                            sequence = ""

                        header += line.strip().strip(">")
                    else:
                        sequence += line.strip("\n").strip("\t").strip()

                # Save fasta format
                if header:
                    record = FastaRow(header, sequence.upper())
                    yield record
        except Exception as e:
            msg = f"COULD NOT PARSE {file} | {type(e).__name__}, {e.args}, LINE AT: {e.traceback.tb_lineno}"
            print(msg)
    
