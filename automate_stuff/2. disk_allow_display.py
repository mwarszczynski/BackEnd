# The script is used for: search .BAK (snapshot) file, compress and save at mentioned path.
import os, os.path

diskSummary = []
choosenDisc = []
typeOfFile = ['pdf','txt']#,'xml','json','html','css','doc','csv','xlsx'
possibleDiskChar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def checkDisc():
    drives = ['%s: ' % x for x in possibleDiskChar if os.path.exists('%s:' % x)]
    for x in drives:
        diskSummary.append(str(x))

def displayDisk():
    for x in diskSummary:
        print(f'Founded hard drive on Your computer {x}')

    while True:
        c = input('Choose disc that You want to scan: \n')
        if c == 'C:' or 'C':
            # print('Choosen: C')
            choosenDisc.append(c)
            break
        elif c == 'D:' or 'D':
            # print('Choosen: D')
            choosenDisc.append(c)
            break
        else:
            print('Cannot find mentioned disc')

# Function scan looking for Your discs on local computer, and appending it to a 'diskSummary' list.
print(checkDisc())
# Function displays available disc.
print(displayDisk())

# Loop displays the disc that were choosen by user
for i in range(len(choosenDisc)):
    print(choosenDisc)























