import os.path

Yes = list()
No = list()
Quit = list()

yes_File = open(os.path.join("Commands", "Yes.txt"), encoding='utf-8-sig')
no_File = open(os.path.join("Commands", "No.txt"), encoding='utf-8-sig')
quit_File = open(os.path.join("Commands", "Quit.txt"), encoding='utf-8-sig')

for yes_Line in yes_File :
    yes_Line = yes_Line.rstrip()
    Yes.append(yes_Line)

for no_Line in no_File :
    no_Line = no_Line.rstrip()
    No.append(no_Line)

for quit_Line in quit_File :
    quit_Line = quit_Line.rstrip()
    Quit.append(quit_Line)
