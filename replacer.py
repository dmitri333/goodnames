import os, sys
import re
import unidecode

orig = sys.argv[1]

if not os.path.exists(orig):
	print("no folder to process")
	sys.exit(0)

for root, dir, files in os.walk(unicode(orig)):
    
    path = root.split('/')

    for file in files:

        originalFullName = os.path.join(root, file)

        newFileName = unidecode.unidecode(unicode(file))
        newFileName = newFileName.replace(" ", "_")
        newFileName = re.sub(r'(;|\:|\!|\?|\,)', "", newFileName)
        newFullname = os.path.join(root, newFileName)


        if originalFullName != newFullname:
            os.rename(originalFullName, newFullname)
            print("Renamed file " + repr(originalFullName) + " into " + newFullname)


