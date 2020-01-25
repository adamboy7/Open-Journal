line_Count = 0
ID = dict()
ID_str = dict()
Icon = dict()

file = open('item_Index.txt', encoding='utf-8-sig')

for line in file :
    line_Count = line_Count + 1
    if str(':') not in line: continue
    line = line.rstrip()
    line = line.split(':')
    try:
        ID.update({int(line[0]) : str(line[1])})
        ID_str.update({str(line[1]) : int(line[0])})
        Icon.update({int(line[0]) : int(line[2])})
    except:
        print ('Invalid Index Entry at Line', line_Count)
