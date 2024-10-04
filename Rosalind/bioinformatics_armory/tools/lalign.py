#################################################
# LALIGN
# by smlee

######################
# CUSTOM SCRIPT IMPORT

#############################
# PYTHON NATIVE MODULE IMPORT
import subprocess

def lalign_cmd(ap:str, bp:str, outp:str) -> str:
    """Command arguments for LALIGN program

    Args:
        ap: A sequence
        bp: B sequence
        outp: out path
    """

    cmd = f"lalign36 " \
          f"{ap} " \
          f"{bp} " \
          f"-O {outp}"
    
    return cmd

def lalign(ap:str, bp:str, outp:str) -> str:
    """Run LALIGN
    
    Args:
        ap: A sequence
        bp: B sequence
        outp: out path
    """

    cmd = lalign_cmd(ap, bp, outp)

    subprocess.call(cmd, shell=True)

    return f"{outp}"
