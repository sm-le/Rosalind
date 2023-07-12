#################################################
# Fastq file reader
# by smlee

######################
# CUSTOM SCRIPT IMPORT

#############################
# PYTHON NATIVE MODULE IMPORT

phred_table = {
                "!":0,
                '"':1,
                "#":2,
                "$":3,
                "%":4,
                "&":5,
                "'":6,
                "(":7,
                ")":8,
                "*":9,
                "+":10,
                ",":11,
                "-":12,
                ".":13,
                "/":14,
                "0":15,
                "1":16,
                "2":17,
                "3":18,
                "4":19,
                "5":20,
                "6":21,
                "7":22,
                "8":23,
                "9":24,
                ":":25,
                ";":26,
                "<":27,
                "=":28,
                ">":29,
                "?":30,
                "@":31,
                "A":32,
                "B":33,
                "C":34,
                "D":35,
                "E":36,
                "F":37,
                "G":38,
                "H":39,
                "I":40,
                "J":41,
                "K":42
            }

class FastqRow():
    """class object for single object within Fastq file 
    """
    def __init__(self,record_id:str, record_seq:str, record_qual:str):
        """initialize object by accepting fastq related information
        """

        self.id = record_id
        self.seq = record_seq
        self.qual = record_qual

class Fastq():
    """class object for fastq file
    """
    def __init__(self,file:str):
        
        self._file = file

        # records
        self.records = list()
        self.arrays = list()

    @staticmethod
    def parse(file:str):

        with open(file, "r") as f:
            try:
                while True:
                    checker = next(f)
                    if checker.startswith("@"):
                        rid = f"{checker.strip().strip('@')}"
                        seq = next(f).strip()
                        next(f)
                        qual = next(f).strip()

                        record = FastqRow(rid, seq, qual)
                        yield record

            except StopIteration:
                pass

    def _parse(self):
        with open(self._file, "r") as f:
            try:
                while True:
                    checker = next(f)
                    if checker.startswith("@"):
                        rid = f"{checker.strip().strip('@')}"
                        seq = next(f).strip()
                        next(f)
                        qual = next(f).strip()

                        record = FastqRow(rid, seq, qual)
                        
                        self.records.append(record)

            except StopIteration:
                pass
    
    def _avgreadclean(self, threshold:int=28):
        """Remove reads based on average read quality

        Args:
            threshold = base quality threshold
        """
        records = list()
        remove_count = 0

        for record in self.records:
            qscores = [phred_table[i] for i in record.qual]
            avg_qscore = sum(qscores) / len(qscores)
            q_check = avg_qscore < threshold

            if q_check:
                remove_count += 1
            else:
                records.append(record)

        print(f"Removed {remove_count} records")
        self.records = records

        return remove_count
    
    def _percreadclean(self, threshold:int=28, percentage:int=90):
        """Remove reads based on percentages of read passing threshold

        Args:
            threshold = base quality threshold
        """

        records = list()
        remove_count = 0

        for record in self.records:
            qscores = [phred_table[i] for i in record.qual]
            bool_qscores = [i >= threshold for i in qscores].count(True)
            avg_qscore = (bool_qscores / len(qscores)) * 100 

            q_check = avg_qscore < percentage

            if q_check:
                remove_count += 1
            else:
                records.append(record)

        print(f"Removed {remove_count} records")
        self.records = records

        return len(self.records)
    
    def _getallquals(self):
        """get all quality array

        Args:
            threshold = base quality threshold
        """
        
        for record in self.records:
            qscores = [phred_table[i] for i in record.qual]
            
            self.arrays.append(qscores)

