##################################################
#   Project 04
#
#   Functions Calculator
#       Ask user what function they want to use
#       Prompt user for a number to calculate
#       Return answer
#
#       Ask user to run again or quit
##################################################

DELTA = 10**-7  # used for the zeta function

PROMPT = "Enter Z for Zeta, C for Conway, Q to quit: "

function_list = ["Z", "z", "Q", "q", "C", "c"]

def int_to_base13(n):
    ''' Convert n to base 13.'''
    
    base_n = ""
    
    # set initial variable values
    quotient_n = int(n) // 13
    remainder_n = int(n) % 13
    new_n = quotient_n
    
    # while the remainder is not 0, keep converting
    while not remainder_n == 0:
        
        if remainder_n == 10:
            base_n = "A" + base_n
    
        elif remainder_n == 11:
            base_n = "B" + base_n
        
        elif remainder_n == 12:
            base_n = "C" + base_n
        
        else:
            base_n = str(remainder_n) + base_n
            
        # reassign variable values
        quotient_n = new_n // 13
        remainder_n = new_n % 13
        new_n = quotient_n
        
    # return the final value
    return base_n

def tridecimal_expansion(n_str):
    ''' Convert base 13 to tridecimal.'''
    
    # replace each number with its respective character
    
    n_str = n_str.replace("A", "+")
    n_str = n_str.replace("B", "-")
    n_str = n_str.replace("C",".")
            
    return n_str
        
def tridecimal_to_conway(n_str):
    ''' Convert tridecimal to conway.'''
    # go through each length of the string from start to end until a float is found
    # if there is no float, then return a zero

    n = 0
    n_float = False

    # try to find a float until end of string
    while (n_float == False) and (n <= len(n_str)):
        n_float = n_str[n:].replace(".", "", 1).isdigit()
        n += 1
        
    n -= 1

    # look for plus and minus signs
    if n_float:
        
        # if plus or minus sign comes after the decimal
        if (n_str[n-1] == "+" or n_str[n-1] == "-") and n_str[n-2] == ".":
            num = 0
        
        elif n_str[n-1] == "+" or n_str[n-1] == "-":
            num = float(n_str[n-1:])
        
        # not a float if there isn't a decimal
        elif "." not in n_str:
            num = 0

        else:
            num = float(n_str[n:])

    else:
        num = 0
        
    return num

def zeta(n):
    ''' Find the zeta function for value s.'''
    
    coefficient = 2
    zeta = 1
    
    n = float(n)
    
    while (abs((1 / ((coefficient + 1) ** n)) - (1 / (coefficient) ** n)) >= (10**-7)) and n > 0:
        zeta += (1 / (coefficient ** n))
        coefficient += 1
    
    zeta += (1 / (coefficient ** n))
        
    if n <= 0:
        zeta = None
        
    return zeta

def main():
    # by convention "main" doesn't need a docstring

    user_int = 0
    
    print("Functions")
    
    # ask user what function to call
    function = input("Enter Z for Zeta, C for Conway, Q to quit: ")
    
    # if valid function not entered
    while function not in function_list:
        print("Error in input. Please try again.")
        function = input("Enter Z for Zeta, C for Conway, Q to quit: ")
        
    # if valid function is entered
    while function in function_list:
        
        # call conway function
        if function == "C" or function == "c":
            print("Conway")
            user_int = input("Input a positive integer: ")
        
            while not user_int.isdigit() or int(user_int) < 0:
                print("Error in input. Please try again.")
                user_int = input("Input a positive integer: ")
        
            print("Base 13: ", int_to_base13(user_int))
            
            user_base = str(int_to_base13(user_int))
            print("Tridecimal: ", tridecimal_expansion(user_base))
            
            user_tridecimal = str(tridecimal_expansion(user_base))
            print("Conway float: ", tridecimal_to_conway(user_tridecimal))
            
            function = input("Enter Z for Zeta, C for Conway, Q to quit: ")
        
        elif function == "Z" or function == "z":
            print("Zeta")
            user_float = input("Input a number: ")
            
            # if there is a negative sign, temporarily remove it to check if it is a float
            user_without_sign = user_float.replace("-", "")
            user_check = user_without_sign.replace(".", "", 1).isdigit()
        
            while not user_check:
                print("Error in input. Please try again.")
                user_float = (input("Input a number: "))
                
                # check again
                user_without_sign = user_float.replace("-", "")
                user_check = user_without_sign.replace(".", "", 1).isdigit()
                
            user_float = float(user_float)
            
            print(zeta(user_float))
            
            function = input("Enter Z for Zeta, C for Conway, Q to quit: ")
        
        elif function == "Q" or function == "q":
            print("\nThank you for playing.")
            break
            
if __name__ == "__main__": 
    main()
