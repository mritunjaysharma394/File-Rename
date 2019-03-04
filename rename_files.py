import os
import string
def rename_files():
    
    filename = os.listdir(r"C:\Users\Mritunjay Sharma\Downloads\prank\prank")
    

    for files in filename:
        os.chdir(r"C:\Users\Mritunjay Sharma\Downloads\prank\prank")
        tab=files.maketrans("0123456789","          ","0123456789")
        os.rename(files,files.translate(tab))
        
         

    
rename_files()
