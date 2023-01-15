##################################################
#   Project 08
#
#   Diabetes Data
#       Ask user which file to open
#       Formats data for each country
#       Prints the formatted data
#
#       Thanks user for running code and quits
##################################################

import csv
from operator import itemgetter

def open_file():
    ''' Starts in a while loop. Asks the user for a valid filename. If the file can not be found, 
        then the loop prints an error message and runs again until the file can be found. Returns
        a file pointer. '''
    
    invalid = True
    
    # loops until a file can successfully be opened
    while invalid == True:
        try:
            fileName = input("Input a file: ")
            fp = open(fileName, encoding = "utf-8")
            break
        
        except FileNotFoundError:
            print("Error: file does not exist. Please try again.")
    
    return fp

def max_in_region(master_dictionary, region):
    '''Master dictionary and region are parameters. Sorts the master dictionary by diabetes per capita and
       returns the first data.'''
    
    # sorts list of data within a key in the dictionary by the diabetes per capita
    master_dictionary[region].sort(key = itemgetter(-1), reverse = True)
    
    # returns first value in sorted list
    return (master_dictionary[region][0][0], master_dictionary[region][0][-1])

def min_in_region(master_dictionary, region):
    '''IMaster dictionary and region are parameters. Sorts the master dictionary by diabetes per capita in ascending 
       order and returns the first data.'''
    
    # adds per capitas greater than zero to a new list, then sorts that list
    greater_than_zero = []
    
    for list in master_dictionary[region]:
        if list[-1] > 0:
            greater_than_zero.append(list)
            
    greater_than_zero.sort(key = itemgetter(-1))
    
    # returns first value in sorted list
    return (greater_than_zero[0][0], greater_than_zero[0][-1])

def read_file(fp):
    '''Function takes in a filepointer (fp). Creates a csv reader to use, then reads through each line
        of the file. As it goes through the file, it adds each country's data to a list of lists in a dictionary, 
        and returns a master dictionary of lists of lists.'''
    
    reader = csv.reader(fp)
    next(reader, None)
    
    master_dictionary = {}
    
    # reads through each line in the file
    for line in reader:
        listed_line = list(line)
        
        # sorts out lines that are missing data
        try:
            region = listed_line[1]
            country = listed_line[2]
            diabetes = float(listed_line[9])
            population = float(listed_line[5].replace(",", ""))
            
        except ValueError:
            continue
            
        data = [country, diabetes, population]
        master_dictionary.setdefault(region, []).append(data)
        
    # sorts the region alphabetically by country name
    for region in master_dictionary:
        master_dictionary[region].sort()
    
    return master_dictionary

def add_per_capita(master_dictionary):
    '''Takes the master dictionary as a parameter. Divides the diabetes by the population for each country and adds
       it to its respective list.'''
    
    # calculates the diabetes per capita by dividing the diabetes by the population and adds it to the master dict.
    for region in master_dictionary:
        for list in master_dictionary[region]:
            try:
                diabetes = list[1] / list[2]
            
            except ZeroDivisionError:
                diabetes = 0.0
                
            list.append(diabetes)
    
    return master_dictionary

def display_region(master_dictionary, region):
    '''Master dictionary and region are parameters. Formats and prints out the data for the region.'''
    
    # finds the summary data for the region within the list, and saves the value as an index integer
    index = 0
    for list in master_dictionary[region]:
        if list[0] == region:
            break
        else:
            index += 1
    
    # saves data and prints formatted data for the region summary
    summary = master_dictionary[region][index]
    
    print("{:<37s} {:>9s} {:>12s} {:>11s}".format("Region","Cases","Population","Per Capita"))
    print("{:<37s} {:>9.0f} {:>12,.0f} {:>11.5f}".format(summary[0], summary[1], summary[2], summary[3]))
    print()
    print("{:<37s} {:>9s} {:>12s} {:>11s}".format("Country","Cases","Population","Per Capita"))
    
    # sorts the region from highest to lowest diabetes per capita
    master_dictionary[region].sort(key = itemgetter(-1), reverse = True)
    
    # formats and prints the data for each country in the region, after checking that the country is not the same
    # value as the region name
    for data_list in master_dictionary[region]:
        if data_list[0] != summary[0]:
            print("{:<37s} {:>9.1f} {:>12,.0f} {:>11.5f}".format(data_list[0], data_list[1], data_list[2], data_list[3]))
    
    print("\nMaximum per-capita in the {} region".format(region))
    print("{:<37s} {:>11s}".format("Country","Per Capita"))
    print("{:<37s} {:>11.5f}".format(max_in_region(master_dictionary, region)[0], max_in_region(master_dictionary, region)[1]))
    print("\nMinimum per-capita in the {} region".format(region))
    print("{:<37s} {:>11s}".format("Country","Per Capita"))
    print("{:<37s} {:>11.5f}".format(min_in_region(master_dictionary, region)[0], min_in_region(master_dictionary, region)[1]))
    print("-"*72)
    
    return
    
def main():
    fp = open_file()
    master_dictionary = read_file(fp)
    add_per_capita(master_dictionary)
    
    # runs the display region function for each region found in the file that the user gives
    for region in master_dictionary:
        print("Type1 Diabetes Data (in thousands)")
        display_region(master_dictionary, region)
    
    print('\n Thanks for using this program!\nHave a good day!')
    
    fp.close()
    
if __name__ == "__main__": 
    main()
