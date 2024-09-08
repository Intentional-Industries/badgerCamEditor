# this script will clean up files if the process is interupted

import os
import shutil

# Define your directories
source_dir = os.path.expanduser('~/Movies/BadgerCam/apr-may-23')
target_dir = os.path.expanduser('~/Movies/BadgerCam/deleteMe')

# List of unprocessed files
unprocessed_files = [
    "DSCF0001.AVI", "DSCF0002.AVI", "DSCF0003.AVI", "DSCF0007.AVI", "DSCF0013.AVI", "DSCF0014.AVI", 
    "DSCF0015.AVI", "DSCF0016.AVI", "DSCF0017.AVI", "DSCF0028.AVI", "DSCF0029.AVI", "DSCF0048.AVI", 
    "DSCF0049.AVI", "DSCF0058.AVI", "DSCF0059.AVI", "DSCF0060.AVI", "DSCF0061.AVI", "DSCF0062.AVI", 
    "DSCF0063.AVI", "DSCF0064.AVI", "DSCF0065.AVI", "DSCF0066.AVI", "DSCF0067.AVI", "DSCF0070.AVI", 
    "DSCF0071.AVI", "DSCF0072.AVI", "DSCF0073.AVI", "DSCF0074.AVI", "DSCF0075.AVI", "DSCF0076.AVI", 
    "DSCF0077.AVI", "DSCF0088.AVI", "DSCF0089.AVI", "DSCF0098.AVI", "DSCF0099.AVI", "DSCF0100.AVI", 
    "DSCF0101.AVI", "DSCF0102.AVI", "DSCF0103.AVI", "DSCF0104.AVI"
]

# Ensure the target directory exists
os.makedirs(target_dir, exist_ok=True)

# Move processed files (those not in unprocessed_files)
for filename in os.listdir(source_dir):
    # Check if the file is an AVI file and not in the unprocessed list
    if filename.endswith(".AVI") and filename not in unprocessed_files:
        source_file = os.path.join(source_dir, filename)
        target_file = os.path.join(target_dir, filename)
        
        # Move the file
        shutil.move(source_file, target_file)
        print(f"Moved {filename} to {target_dir}")

print("Processed files moved successfully.")

