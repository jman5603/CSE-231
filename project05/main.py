############################################################
#   Project 05
#   
#   Best Surf Calculator
#       Enter year to calculate
#       Open file name with that year
#       Ask again until valid file is found with user input
#       Calculate best surf day and max, min, and avg wvht
#       
#       Format and display the outcome
############################################################

# open a file with a given year
def open_file():
    '''Asks user to input a year, adds that year to a file name and opens the file'''
    
    # sets up for while loop to run until a valid file is found
    invalid = True
    
    while invalid == True:
        # prompt user for a year and try to open the file
        
        year = input("Input a year: ")
        
        try:
            filename = "wave_data_" + str(year) + ".txt"
            file = open(filename, "r")
            break
        
        # if invalid year is entered
        except FileNotFoundError:
            print("File does not exist. Please try again.")\
        
    return file
        
# get month in letter abbreviation
def get_month_str(mm):
    '''Takes in mm as a number, and returns it as an abbreviated month'''
    
    if mm == "01":
        mm = "Jan"
    if mm == "02":
        mm = "Feb"
    if mm == "03":
        mm = "Mar"
    if mm == "04":
        mm = "Apr"
    if mm == "05":
        mm = "May"
    if mm == "06":
        mm = "Jun"
    if mm == "07":
        mm = "Jul"
    if mm == "08":
        mm = "Aug"
    if mm == "09":
        mm = "Sep"
    if mm == "10":
        mm = "Oct"
    if mm == "11":
        mm = "Nov"
    if mm == "12":
        mm = "Dec"
    
    return mm

def best_surf(mm, dd, hr, wvht, dpd, best_mm, best_dd, best_hr, best_wvht, best_dpd):
    '''Takes in data from current line in the file, then determines if the waves are better than the current best.
        Returns the new best values.'''
    
    # ensure you skip night hours when you would not be surfing
    if 6 < hr and hr < 19:
        # if the wave height and dpd are greater than their current bests
        if float(wvht) >= best_wvht and dpd > best_dpd:
            best_mm = mm
            best_dd = dd
            best_hr = hr
            best_wvht = wvht
            best_dpd = dpd
                
        # if only the wave height is heigher than it's current best
        elif float(wvht) > best_wvht:
            best_mm = mm
            best_dd = dd
            best_hr = hr
            best_wvht = wvht
            best_dpd = dpd
    
    # return the best values
    return best_mm, best_dd, best_hr, best_wvht, best_dpd

def main():
    print("Wave Data")
    
    # initialize way too many variables
    # project pdf said nine, I have thirteen?
    # if it ain't broke don't fix it
    mm = 0
    dd = 0
    hr = 0
    wvht = 0
    dpd = 0
    best_mm = 0
    best_dd = 0
    best_hr = 0
    best_wvht = 0
    best_dpd = 0
    min_wvht = 10**6
    max_wvht = 0
    total_wvht = 0
    
    n = 0
    
    # sets file name
    wave_file = open_file()
    wave_file.readline()
    wave_file.readline()
    
    # go though each line and extract the data we need
    for line in wave_file:
        mm = line[5:7]
        dd = line[8:10]
        hr = int(line[11:13])
        wvht = float(line[30:36].strip())
        dpd = float(line[37:42])
        
        # used to find average wave height, only when there is data
        if wvht < 99.00 and dpd < 99.00:
            total_wvht += wvht
            n += 1
        
        # set min wvht to current wvht if it is smaller than the current min wvht
        if wvht < min_wvht:
            min_wvht = wvht
            
        # same thing but max, set current wvht to max wvht if it is larger than the current max
        if wvht > max_wvht and wvht < 99.00 and dpd < 99.00:
            max_wvht = wvht
        
        # calculate best data only when there is data recorded
        if wvht < 99.00 and dpd < 99.00:
            best_mm, best_dd, best_hr, best_wvht, best_dpd = best_surf(mm, dd, hr, wvht, dpd, best_mm, best_dd, best_hr, best_wvht, best_dpd)
    
    # find average wave height
    avg_wvht = total_wvht / n
    
    # change best month to it's abbreviation (01 --> Jan)
    best_mm = get_month_str(best_mm)
        
    # prints and formats data using given strings
    print("\nWave Height in meters.")
    print("{:7s}: {:4.2f} m".format("average", avg_wvht))
    print("{:7s}: {:4.2f} m".format("max", max_wvht))
    print("{:7s}: {:4.2f} m".format("min", min_wvht))
    
    print("\nBest Surfing Time:")
    print("{:3s} {:3s} {:2s} {:>6s} {:>6s}".format("MTH","DAY","HR","WVHT","DPD"))
    print("{:3s} {:>3s} {:2d} {:5.2f}m {:5.2f}s".format(best_mm, best_dd, best_hr, best_wvht, best_dpd))
        
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()
