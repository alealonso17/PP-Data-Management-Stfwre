import pandas as pd #for reading data
import numpy as np #for mean and median
import getpass # fo hidding password 

opts = [ 'Department', 'Designation' , 'Hire Date'  ]#Load esential data into str 
print(" WELCOME  TO THE EMPLOYEE MANAGEMENT PROGRAM ! \n ")
# Program to log in and acces data

users = {'admin' : 'RGU'}
is_register = 0
t = True 
data = pd.read_csv('Employee-Management.csv')

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#---------------------------------------------LOG IN MENU -------------------------------------------
while (t):
    print(""" 
                    -Press '0' : Log In 
                    -Press '1' : Register
                    -Press '9':  Exit """) # Display the menu for letting the user now what to do 
    
    action  = input() #what did the user choose  ? 

    if(action == '1') : # If he chose 1 , we are adding a new useername and pssw to the dictionary of the Users 
        username = input("Enter New Username :")
        passwd = getpass.getpass("Enter New Password :") 
        users[username]=passwd
        print(' \n Account Created Successfully \n')
    elif( action == '0'): #If he chose  to log in ...
        log_in = True# variable for starting the loop of log in until the username and pass is correct 
        failed = 0 # If they fail 2 times or more the pass , we display a menu for changing or adding a new account 
        
        while(log_in):
            username = input("Enter  Username :") 
            passwd = getpass.getpass("Enter  Password :") 
            
            
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#---------------------------------------------OPTIONS FOR ADMIN-------------------------------------------
            if username == 'admin' and passwd == users[username] :
                print("ADMIN PRIVILEGE TAKEN : ")
                admin = True
                while(admin):
                    nn = input ('Choose an option : \n 1 : Explore admin privileges \n 2 : Skip and go to menu \n: ')
                    if  nn == '1' :
                            b = input('''\n Choose your option : 
                                        1 : Explore Registered Users 
                                        2 : Delete a User
                                        3 : Go back to menu    \n:''' )
                            if (b=='1'):print("List of Users format { username : passwd } \n" + str(users) + '\n')
                            elif(b == '2') :  # If they choose to delete a user ... 
                                delete = input('Enter the Username of the account you want to delete  : ')
                                if (delete == 'admin') : print("You cannot delete the admin account")    # If tehy think they are smart and they try to delete the admin ...                     
                                elif delete in users:  # else delete that user 
                                    del users[delete] 
                                    print("User Deleted Succesfully!")
                                else : print("User NOT Found ! ") #If a spelling error was made 
                            elif(b == '3'): 
                                admin = False # If they choose to go back to the menu 
                                continue 
                    if nn == '2': admin = False #If they choose to skip and go to the menu 
                                
                

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
                                passwd = getpass.getpass("Enter New Password :")  
                                users[username]=passwd
                                print ( "\n New Username created Succesfully ! Please Log in Now . \n")
                
    elif(action == '9'):
        t=False
        print(' \n Session closed ')
        quit
    else:
         print('\n Option NOT Valid, try again! \n')

    
    

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#---------------------------------------------NAVIGATION MENU  -------------------------------------------
menu = True
while(menu): #Menu loope  incase they want to go bck to the menu 
    z = input("""SELECT OPTION 
                    1 : Display and search for specific data
                    2 : Calculate Specific means 
                    3 : Calculate Specific medians 
                    4 : Exit 
                    :""")

    t = True 
    while(t): # loop for displaying data 

    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    #---------------------------------------------IF THEY CHOOSE DISPLAY DATA ... -------------------------------------------
        if(z=='1'):#If they choose to display data ...
            x = input(" 1 : Display  first few rows         2 : Display all dataset               3: Search for  specific data      4 : Back to menu  \n:") 
            if(x=='1'): #Display the first few rows 
                print(data.head())
                 
            elif(x=='2'):#Display the whole data set 
                print(data)
                 
            elif(x=='3'): # Incase they choose to display specific data ... 
                
                
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
                        
                        


            elif( x == '4'):
                print("Session Closed!")
                t = False
                
                            


                    
                                
            
            
            
            
            else: #If they enter another number ... 
                print('Option not valid')
                z=input("Anything Else you want to do ? \n:") # Re-select another option 
        

    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    #---------------------------------------------IF THEY CHOSE CALCULATE MEANS ....-------------------------------------------
        elif(z=='2'):#If they choose to Calculate the means ... 
            m = input('''  
                             Options Available for calculate mean ... ;

                        1 : Anual Salary (USD) 
                        0 : Back to menu
                        \n : '''  )  #Dislpay options 
                                               
            
            if(m == '1'):
                col = input(' \n Anual  Salary (USD) of ...' + str(opts) + '\n:\n') #Display colomns 
                sta  = input( ' \n 1 : All of ' + str(col) + '\n 2 : Specific One\n:\n') #Option for the user to choose 
                if(col in opts):
                    if (sta == '1') : print('\nANUAL SALARY (USD)\n' , data.groupby(col)['Annual Salary (USD)'].agg(['mean'])) # If they choose one , print all means of the col
                    if(sta == '2'): #if they choose 2 
                    
                        k = input('  Options Available in your choice ; ' + str(data[col].unique()) + '\nHow many options would you like to enter ? :') # Ask them how many they want to filter
                        
                        print('Mean of the Annual Salary of ' + str(k) + ':  ' + str(np.mean(data[data[col] == k]['Annual Salary (USD)'])))
                        
                else: print('\n'+str(col) + ' Is NOT an option !\n')            
            elif(m == '0'):     
                t = False
            
        
        
        
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    #---------------------------------------------IF THEY CHOSE CALCULATE MEDIANS ....-------------------------------------------
        elif(z == '3'):
            m = input('''  
                             Options Available for calculate median ... ;

                        1 : Anual Salary (USD) 
                        0 : Back to menu
                        \n : '''  )  #Dislpay options 
                                               
            
            if(m == '1'):
                col = input(' \n Anual  Salary (USD) of ...' + str(opts) + '\n:\n') #Display colomns 
                sta  = input( ' \n 1 : All of ' + str(col) + '\n 2 : Specific One\n:\n') #Option for the user to choose 
                if(col in opts):
                    if (sta == '1') : print('\nANUAL SALARY (USD)\n' , data.groupby(col)['Annual Salary (USD)'].agg(['median'])) # If they choose one , print all means of the col
                    if(sta == '2'): #if they choose 2 
                    
                        k = input('  Options Available in your choice ; ' + str(data[col].unique()) + '\nHow many options would you like to enter ? :') # Ask them how many they want to filter
                        
                        print('Median of the Annual Salary of ' + str(k) + ':  ' + str(np.median(data[data[col] == k]['Annual Salary (USD)'])))
                        
                else: print('\n'+str(col) + ' Is NOT an option !\n')            
            elif(m == '0'):     
                t = False
            
        
        
        
        
        
        
        elif(z=='4'):
            print("""THANK YOU FOR USING THE APP !
                        Session Closed """)
            t = False
            menu = False
            

            
                    

                    
    
        
    
