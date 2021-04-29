while True:
    #Ask user to enter number to check if its Armsrong number or not
    user_input=input("Enter positive number: ")
    #Evalute the number was entered by user to check if its float or negative values 

    # # here we will keep ask user to type the number until they put the right number witch is positive number
    if not user_input.isdigit():
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    #When user type the right number this block will take place    
    elif int(user_input)>=0: # Covert the user value to in to compare it if its positive and greather then 0
        digit=0 #the digit is the numbers a,b,c ... (abcd=a**n +b**n +c**n .... we intial it to sum it )
        power =len((user_input)) #the power is n the power  
        for i in range(power):
            digit=digit + int(user_input[i])**power
        if digit==int(user_input):
            print(user_input, "is an Armstrong Number.")
            break
        else:
             print(user_input, "is not an Armstrong Number.")
             break
