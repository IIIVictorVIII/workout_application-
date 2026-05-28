#previous session notes: worked on add session definition, didnt figure out how to store the sets and reps 
#properly to dictionary key. also figured might need to add a function that after any time quit is entered 
#the program should direct back to the main menu. also watch a video about using json in python. 

import json
import os

#menu options as varialbles to be used through out the program.
ADD = 1 
VIEW= 2
QUIT=' '

#main establises what the users choice is and executes corresponding menu item.
def main():
    
    #starting variables
    session= {}
    choice= 0

    #assigns user choice to a menu item 
    while choice != QUIT:
        
        choice= menu_choice()

        if choice == ADD:
            add_sessions(session)
        elif choice == VIEW:
            view_sessions(session) 
    print ('gg')
    print (session)
    
def menu_choice(): 

    #menu options for users
    print('menu')
    print ('1.add')
    print ('2.VIEW')

    choice = int(input('Enter menu choice: '))

    while choice < ADD or choice > VIEW : 
        choice= int(input('enter valid choice: '))

    return choice

#should ask user for workount information and add to json file as a dictionary.
def add_sessions(session):
    
    session_name= input('Workout name: ')    
    
  
    while session_name != QUIT:
        
        excersice_name = input('enter excersice name: ')

        looping = 'y'
        set= 1
        weight = []
        reps = []

        while looping == 'y':
            set_weight= float(input(f'weight for set {set} (4 to quit): '))
            if set_weight== 4:
                looping = 'n'
            else: 
                weight.append(set_weight)
                weight_reps = float(input('enter set reps: '))
                reps.append(weight_reps)        
                set+=1
            #should figure out how to format dictionary loop should work for getting user values, need to also tweak
            #how this nested loop works
            
        
    
           

#will be updated. 
def view_sessions(session):

    for i in range (5):
        print (f'session {i:}')



main()
