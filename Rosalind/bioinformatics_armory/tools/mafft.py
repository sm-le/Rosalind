#################################################
# Running MAFFT
# by smlee

######################
# CUSTOM SCRIPT IMPORT

#############################
# PYTHON NATIVE MODULE IMPORT
import subprocess

def mafft_cmd(file:str, outp:str) -> str:
    """Command arguments for MAFFT program

    Args:
        file: sequences in fasta format
        outp: out path
    """

    cmd = f"mafft " \
          f"{file} " \
          f"> {outp}"
    
    return cmd

def mafft(file:str, outp:str) -> str:
    """run MAFFT program

    Args:
        file: sequences in fasta format
        outp: out path
    """

    cmd = mafft_cmd(file, outp)

    subprocess.call(cmd, shell=True)

    return f"{outp}"
