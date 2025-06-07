import glob
import os.path

line_Count = 0
name_Temp = str()

worlds = list()

chests = dict()
chests_Temp = list()
rewards = dict()
rewards_Temp = list()
enemies = dict()
enemies_Temp = list()

for filename in glob.glob(os.path.join("Worlds", "*")) :
    worlds.append(str(filename[7:]))
    name_Temp = str(filename[7:])
    chests_Temp = list()
    rewards_Temp = list()
    enemies_Temp = list()
    try:
        with open(os.path.join("Worlds", name_Temp, "chests.txt"), encoding='utf-8-sig') as file_Chests:
            line_Count = 0
            for line in file_Chests:
                line_Count += 1
                line = line.strip()
                try:
                    line = int(line)
                    chests_Temp.append(line)
                except Exception:
                    print('Invalid drop in', os.path.join(filename, 'chests.txt'), 'Line:', line_Count)
                    continue
        chests[name_Temp] = chests_Temp
    except Exception:
        print('No chests found in', name_Temp)
        chests[name_Temp] = chests_Temp
    try:
        with open(os.path.join("Worlds", name_Temp, "rewards.txt"), encoding='utf-8-sig') as file_Rewards:
            line_Count = 0
            for line in file_Rewards:
                line_Count += 1
                line = line.strip()
                try:
                    line = int(line)
                    rewards_Temp.append(line)
                except Exception:
                    print('Invalid drop in', os.path.join(filename, 'rewards.txt'), 'Line:', line_Count)
                    continue
        rewards[name_Temp] = rewards_Temp
    except Exception:
        print('No rewards found in', name_Temp)
        rewards[name_Temp] = rewards_Temp

    try:
        with open(os.path.join("Worlds", name_Temp, "enemies.txt"), encoding='utf-8-sig') as file_Enemies:
            line_Count = 0
            for line in file_Enemies:
                line_Count += 1
                line = line.strip()
                try:
                    line = int(line)
                    enemies_Temp.append(line)
                except Exception:
                    print('Invalid drop in', os.path.join(filename, 'enemies.txt'), 'Line:', line_Count)
                    continue
        enemies[name_Temp] = enemies_Temp
    except Exception:
        print('No enemies found in', name_Temp)
        enemies[name_Temp] = enemies_Temp
