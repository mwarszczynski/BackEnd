# Script that searches all .pdf files on mentioned disk [For now this scripts will work only on win os].
import os

def dirThrough(text, counter=0):
    for root, dirs, files in os.walk(text):
        for file in files:
            if file.endswith(fileType):
                counter += 1
                print('['+str(counter)+']. ', os.path.join(root, file))

fileType = input('\nType the file that You want to find: \n')
c = input('\nType the path of Your disc which You want to research: \t\t(example " D:\\ ". )\n')
d = 'Total: '

os.chdir(c)
currentPath = os.getcwd()
print('\nLets search pdf file in the current path, which is: %s\n' % currentPath)
print(dirThrough(currentPath))

input('Press enter to close program')






