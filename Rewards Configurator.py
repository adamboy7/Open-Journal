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
    reward_File = open(os.path.join("Worlds", world, "rewards.txt"), "x")
    while True:
        reward_Prompt = input("Select a Reward: ")
        if reward_Prompt in Quit :
            reward_File.close()
            break
        drop = item_Lookup(reward_Prompt)
        if newLine == 0 :
            reward_File.write(str(drop))
            newLine = 1
        else:
            reward_File.write("\n" + str(drop))
except:
    print (str(world) + " already has a rewards file!")
    delete_Prompt = input("Would you like to delete " + str(world) + "'s rewards.txt?: ")
    if delete_Prompt in Yes :
        print ('Contents will be erased')
        reward_File = open(os.path.join("Worlds", world, "rewards.txt"), "w")
        while True:
            reward_Prompt = input("Select a Reward: ")
            if reward_Prompt in Quit :
                reward_File.close()
                break
            drop = item_Lookup(reward_Prompt)
            if newLine == 0 :
                reward_File.write(str(drop))
                newLine = 1
            else:
                reward_File.write("\n" + str(drop))
    if delete_Prompt in No :
        print ('Contents will be appended')
        reward_File = open(os.path.join("Worlds", world, "rewards.txt"), "a")
        while True:
            reward_Prompt = input("Select a Reward: ")
            if reward_Prompt in Quit :
                reward_File.close()
                break
            newLine = 1
            drop = item_Lookup(reward_Prompt)
            if newLine == 0 :
                reward_File.write(str(drop))
                newLine = 1
            else:
                reward_File.write("\n" + str(drop))
    if delete_Prompt in Quit :
        print ('Contents will be unchanged')
        exit()
