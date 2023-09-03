import os
from pprint import pprint
import time
'''
In the data/ directory,
For each subdirectory
    For each sub-subdirectory
        Rename it to '{sub_dir}_{subsub_dir}'
        Take the subsub_dir out of the sub_dir, and place it in 'data'
    After the inner loop, the subdir should be empty and we can remove it
'''
PATH = r'data' # Relative path
for s in os.listdir(PATH):
    subdir_path = os.path.join(PATH, s)
    for ss in os.listdir(subdir_path):
        pprint(f'Before: {ss}')
        ss = f'{s}_{ss}' # 
        pprint(f'After: {ss}')
        os.rename(os.path.join(subdir_path, ss), os.path.join(PATH, ss))
    # os.remove(subdir_path) # Commented out for safety