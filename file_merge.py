#Please ensure the modules are installed
from datetime import datetime
import glob2
import os
import time
print(os.getcwd())
new_dir = input("enter the directory:")
files_to_merge = input("Enter the files that needs to be merged(regex supported):")
os.chdir(new_dir)
print(os.getcwd())
print(os.listdir(new_dir))
filenames = glob2.glob(files_to_merge)
with open(datetime.now().strftime("merged"+"%Y-%m-%d-%H-%M-%S-%f")+".txt",'w') as file:
    for filename in filenames:
        with open(filename,"r") as f:
            file.write(filename + "\n" + f.read()+"\n")
time.sleep(5.5)