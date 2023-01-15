##################################################
#   Project 07
#
#   Regime History
#       Ask user which regime option to use
#       Prompt user for relevant information
#       Return regime information
#
#       Ask user to run again or quit
##################################################

import csv

REGIME=["Closed autocracy","Electoral autocracy","Electoral democracy","Liberal democracy"]
MENU='''\nRegime Options:
            (1) Display regime history
            (2) Display allies
            (3) Display chaotic regimes        
    '''

def open_file():
    ''' Starts in a while loop. Asks the user for a valid filename. If the file can not be found, 
        then the loop prints an error message and runs again until the file can be found. Returns
        a file pointer. '''
    
    invalid = True
    
    # loops until a file can successfully be opened
    while invalid == True:
        try:
            fileName = input("Enter a file: ")
            fp = open(fileName, "r")
            break
        
        except FileNotFoundError:
            print("File not found. Please try again.")
    
    return fp

def read_file(fp):
    ''' Function takes in a filepointer (fp). Creates a csv reader to use, then reads through each line
        of the file. As it goes through the file, it adds each country to a list of country names, and 
        then each regime for each country to a list of regime lists. Returns those two lists. '''
    
    reader = csv.reader(fp)
    next(reader, None)
    
    country_names = []
    list_of_regime_lists = []
    
    # reads through the file
    for line in fp:
        listed_line = line.strip().split(",")
        
        # looks for country in current list
        try:
            index = country_names.index(listed_line[1])
            
        # if the country is not in the list, then it adds it to the country names list
        # then adds other data to list of regimes list
        except ValueError:
            country_names.append(listed_line[1])
            list_of_regime_lists.append(list())
            index = country_names.index(listed_line[1])
            
        list_of_regime_lists[index].append(int(listed_line[4]))
    
    return country_names, list_of_regime_lists
    
def history_of_country(country,country_names,list_of_regime_lists):
    ''' Takes a user-given country, as well as the list of country names and list of regime lists as parameters.
        Indexes the list of country names. Uses that index to look through a specific list of regimes in the 
        main list. Returns a string of the most prevalent regime in the history of a country. '''
    
    index = country_names.index(country)
    count_list = []
        
    # counts number of each regime type for the given country
    zero = list_of_regime_lists[index].count(0)
    one = list_of_regime_lists[index].count(1)
    two = list_of_regime_lists[index].count(2)
    three = list_of_regime_lists[index].count(3)

    # makes each value a list, which is then used for sorting ties    
    zeroList = [zero, 0]
    oneList = [one, 1]
    twoList = [two, 2]
    threeList = [three, 3]

    # creates main list of all count values
    count_list.append(zeroList)
    count_list.append(oneList)
    count_list.append(twoList)
    count_list.append(threeList)

    # sorted by amount, then by number in reverse (lower numbers first)
    sortedCountList = sorted(count_list, key = lambda num: (num[0], -num[1]), reverse = True)
            
    return REGIME[sortedCountList[0][1]]

def historical_allies(regime,country_names,list_of_regime_lists):
    ''' Takes a user-given regime, as well as the two main lists as parameters. Returns a printed list of countries
        that would have been allies, based on their most prevalent historical regime. '''
    
    alliesList = []
    
    # if the country has the same historical regime as the user's regime, the country is added to a list of allies
    for country in country_names:
        country_max = history_of_country(country, country_names, list_of_regime_lists)
        
        if country_max == regime:
            alliesList.append(country)
    
    return sorted(alliesList)

def top_coup_detat_count(top, country_names,list_of_regime_lists):          
    ''' Takes a number of coup counts to print, as well as the two main lists as parameters. Goes through
        the list of countries and counts each time the regime changed throughout history. Returns a formatted 
        printed list of the top countries with the most coup detats. '''
    
    regimeChanges = []
    finalList = []
    
    # goes through the list of countries one at a time
    for country in country_names:
        index = country_names.index(country)
        changeCount = 0
        
        # initializes the last regime to be the fist regime
        lastRegime = list_of_regime_lists[index][0]
        
        #tests if the new regime is the same as the old, if it isn't then add 1 to the regime change counter
        for regime in list_of_regime_lists[index]:
            if regime != lastRegime:
                changeCount += 1
                
            # sets a new last regime to be the regime from this test, cycles back to run through for rest of country
            lastRegime = regime
        
        regimeList = (country, changeCount)
        
        regimeChanges.append(regimeList)
        
    # sorts the list of regime changes by the number of changes (greatest to least), sorts ties alphabetically
    regimeChanges = sorted(regimeChanges, key = lambda nation: (-nation[1], nation[0]))
    
    # the final list is from the nation with the highest coup count to the "top" number the user gave
    finalList = regimeChanges[0:top]
    
    return finalList
    
def main():
    # by convention "main" doesn't need a docstring
    
    # initializes the file and country names/list of regime lists
    fp = open_file()
    country_names, list_of_regime_lists = read_file(fp)
    
    print(MENU)
    
    userOption = input("Input an option (Q to quit): ")
    
    # enters a loop that only ends when the user enters "q" or "Q"
    while userOption != "q" and userOption != "Q":
        
        # runs the regime history function and prints data
        if userOption == "1":
            country = input("Enter a country: ")
            
            # ensures a valid country is entered
            while country not in country_names:
                print("Invalid country. Please try again.")
                country = input("Enter a country: ")
                
            # determines whether to write "an" or "a" in the print statement
            if history_of_country(country, country_names, list_of_regime_lists)[0] == "A" \
                or history_of_country(country, country_names, list_of_regime_lists)[0] == "E"\
                or history_of_country(country, country_names, list_of_regime_lists)[0] == "I" \
                or history_of_country(country, country_names, list_of_regime_lists)[0] == "O" or \
                history_of_country(country, country_names, list_of_regime_lists)[0] == "U":
                    
                    
                print("\nHistorically " + country + " has mostly been an " + \
                      history_of_country(country, country_names, list_of_regime_lists))
                
                # asks the user if they want to run again or quit
                print(MENU)
                userOption = input("Input an option (Q to quit): ")
                
            else:
                print("\nHistorically " + country + " has mostly been a " + \
                      history_of_country(country, country_names, list_of_regime_lists))
                    
                # asks the user if they want to run again or quit
                print(MENU)
                userOption = input("Input an option (Q to quit): ")
        
        # runs the display allies function and prints data
        elif userOption == "2":
            regime = input("Enter a regime: ")
            
            # ensures the user enters a valid regime
            while regime not in REGIME:
                print("Invalid regime. Please try again.")
                regime = input("Enter a regime: ")
                
            print("\nHistorically these countries are allies of type: " + regime)
            alliesList = historical_allies(regime, country_names, list_of_regime_lists)
            
            print(*alliesList, sep = ", ")
            
            # asks the user if they want to run again or quit
            print(MENU)
            userOption = input("Input an option (Q to quit): ")
            
        # runs the display chaotic regimes function and prints data
        elif userOption == "3":
            top = input("Enter how many to display: ")
            
            # makes sure the user enters a valid whole number for the "top" variable
            while not str(top).isdigit():
                print("Invalid number. Please try again.")
                top = int(input("Enter how many to display: "))
                
            top = int(top)
            
            coup_list = top_coup_detat_count(top, country_names, list_of_regime_lists)
            
            # format and print the data
            print("\n{: >25} {: >8}".format("Country", "Changes"))
            print()
            for country in coup_list:
                print("{: >25} {: >8}".format(country[0], country[1]))
                
            # asks the user if they want to run again or quit
            print(MENU)
            userOption = input("Input an option (Q to quit): ")
    
    print("The end.")
 
if __name__ == "__main__": 
    main() 
