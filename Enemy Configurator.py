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
    reward_File = open(os.path.join("Worlds", world, "enemies.txt"), "x")
    while True:
        reward_Prompt = input("Select an Enemy: ")
        if reward_Prompt in Quit :
            reward_File.close()
            break
        drop = enemy_Lookup(reward_Prompt)
        reward_File.write(str(drop))
except:
    print (str(world) + " already has am Enemies file!")
    delete_Prompt = input("Would you like to delete " + str(world) + "'s enemies.txt?: ")
    if delete_Prompt in Yes :
        print ('Contents will be erased')
        reward_File = open(os.path.join("Worlds", world, "enemies.txt"), "w")
        while True:
            reward_Prompt = input("Select an Enemy: ")
            if reward_Prompt in Quit :
                reward_File.close()
                break
            drop = enemy_Lookup(reward_Prompt)
            reward_File.write(str(drop))
    if delete_Prompt in No :
        print ('Contents will be appended')
        reward_File = open(os.path.join("Worlds", world, "enemies.txt"), "a")
        while True:
            reward_Prompt = input("Select an Enemy: ")
            if reward_Prompt in Quit :
                reward_File.close()
                break
            newLine = 1
            drop = enemy_Lookup(reward_Prompt)
            if newLine == 0 :
                reward_File.write(str(drop))
                newLine = 1
            else:
                reward_File.write("\n" + str(drop))
    if delete_Prompt in Quit :
        print ('Contents will be unchanged')
        exit()
