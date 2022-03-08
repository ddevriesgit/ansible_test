import os

# /volume1/WaweLab/Wawe Confocal - All Users

oldNAS = '/volume1/WaweLab/Wawe Confocal - All Users/Wawersik Lab  (transferred)'
outfile = "/volume1/WaweLab/Wawe Confocal - All Users/all_files_list.txt"
# print(oldNAS)
# print(os.walk(oldNAS))

filelist = []

for root, dirs, files in os.walk(oldNAS):
    for file in files:
        #append the file name to the list
        filelist.append(os.path.join(root,file))
print "Step one complete, file list compiled"

with open(outfile, 'w') as file:
    for name in filelist:
        # print name
        name = name.split('Wawersik Lab  (transferred)')[1]
        file.write(name + '\n')
print "Step two complete, file written to" + outfile
