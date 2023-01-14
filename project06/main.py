import csv
from operator import itemgetter

# Keywords used to find christmas songs in get_christmas_songs()
CHRISTMAS_WORDS = ['christmas', 'navidad', 'jingle', 'sleigh', 'snow',\
                   'wonderful time', 'santa', 'reindeer']

# Titles of the columns of the csv file. used in print_data()
TITLES = ['Song', 'Artist', 'Rank', 'Last Week', 'Peak Rank', 'Weeks On']

# ranking parameters -- listed here for easy manipulation
A,B,C,D = 1.5, -5, 5, 3

#The options that should be displayed
OPTIONS = "\nOptions:\n\t\
        a - display Christmas songs\n\t\
        b - display songs by peak rank\n\t\
        c - display songs by weeks on the charts\n\t\
        d - display scores by calculated rank\n\t\
        q - terminate the program \n"

#the prompt to ask the user for an option
PROMPT = "Enter one of the listed options: "

# prompt the user for an option, and provide an error message until a valid option is entered
def get_option():
    '''Prompt the user to enter an option to search songs, then print error message until a valid option is entered'''
    
    print(OPTIONS)
    
    options = ["a", "b", "c", "d", "q"]
    
    option = input(PROMPT)
    option = option.lower()
    
    while not option in options:
        print("Invalid option!\nTry again")
        option = input(PROMPT)
    
    return option

# sets up a while loop that runs until the user enters a valid filename, then a file is returned
def open_file():
    '''Ask the user to input a filename, use try except to keep asking until a file is found'''
    
    # sets up for while loop to run until a valid file is found
    invalid = True
    
    while invalid == True:
        # prompt user for a filename and try to open the file
        
        try:
            filename = input("Enter a file name: ")
            fp = open(filename, "r")
            break
        
        # if invalid name is entered
        except FileNotFoundError:
            print("\nInvalid file name; please try again.\n")
        
    return fp

# the file from open_file is read into a master list of data
def read_file(fp):
    '''Takes the filename as an input, reads the file, and returns a master list of all the songs and their data'''
    
    master_list = []
    
    reader = csv.reader(fp)
    next(reader,None)
    
    for line in reader:
        list(line)
        
        # several try except lists to weed out error messages
        try:
            line[2] = int(line[2])
        except ValueError:
            line[2] = -1
        try:
            line[3] = int(line[3])
        except ValueError:
            line[3] = -1
        try:
            line[4] = int(line[4])
        except ValueError:
            line[4] = -1
        try:
            line[5] = int(line[5])
        except ValueError:
            line[5] = -1
            
        # gets rid of any extra data from lines
        new_list = line[0:6]
            
        master_list.append(new_list)
          
    return master_list

def print_data(song_list):
    '''
    This function is provided to you. Do not change it
    It Prints a list of song lists.
    '''
    if not song_list:
        print("\nSong list is empty -- nothing to print.")
        return
    # String that the data will be formatted to. allocates space
    # and alignment of text
    format_string = "{:>3d}. "+"{:<45.40s} {:<20.18s} "+"{:>11d} "*4
    
    # Prints an empty line and the header formatted as the entries will be
    print()
    print(" "*5 + ("{:<45.40s} {:<20.18s} "+"{:>11.9s} "*4+'\n'+'-'*120).format(*TITLES))

    # Prints the formatted contents of every entry
    for i, sublist in enumerate(song_list, 1):
        #print(i,sublist)
        print(format_string.format(i, *sublist).replace('-1', '- '))

# split up the title of each song in the master list and search for christmas words within them
def get_christmas_songs(master_list):
    '''Read through master list of songs and search for christmas words in the titles, 
       then add those songs to a list and return an alphabetically sorted list of christmas songs'''
    
    christmas_songs = []
    
    for list in master_list:
        title_words = []
        
        # make a list of the split up title words
        split_list = list[0].split()
        
        # search for Christmas words
        for word in split_list:
            word = word.lower()
            title_words.append(word)
            if word in CHRISTMAS_WORDS:
                christmas_songs.append(list)
        if "wonderful" in title_words and "time" in title_words:
            christmas_songs.append(list)
            
    # alohabetically sort christmas songs
    christmas_songs.sort()
    
    return christmas_songs
            
# sorts all songs in the master list by their peak ranking
def sort_by_peak(master_list):
    '''Sort all of the songs in the master list by their peak ranking and return that list'''
    
    new = []

    for list in master_list:
        if list[4] != -1:
            new.append(list)

    return sorted(new, key = itemgetter(4))

# sorts all songs in the master list by their weeks on the list
def sort_by_weeks_on_list(master_list):
    '''Sort all of the songs in the master list by their weeks on billboard and return that list'''
    
    new_list = []

    for list in master_list:
        if list[5] != -1:
            new_list.append(list)
    
    return sorted(new_list, key = itemgetter(5), reverse = True)
        
# gives each song in the master list a score
def song_score(song):
    '''Use the inputted song's data to compute a score, and then return that score'''
    
    peak_rank = 100 - int(song[4])
    weeks_on_chart = int(song[5])
    curr_rank = 100 - int(song[2])

    if int(song[2]) == -1:
        curr_rank = -100
        
    if int(song[4]) == -1:
        peak_rank = -100
        
    rank_delta = int(song[2]) - int(song[3])

    song_score = A * peak_rank + B * rank_delta + C*weeks_on_chart + D*curr_rank
    
    return song_score

# ranks the songs by their scores
# did not figure out how to rank the ties alphabetically, ran out of time to trial and error
def sort_by_score(master_list):
    '''Sorts all of the songs in the master list by their score, then returns that list'''
    
    index = 0

    song_scores_list = []
    sorted_songs_by_score = []

    for list in master_list:
        score = [index, song_score(list)]
        song_scores_list.append(score)
        index += 1

    sorted_scores = sorted(song_scores_list, key = itemgetter(1), reverse = True)

    for list in sorted_scores:
        sorted_songs_by_score.append(master_list[list[0]])
    
    return sorted_songs_by_score
        
    
def main():
    
    print("\nBillboard Top 100\n")
    
    master_list = read_file(open_file())
    print_data(master_list)
    
    user_option = get_option()
    
   # uses get option, then runs while the option is not to quit
    while not user_option == "q":
        
        # option a
        if user_option == "a":
            print_data(get_christmas_songs(master_list))
            
            total_songs = len(master_list)
            christmas = len(get_christmas_songs(master_list))
            
            if christmas > 0:
                christmas_percent = int((christmas / total_songs) * 100)
                print("\n{:d}% of the top 100 songs are Christmas songs.".format(christmas_percent))
            
            elif christmas <= 0:
                print("None of the top 100 songs are Christmas songs.")
            
            user_option = get_option()
            
        # else option b
        elif user_option == "b":
            print_data(sort_by_peak(master_list))
            user_option = get_option()
        
        # else option c
        elif user_option == "c":
            print_data(sort_by_weeks_on_list(master_list))
            user_option = get_option()
            
        # else option d
        elif user_option == "d":
            print_data(sort_by_score(master_list))
            user_option = get_option()
        
    # closing print statement
    print("\nThanks for using this program!\nHave a good day!\n")
            

# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()           
