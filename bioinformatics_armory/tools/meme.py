#################################################
# MEME
# by smlee

######################
# CUSTOM SCRIPT IMPORT

#############################
# PYTHON NATIVE MODULE IMPORT
import subprocess

def meme_cmd(file:str, out_path:str, minw:int=15, maxw:int=50):
    """Command for meme
    
    Args:
        file: file
        out_path: output path
        minw: minimum width
        maxw: maximum width
    """

    cmd = f"meme {file} " \
          f"-o {out_path} " \
          f"-minw {minw} " \
          f"-maxw {maxw} " \
          f"-nostatus"
    
    return cmd

def meme(file:str, out_path:str, minw:int=15, maxw:int=50):
    """Run MEME
    
    Args:
        file: file
        out_path: output path
        minw: minimum width
        maxw: maximum width
    """

    cmd = meme_cmd(file, out_path, minw, maxw)

    subprocess.call(cmd, shell=True)

    return f"{out_path}meme.txt"


