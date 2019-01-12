# Script that searches all .pdf files on mentioned disk. [For now this scripts will work only on win os].

import os

def dirThrough(text):
    for root, dirs, files in os.walk(text):
        for file in files:
            if file.endswith('pdf'):
                print(os.path.join(root, file))

os.chdir('E:\\')                    # Type any Disc name that u want to research
currentPath = os.getcwd()
print('\nLets search in the current directory, which is: %s\n' % currentPath)
print(dirThrough(currentPath))
