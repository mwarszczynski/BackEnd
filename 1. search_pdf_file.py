# Script that searches all .pdf files on mentioned disk

import os

def dirThrough(text):
    for root, dirs, files in os.walk(text):
        for file in files:
            if file.endswith('pdf'):
                print(os.path.join(root, file))

os.chdir('E:\\')
currentPath = os.getcwd()
print('\nLets search in the current directory, which is: %s\n' % currentPath)
print(dirThrough(currentPath))