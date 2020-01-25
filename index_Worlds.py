import glob
import os.path

line_Count = 0

chests = dict()
name_Temp = str()
chests_Temp = list()
#Todo
enemies = dict()
enemies_Temp = list()

for filename in glob.glob(os.path.join("Worlds", "*")) :
    name_Temp = str(filename[7:])
    chests_Temp = list()
    try:
        file = open(os.path.join("Worlds", name_Temp, "chests.txt"), encoding='utf-8-sig')
    except:
        print ('No chests found in', name_Temp)
        chests[name_Temp] = chests_Temp
        continue

    line_Count = 0
    for line in file :
        line_Count = line_Count + 1
        line = line.strip()
        try:
            line = int(line)
            chests_Temp.append(line)
        except:
            print ('Invalid drop in', filename + 'Chests.txt', 'Line:', line_Count)
            continue
    chests[name_Temp] = chests_Temp
