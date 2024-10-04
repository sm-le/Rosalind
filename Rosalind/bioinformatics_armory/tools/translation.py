#################################################
# nucleotide translation into protein with table
# by smlee

######################
# CUSTOM SCRIPT IMPORT

#############################
# PYTHON NATIVE MODULE IMPORT

translation_table = {
                        "1": {
                                "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                                "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                                "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
                                "TGT":"C", "TGC":"C", "TGA":"*", "TGG":"W",

                                "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                                "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                                "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                                "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",

                                "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
                                "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                                "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                                "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",

                                "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                                "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                                "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                                "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                            },

                        "2": {
                                "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                                "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                                "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
                                "TGT":"C", "TGC":"C", "TGA":"W", "TGG":"W",

                                "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                                "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                                "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                                "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",

                                "ATT":"I", "ATC":"I", "ATA":"M", "ATG":"M",
                                "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                                "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                                "AGT":"S", "AGC":"S", "AGA":"*", "AGG":"*",

                                "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                                "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                                "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                                "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                            },

                        "3": {
                                "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                                "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                                "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
                                "TGT":"C", "TGC":"C", "TGA":"W", "TGG":"W",

                                "CTT":"T", "CTC":"T", "CTA":"T", "CTG":"T",
                                "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                                "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                                "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",

                                "ATT":"I", "ATC":"I", "ATA":"M", "ATG":"M",
                                "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                                "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                                "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",

                                "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                                "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                                "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                                "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                            },

                        "4": {
                                "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                                "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                                "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
                                "TGT":"C", "TGC":"C", "TGA":"W", "TGG":"W",

                                "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                                "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                                "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                                "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",

                                "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
                                "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                                "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                                "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",

                                "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                                "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                                "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                                "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                            },

                        "5": {
                                "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                                "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                                "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
                                "TGT":"C", "TGC":"C", "TGA":"W", "TGG":"W",

                                "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                                "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                                "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                                "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",

                                "ATT":"I", "ATC":"I", "ATA":"M", "ATG":"M",
                                "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                                "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                                "AGT":"S", "AGC":"S", "AGA":"S", "AGG":"S",

                                "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                                "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                                "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                                "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                            },

                        "6": {
                                "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                                "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                                "TAT":"Y", "TAC":"Y", "TAA":"Q", "TAG":"Q",
                                "TGT":"C", "TGC":"C", "TGA":"*", "TGG":"W",

                                "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                                "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                                "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                                "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",

                                "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
                                "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                                "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                                "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",

                                "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                                "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                                "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                                "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                            },

                        "9": {
                                "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                                "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                                "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
                                "TGT":"C", "TGC":"C", "TGA":"W", "TGG":"W",

                                "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                                "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                                "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                                "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",

                                "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
                                "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                                "AAT":"N", "AAC":"N", "AAA":"N", "AAG":"K",
                                "AGT":"S", "AGC":"S", "AGA":"S", "AGG":"S",

                                "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                                "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                                "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                                "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                            },
                        
                        "10": {
                                "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                                "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                                "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
                                "TGT":"C", "TGC":"C", "TGA":"C", "TGG":"W",

                                "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                                "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                                "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                                "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",

                                "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
                                "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                                "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                                "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",

                                "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                                "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                                "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                                "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                            },
                        
                        "11": {
                                "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                                "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                                "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
                                "TGT":"C", "TGC":"C", "TGA":"*", "TGG":"W",

                                "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                                "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                                "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                                "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",

                                "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
                                "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                                "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                                "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",

                                "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                                "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                                "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                                "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                            },

                        "12": {
                                "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                                "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                                "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
                                "TGT":"C", "TGC":"C", "TGA":"*", "TGG":"W",

                                "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"S",
                                "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                                "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                                "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",

                                "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
                                "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                                "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                                "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",

                                "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                                "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                                "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                                "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                            },

                        "13": {
                                "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                                "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                                "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
                                "TGT":"C", "TGC":"C", "TGA":"W", "TGG":"W",

                                "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                                "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                                "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                                "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",

                                "ATT":"I", "ATC":"I", "ATA":"M", "ATG":"M",
                                "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                                "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                                "AGT":"S", "AGC":"S", "AGA":"G", "AGG":"G",

                                "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                                "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                                "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                                "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                            },

                        "14": {
                                "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                                "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                                "TAT":"Y", "TAC":"Y", "TAA":"Y", "TAG":"*",
                                "TGT":"C", "TGC":"C", "TGA":"W", "TGG":"W",

                                "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                                "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                                "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                                "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",

                                "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
                                "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                                "AAT":"N", "AAC":"N", "AAA":"N", "AAG":"K",
                                "AGT":"S", "AGC":"S", "AGA":"S", "AGG":"S",

                                "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                                "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                                "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                                "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                            },

                        "15": {
                                "TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
                                "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
                                "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"Q",
                                "TGT":"C", "TGC":"C", "TGA":"*", "TGG":"W",

                                "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
                                "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                                "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                                "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",

                                "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
                                "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                                "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                                "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",

                                "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
                                "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                                "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                                "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"
                            }
                    }


def translate(sequence:str, tnum:str='1') -> str:
    """Translate D/RNA to protein

    Args:
        sequence: a nucleotide sequence only comprised of ACGT...
        tnum = translation table number
    Returns:
        "amino acid string"
    """

    sequence = "".join([translation_table[tnum][sequence[i:i+3]] for i in range(0,len(sequence),3)])

    return sequence