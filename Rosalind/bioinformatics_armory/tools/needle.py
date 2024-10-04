#################################################
# NEEDLE
# by smlee

######################
# CUSTOM SCRIPT IMPORT

#############################
# PYTHON NATIVE MODULE IMPORT
import subprocess

def needle_cmd(ap:str, bp:str, outp:str, open_penalty:int=10, extend_penalty:int=1) -> str:
    """Command arguments for NEEDLE program

    Args:
        ap: A sequence
        bp: B sequence
        outp: out path
        open_penalty: gap open penalty
        extend_penalty: gap extend penalty
    """

    cmd = f"needle " \
          f"-asequence {ap} " \
          f"-bsequence {bp} " \
          f"-gapopen {open_penalty} " \
          f"-gapextend {extend_penalty} " \
          f"-endweight Y " \
          f"-endopen 10 " \
          f"-endextend 1 " \
          f"-outfile {outp}"
    
    return cmd

def needle(ap:str, bp:str, outp:str, open_penalty:int=10, extend_penalty:int=1) -> str:
    """Run NEEDLE
    
    Args:
        ap: A sequence
        bp: B sequence
        outp: out path
        open_penalty: gap open penalty
        extend_penalty: gap extend penalty
    """

    cmd = needle_cmd(ap, bp, outp, open_penalty, extend_penalty)

    subprocess.call(cmd, shell=True)

    return f"{outp}"
