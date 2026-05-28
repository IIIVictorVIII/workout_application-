
session_name = {}
excersiceinfo = {}
weightxreps= {}

nameOfSession= input('sessionn name: ')
name= input('excersice name: ')

set=1
while True:
    
    print(f'set{set}')
    weight= float(input('how much weight (0 to quit): '))
    if weight== 0:
        reps = 0
        break
    reps = float(input('for how many reps(0 to quit): '))
    if reps == 0:
        weight= 0
        break
    weightxreps.update({weight:reps})
    set+=1

weightxreps.update({weight:reps})
excersice= {name: weightxreps}

excersiceinfo.update(excersice)
session_name.update({nameOfSession:excersiceinfo})
print (session_name)