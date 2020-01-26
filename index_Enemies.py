line_Count = 0
enemy_ID = dict()
enemy_ID_str = dict()
enemy_Emblem = dict()

file = open('enemy_Index.txt', encoding='utf-8-sig')

for line in file :
    line_Count = line_Count + 1
    if str(':') not in line: continue
    if str('#') in line: continue
    line = line.rstrip()
    line = line.split(':')
    try:
        enemy_ID.update({int(line[0]) : str(line[1])})
        enemy_ID_str.update({str(line[1]) : int(line[0])})
        enemy_Emblem.update({int(line[0]) : int(line[2])})
    except:
        print ('Invalid Index Entry at Line', line_Count)
