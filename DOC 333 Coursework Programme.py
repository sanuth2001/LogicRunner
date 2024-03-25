count = 1
value = 0
repeat=True
number=0
kill=0

while repeat==True:
#input_name
    uname = str(input("\nEnter your name :"))
    print("\n\t\t\t\t\t\t\t\t\t...Hello Welcome",uname,"to Game Int...")
    print("\nNumber to Guess - (* * * *)\t\t\t\t\t\t\t\t\t\t\t\t\t\tColour Mapping : 1-White 2-Blue 3-Red")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t 4-Yellow 5-Green 6-Purple")

#input_random_list
    import random
    random_list= []
    new_list=[]
    user_list= []
    for i in range(0,4):
        random_list.append(random.randint(1,6))
        

    print("\n\n\t\t\t\t\t\tAttempt No\t\t\t\t\t\tGuess\t\t\t\t\t\t\tResults")
    
    count=1
    while count <= 8 and random_list != new_list:
        print ("\n\n\t\t\t\t\t\t",count)
        
    
#Getting_inputs
        message=""
        user_list = list(input("Enter the Guesses :\t\t\t\t\t\t\t\t\t\t\t"))
        while len(user_list)!=4:
            print("\t\t\t...Invalied Guess...")
            user_list=list(input("\nEnter four digit guess : \t\t\t\t\t\t\t\t\t\t"))

        for slot in range(4):
            while user_list[slot] not in ["0","1","2","3","4","5","6"]:
                print("\t\t\t...Invalied Guess...")
                user_list=list(input("\nEnter guesses between 1 - 6 !!! \t\t\t\t\t\t\t\t\t"))
    
        new_list=[int(number)for number in user_list]

        text=0
        for kill in range(0,4):
            if new_list[kill]==0:
                text=text+1
            else:
                pass
        if text==4:
            exit()
        else:
            pass

        if random_list == new_list:
            print ("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  \t1111\n\t\t\t\t\t\tCongratulations!!!!!   You have won the game...")
        else:
#compare_1st_spot
            
            message=""
            if new_list[0] not in random_list:
                message=message+"."
            elif new_list[0] != random_list[0]:
                message=message+"0"
            else:
                message=message+"1"

    

#compare_2nd_spot
    
            if new_list[1] not in random_list:
                message=message+"."
            elif new_list[1] != random_list[1]:
                message=message+"0"
            else:
                message=message+"1"

#compare_3rd_spot

            if new_list[2] not in random_list:
                message=message+"."
            elif new_list[2] != random_list[2]:
                message=message+"0"
            else:
                message=message+"1"

#compare_4th_spot
    
            if new_list[3] not in random_list:
                message=message+"."
            elif new_list[3] != random_list[3]:
                message=message+"0"
            else:
                message=message+"1"
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",message)
            count=count + 1    

    else:
        if new_list==random_list:
            print("\n\t\t\t\t\t\tYou scored 100 points")
        else:
            print ("\n\t\t\t\t\t\t\t\t\t\tYou lost \n\n\t\t\t\t\t\t\t\t\t\tYou scored 00 points")
        
        
    temp1 = True         
    while temp1 == True:
    
        rep= str(input("\nDo you want to play again? \npress Y to Play again &  N to End  "))
        if rep== "Y":
            repeat=True
            temp1 = False
        elif rep== "N" :
            repeat = False
            temp1 = False 
            print ("\t\t\t\t\t\t\t\t\t\tThanks for playing...")    
        else:
            print ("\t\t\t\t\t\t\t\t\t\tInvalied Input")
            temp1=True
    
        

        

    
    


