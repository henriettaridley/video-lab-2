import os
import urllib.request
import rarfile

UCF50_URL = 'https://www.crcv.ucf.edu/data/UCF50.rar'
UCF50_PATH = 'datasets/UCF50.rar'

# Step 1: Download the entire UCF50 dataset
# print('Downloading UCF50 dataset...')
# urllib.request.urlretrieve(UCF50_URL, UCF50_PATH)
# print('Download complete!')

# Step 2: Extract the dataset
with rarfile.RarFile(UCF50_PATH) as rf:
    print('Extracting UCF50 dataset...')
    rf.extractall()
    print('Extraction complete!')

# Cleanup UCF50 RAR file
os.remove(UCF50_PATH)