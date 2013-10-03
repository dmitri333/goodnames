import os, sys
import re
import unidecode

orig = sys.argv[1]

def nameChange(name):

    newFileName = unidecode.unidecode(unicode(name))
    newFileName = newFileName.replace(" ", "_")
    newFileName = re.sub(r'(;|\:|\!|\?|\,)', "", newFileName)

    return newFileName


if not os.path.exists(orig):
	print("no folder to process")
	sys.exit(0)

# first files
for root, dir, files in os.walk(unicode(orig)):
    
    for file in files:

        originalFullName = os.path.join(root, file)

        newFileName = nameChange(file)
        newFullname = os.path.join(root, newFileName)

        if originalFullName != newFullname:
            os.rename(originalFullName, newFullname)
            print("Renamed file " + repr(originalFullName) + " into " + repr(newFullname))


# now directories
while True:

    renameDone = False

    for root, dir, files in os.walk(unicode(orig)):
        for d in dir:
            newDirName = nameChange(d)
            if newDirName != d:

                fullDirName = os.path.join(root, d)
                newFullDirName = os.path.join(root, newDirName)
                os.rename(fullDirName, newFullDirName)
                print("Renamed directory from " + repr(fullDirName) + " to "  + repr(newFullDirName))
                renameDone = True
          
    if renameDone == False: break            