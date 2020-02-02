from index_Commands import *
from index_Enemies import *
from index_Worlds import *

import glob
import os.path

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

def world_Lookup(Data) :
    if Data in worlds :
        return (Data)
    else:
        Search = input("Look up a world: ")
        return world_Lookup(Search)

newLine = 0

world_Prompt = input("Select a World: ")
if world_Prompt in Quit :
    exit()
world = world_Lookup(world_Prompt)
try:
    enemy_File = open(os.path.join("Worlds", world, "enemies.txt"), "x")
    while True:
        enemy_Prompt = input("Select an Enemy: ")
        if enemy_Prompt in Quit :
            enemy_File.close()
            break
        enemy = enemy_Lookup(enemy_Prompt)
        if newLine == 0 :
            enemy_File.write(str(enemy))
            newLine = 1
        else:
            enemy_File.write("\n" + str(enemy))
except:
    print (str(world) + " already has am Enemies file!")
    delete_Prompt = input("Would you like to delete " + str(world) + "'s enemies.txt?: ")
    if delete_Prompt in Yes :
        print ('Contents will be erased')
        enemy_File = open(os.path.join("Worlds", world, "enemies.txt"), "w")
        while True:
            enemy_Prompt = input("Select an Enemy: ")
            if enemy_Prompt in Quit :
                enemy_File.close()
                break
            enemy = enemy_Lookup(enemy_Prompt)
            if newLine == 0 :
                enemy_File.write(str(enemy))
                newLine = 1
            else:
                enemy_File.write("\n" + str(enemy))
    if delete_Prompt in No :
        print ('Contents will be appended')
        enemy_File = open(os.path.join("Worlds", world, "enemies.txt"), "a")
        while True:
            enemy_Prompt = input("Select an Enemy: ")
            if enemy_Prompt in Quit :
                enemy_File.close()
                break
            newLine = 1
            enemy = enemy_Lookup(enemy_Prompt)
            if newLine == 0 :
                enemy_File.write(str(enemy))
                newLine = 1
            else:
                enemy_File.write("\n" + str(enemy))
    if delete_Prompt in Quit :
        print ('Contents will be unchanged')
        exit()
