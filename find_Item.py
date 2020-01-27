from index_Items import *
from index_Enemies import *
from index_Commands import *
from index_Worlds import *

import glob
import os.path

temp_File = None

def item_Lookup(Data) :
    try:
        Data = int(Data)
        if Data in ID :
            print ("Found", ID[Data])
            return (Data)
        else:
            print ('ID search not found')
            Search = input("Look up an Item: ")
            return item_Lookup(Search)
    except:
        try:
            Data = str(Data)
            if Data in ID_str :
                return ID_str[str(Data)]
            else:
                print ('Name search not found')
                Search = input("Look up an Item: ")
                return item_Lookup(Search)
        except:
            print ('Invalid Search')
            Search = input("Look up an Item: ")
            return item_Lookup(Search)

while True :
    Search = input("What do you want to find?: ")
    if Search in Quit : exit()
    find = item_Lookup(Search)

    for filename in glob.glob(os.path.join("Drops", "*.txt")) :
        temp_File = open(filename, "r")
        for line in temp_File :
            line = line.strip()
            if str(find) == str(line) :
                print (filename[6:-4])
                break
