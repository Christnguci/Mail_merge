 #TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os
path_invited_name = r'Input\Names\invited_names.txt'
with open(path_invited_name,'r') as name :
    names=name.readlines()

path_letter = r'Input\Letters\starting_letter.txt'
with open(path_letter,'r') as letters:
    letter=letters.read()
folder_send =r'Output\ReadyToSend'
for name in names :
    name=name.strip("\n")
    member_letter=letter
    member_letter=member_letter.replace("[name]",name)
    with open(os.path.join(folder_send,r"Letter_for_{}.txt".format(name)),'w') as readytosend:
        readytosend.write(member_letter)
        



