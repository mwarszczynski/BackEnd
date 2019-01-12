# Script that searches all .pdf files on mentioned disk [For now this scripts will work only on win os].
import os

def dirThrough(text):
    for root, dirs, files in os.walk(text):
        for file in files:
            if file.endswith('pdf'):
                print(os.path.join(root, file))

c = input('\nType the path of Your disc which You want to research: \t\t(write like " D:\\ ". )\n')

os.chdir(c)
currentPath = os.getcwd()
print('\nLets search pdf file in the current path, which is: %s\n' % currentPath)
print(dirThrough(currentPath))






