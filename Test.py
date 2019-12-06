import os
import time

def getSize(file_path):
    st = os.stat(file_path).st_size
    current_size = st
    
    time.sleep(5)
    
    while (st != os.stat(file_path).st_size):
        time.sleep(0.5)
    
    return True

print (getSize("/mnt/c/Users/Me/Downloads/"))