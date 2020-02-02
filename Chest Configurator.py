from index_Commands import *
from index_Items import *
from index_Worlds import *

import glob
import os.path

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

def world_Lookup(Data) :
    if Data in worlds :
        return (Data)
    else:
        print ("World name not found")
        Search = input("Look up a world: ")
        return world_Lookup(Search)

newLine = 0

world_Prompt = input("Select a World: ")
if world_Prompt in Quit :
    exit()
world = world_Lookup(world_Prompt)
try:
    chest_File = open(os.path.join("Worlds", world, "chests.txt"), "x")
    while True:
        chest_Prompt = input("Select an item: ")
        if chest_Prompt in Quit :
            chest_File.close()
            break
        drop = item_Lookup(chest_Prompt)
        if newLine == 0 :
            chest_File.write(str(drop))
            newLine = 1
        else:
            chest_File.write("\n" + str(drop))
except:
    print (str(world) + " already has a chests file!")
    delete_Prompt = input("Would you like to delete " + str(world) + "'s chests.txt?: ")
    if delete_Prompt in Yes :
        print ('Contents will be erased')
        chest_File = open(os.path.join("Worlds", world, "chests.txt"), "w")
        while True:
            chest_Prompt = input("Select an item: ")
            if chest_Prompt in Quit :
                chest_File.close()
                break
            drop = item_Lookup(chest_Prompt)
            if newLine == 0 :
                chest_File.write(str(drop))
                newLine = 1
            else:
                chest_File.write("\n" + str(drop))
    if delete_Prompt in No :
        print ('Contents will be appended')
        chest_File = open(os.path.join("Worlds", world, "chests.txt"), "a")
        while True:
            chest_Prompt = input("Select an item: ")
            if chest_Prompt in Quit :
                chest_File.close()
                break
            newLine = 1
            drop = item_Lookup(chest_Prompt)
            if newLine == 0 :
                chest_File.write(str(drop))
                newLine = 1
            else:
                chest_File.write("\n" + str(drop))
    if delete_Prompt in Quit :
        print ('Contents will be unchanged')
        exit()
