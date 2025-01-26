import pandas as pd
import numpy as np

# Program to log in and acces data

users = {}
is_register = 0
t = True 
data = pd.read_csv('Employee-Management.csv')

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#---------------------------------------------LOG IN MENU -------------------------------------------
while (t):
    print(""" WELCOME BACK TO THE EMPLOYEE MANAGEMENT PROGRAM ! 
            What would you like to do ? 
                    -Press '0' if you would like to would like to log in 
                    -Press '1' if you woukd like to register
                    -Press '9' if you want to exit the program """) # Display the menu for letting the user now what to do 
    
    action  = input() #what did the user choose  ? 

    if(action == '1') : # If he chose 1 , we are adding a new useername and pssw to the dictionary of the Users 
        username = input("Enter New Username :")
        passwd = input("Enter New Password :") 
        users[username]=passwd
        print(' \n Account Created Successfully \n')
    elif( action == '0'): #If he chose  to log in ...
        log_in = True# variable for starting the loop of log in until the username and pass is correct 
        failed = 0 # If they fail 2 times or more the pass , we display a menu for changing or adding a new account 
        
        while(log_in):
            username = input("Enter  Username :") 
            passwd = input("Enter  Password :")
            if username in users and users[username] == passwd: # Check if that combination of username and ppswd are in the dictionary odf users 
                print('\n Acces Granted! \n') 
                log_in = False # Exit the loop of the login
                t=False #Exit first menu 

            
            else: #If passwd or username is incorrect ...
                print('\n Wrong Username or Password , please try again ! \n')
                failed +=1 # Add +1 to the failed counter 
                if(failed >= 2) : # If the failed counter is 2 or more display a menu for changing or adding a new account 
                    sit = input('If you want to create a new account Y/N : ') 
                    if ( sit.lower() == 'y') :#If they choose to create a neew account ... 
                                username = input("Enter New Username :")
                                passwd = input("Enter New Password :") 
                                users[username]=passwd
                                print ( "\n New Username created Succesfully ! Please Log in Now . \n")
                
    elif(action == '9'):
        t=False
        print(' \n Session closed ')
    else:
         print('\n Option NOT Valid, try again! \n')

    
    

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#---------------------------------------------NAVIGATION MENU  -------------------------------------------

z = input("""SELECT OPTION 
                1 : Display and search for  data
                2 : Calculate means 
                3 : Calculate medians 
                4 : Exit 
                :""")

t = True 
while(t): 

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#---------------------------------------------IF THEY CHOOSE DISPLAY DATA ... -------------------------------------------
    if(z=='1'):#If they choose to display data ...
        x = input(" 1 : Display  first few rows         2 : Display all dataset               3: Search for  specific data      4 : Exit  \n:") 
        if(x=='1'): #Display the first few rows 
             print(data.head())
             z=input("Anything Else you want to do ? \n:")# Re-select another option 
        elif(x=='2'):#Display the whole data set 
             print(data)
             z=input("Anything Else you want to do ? \n:")# Re-select another option 
        elif(x=='3'): # Incase they choose to display specific data ... :( 
            
            opts = [ 'Department', 'Designation' , 'Hire Date'  ,'Anual Salary (USD)'] # load columns on array
            option = input(" Type option to filter : " + str(opts) + '\n') #Show the columns 
            if option in opts :  #If no spelling mistake was done ...
                
                answ = input('Do you want to see all the options available for your choice? Y/N') #Does he want to check the department
                if answ.lower() == 'y' : print(data[option].unique()) #Show unique Designations  
                filt = True
                while(filt):
                    print(data[data[option] == (input("Which one you want to filter ? "))] ) # Print that column chose
                    
                    #If they want to exit -----------------------------------------------------
                    p = input('Exit ? Y/N') #Give the user option to exit 
                    if p.lower() == 'y':# If they want to e1xit() ...  
                            print(" \n Session Closed " )
                            filt = False #exit loop 
                    #If a spelling mistake was done -----------------------------------------------
                    else : print('That option is not available ! \n')


        elif( x == '4'):
              print("Session Closed ! ")
              t = False
                         


                
                              
        
        
        
        
        else: #If they enter another number ... 
             print('Option not valid')
             z=input("Anything Else you want to do ? \n:") # Re-select another option 
    

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#---------------------------------------------IF THEY CHOSE CALCULATE MEANS ....-------------------------------------------
    elif(z=='2'):
         print('x') #If they choose to Calculate the means ... 
         
         
    
    
    
    
    
    
    elif(z=='4'):
         print("""THANK YOU FOR USING THE APP !
                    Session Closed """)
         t = False

         
                  

                
    
        
    
