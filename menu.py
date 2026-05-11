

import json
import os

#menu options as varialbles
ADD = '1' 
VIEW= '2'
QUIT=''

def main():

    #menu options for users
    print('menu')
    print ('1.add')
    print ('2.save')

    #assigne user choice to a menu item 
    choice=0
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

    while session_name != ' ':

        excersice_name = input('Name of excersice:\n')
        
        sets = int(input ('number of sets' ))

        session_dict = {}
        for i in range (1,sets+1):
            set_weight= float(input(f'set {i} weight:'))
            session_dict[f'{session_name}'] = f'set {i}',set_weight

        
    
        print (f'{excersice_name:}\n')
        print (session_dict)
            
            


#placeholder for defnintion, should be 
#should read json and display it formatted.
def view_sessions():

    for i in range (5):
        print (f'session {i:}')
    
   

main()
