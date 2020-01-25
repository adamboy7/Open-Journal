# Open-Journal
Open Journal is an easily customizable and searchable index of items and loot. Currently configured for Kingdom Hearts 2 Final Mix, items can be easily created or removed, added to drop tables, and can can be programmatically searched for and found in defined locations.

# How it works:

## Item Index and Enemy Index
The backbone of the journal is designed to be really simple and easy to edit. Every item, weapon, and ability is defined in item_Index.txt. Every Enemy is defined in enemy_Index.txt. The structure of any given item (Enemies follow the same format, just a different set of ID's and icons) is broken into three simple parts seperated by colons. Add a Number:Name:Number to an index and you've created and index a custom item/enemy.

<img src="https://github.com/adamboy7/Open-Journal/blob/master/readme/index.png?raw=true">

### ID# : Name : Icon

* *ID#: The number assigned to the item, usually it's position in the index starting from 0. Items don't have to be in order though and gaps are allowed. Supplied indexies are based off of in game values found in RAM using Crazycatz00's Englich Patch.*

* *Name: What you'd like to call your item/ability/enemy. Supplied names are based off of the 2.5 HD remake. Any character including spaces are allowed, except colon ":" and hashtag "#". Colon is used as the index divider, and any line with a hashtag will be treated as a comment.*

* *Icon: A number loosely corisponding to a grid of icons found in fontimage.bar on the disc itself. Enemies use a different set of icons, 1 for Heartless, 2 for Nobodies, 3 for other (Bosses and other humanoid enemies)*

## Enemy Drops
Enemy drops are defined and stored in the Drops folder. The name of the enemy is the name of the file (Case sensitive, needs to match a name in enemy_Index). The drops are defined by putting item existing ID numbers inside an enemy's file. Add an ID number to an enemy's file, it now "drops" that item.

<img src="https://github.com/adamboy7/Open-Journal/blob/master/readme/drops.png">

## World structures:
Currently enemy and item indexes are stored on the root folder. However thanks to Glob you're able to place your own worlds in the Worlds folder, populate them with chests, enemies, rewards, and have your world be automatically detected and indexed. Similar to drops, World files only use ID numbers. Names and icons are already defined in the main files. Create and name a folder in Worlds, place chests, Enemies, or rewards.txt inside and you're created a custom world.

<img src= "https://github.com/adamboy7/Open-Journal/blob/master/readme/worlds.png">

* Chests: A list of Item ID numbers corosponding to ID's found in item_Index.txt

* Enemies: A list of enemy ID numbers corosponding to ID's found in enemy_Index.txt

* Rewards: A list of Item ID numbers corosponding to ID's found in item_Index.txt

# Todo:
* **An actual GUI**
* Custom art
* Better define chest locations (World/Closest Save/Room/Coordinates maybe?)
* Impliment boss fights giving abilities
* Gummi treasures
* Impliment a texture pack system to load user supplied images (Avoid uploading copyrighted textures as much as reasonably possible)

# Wishful Thinking:
* Impliment Crazycatz00 or Xeeynamo's unpacking tool to automatically generate indexes, images, and descriptions
* *~~Become part of Xeeynamo's OpenKH project~~*
* *~~Get hired by Square Enix~~*
* *~~Get Square Enix to impliment search features into the game~~*
