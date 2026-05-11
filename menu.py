#previous session notes: worked on add session definition, didnt figure out how to store the sets and reps 
#properly to dictionary key. also figured might need to add a function that after any time quit is entered 
#the program should direct back to the main menu. also watch a video about using json in python. 

import json
import os

#menu options as varialbles to be used through out the program.
ADD = '1' 
VIEW= '2'
QUIT=''

#main establises what the users choice is and executes corresponding menu item.
def main():

    #menu options for users
    print('menu')
    print ('1.add')
    print ('2.save')

    #assigns user choice to a menu item 
    
    while choice != quit:
        choice= input('Enter choice (Enter to quit):')

        if choice == ADD:
            add_sessions()
        elif choice == VIEW:
            view_sessions()

#should ask user for workount information and add to json file as a dictionary.
def add_sessions():
    
    session_name= input('Workout name:\n')    
    excercise_count= 0 

    #if users input is enter the program should exit
    # --add a way that if quits goes back to main menu.  
    while session_name != ' ':
        
        #establish initial workout information 
        excersice_name = input('Name of excersice:\n')
        sets = int(input ('number of sets' ))

        #figure out how to send sets and weights all into the dictionary beore then adding it to a json 
        #that will store all workout and workout details 
        session_dict = {}
        for i in range (1,sets+1):
            set_weight= float(input(f'set {i} weight:'))
            session_dict[f'{session_name}'] = session_dict.append(f'set {i}',set_weight)

        

    #test the dictionary is stored properly
        print (f'{excersice_name:}\n')
        print (session_dict)
            
            


#placeholder for defnintion, should be 
#should read json and display it formatted.
def view_sessions():

    for i in range (5):
        print (f'session {i:}')
    
   

main()
