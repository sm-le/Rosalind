class DistanceCalculator:
    """Wrapper object for different distance calculators"""

    @classmethod
    def h_distance(cls,
                   seq1:str,
                   seq2:str) -> int:
        """Calculate hamming distance between two given input

        Args:
            seq1: sequence 1 (or base sequence)
            seq2: sequence 2 (or sequence to compare)
        Returns:
            int(observed difference)
        """
        return sum([i!=j for i, j in zip(list(seq1), list(seq2))])

    @classmethod
    def p_distance(cls,
                   seq1:str,
                   seq2:str) -> float:
        """Calculate p distance between two given input

        Args:
            seq1: sequence 1 (or base sequence)
            seq2: sequence 2 (or sequence to compare)
        Returns:
            float(observed proportional difference)
        """
        return cls.h_distance(seq1,seq2) / len(seq1)