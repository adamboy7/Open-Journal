from index_Items import *
from index_Enemies import *
from index_Commands import *

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

def enemy_Lookup(Data) :
    try:
        Data = int(Data)
        if Data in enemy_ID :
            print ("Found", enemy_ID[Data])
            return (Data)
        else:
            print ('ID search not found')
            Data = input("Look up an Enemy: ")
            return enemy_Lookup(Data)
    except:
        try:
            Data = str(Data)
            if Data in enemy_ID_str :
                return enemy_ID_str[str(Data)]
            else:
                print ('Name search not found')
                Search = input("Look up an Enemy: ")
                return enemy_Lookup(Search)
        except:
            print ('Invalid Search')
            Search = input("Look up an Enemy: ")
            return enemy_Lookup(Search)

newLine = 0

enemy_Prompt = input("Select an Enemy: ")
if enemy_Prompt in Quit : exit()
Enemy = enemy_Lookup(enemy_Prompt)
try:
    enemy_Drop = open(os.path.join("Drops", str(enemy_ID[Enemy])) + ".txt", "x")
    while True :
        item_Prompt = input("What item would you like " + str(enemy_ID[Enemy]) + " to drop?: ")
        if item_Prompt in Quit :
            enemy_Drop.close()
            break
        drop = item_Lookup(item_Prompt)
        if newLine == 0 :
            enemy_Drop.write(str(drop))
            newLine = 1
        else:
            enemy_Drop.write("\n" + str(drop))
except:
    print(str(enemy_ID[Enemy]), 'already exists!')
    delete_Prompt = input("Would you like to delete " + str(enemy_ID[Enemy]) + "?: ")
    if delete_Prompt in Yes :
        print ('Contents will be erased')
        enemy_Drop = open(os.path.join("Drops", str(enemy_ID[Enemy])) + ".txt", "w")
        while True :
            item_Prompt_Delete = input("What item would you like " + str(enemy_ID[Enemy]) + " to drop?: ")
            if item_Prompt_Delete in Quit :
                enemy_Drop.close()
                break
            drop = item_Lookup(item_Prompt_Delete)
            if newLine == 0 :
                enemy_Drop.write(str(drop))
                newLine = 1
            else:
                enemy_Drop.write("\n" + str(drop))
    if delete_Prompt in No :
        print ('Contents will be appended')
        enemy_Drop = open(os.path.join("Drops", str(enemy_ID[Enemy])) + ".txt", "a")
        while True :
            item_Prompt_Append = input("What item would you like " + str(enemy_ID[Enemy]) + " to drop?: ")
            if item_Prompt_Append in Quit :
                enemy_Drop.close()
                break
            newLine = 1
            drop = item_Lookup(item_Prompt_Append)
            if newLine == 0 :
                enemy_Drop.write(str(drop))
                newLine = 1
            else:
                enemy_Drop.write("\n" + str(drop))
    if delete_Prompt in Quit :
        print ('Contents will be unchanged')
        exit()
