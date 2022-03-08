# /volume1/WaweLab/Wawe Confocal - All Users
# Wawersik Confocal - Olympus Folder  (transferred)
# Wawersik Confocal - Users Folder  (transferred)
# /volume2/LabData
# /volume2/LabData/Additional stuff/Wawersik Confocal - Users Folder


import os
oldNAS = '/volume2/LabData/Additional stuff/Wawersik Confocal - Olympus Folder'
outfile = "/volume2/LabData/derek_dir/olympus_NEW.txt"
# print(oldNAS)
# print(os.walk(oldNAS))

filelist = []

for root, dirs, files in os.walk(oldNAS):
    for file in files:
        #append the file name to the list
        filelist.append(os.path.join(root,file))
# print filelist
print("Step one complete, file list compiled")

with open(outfile, 'w') as file:
     for name in filelist:
        # print name
        name = name.split('Wawersik Confocal - Olympus Folder')[1]
        file.write(name + '\n')
print("Step two complete, file written to" + outfile)

