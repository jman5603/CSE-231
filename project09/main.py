##################################################
#   Project 09
#
#   Machine Learning Image Data
#       Ask user which files to open (json, txt)
#       Formats data for each image
#       Asks user what functions to call
#       Prints data for that option
#       Ask user for a new option or to quit
#
#       Thanks user for running code and quits
##################################################

import json,string

STOP_WORDS = ['a','an','the','in','on','of','is','was','am','I','me','you','and','or','not','this','that','to','with','his','hers','out','it','as','by','are','he','her','at','its']

MENU = '''
    Select from the menu:
        c: display categories
        f: find images by category
        i: find max instances of categories
        m: find max number of images of categories
        w: display the top ten words in captions
        q: quit
        
    Choice: '''
    
OPTIONS = "cfimwq"

def get_option():
   ''' Asks user for an option from the menu. Loops until a valid option is given. '''
   
   valid = False
   option = input(MENU)
   
   while valid == False:
       
       if option.lower() in OPTIONS:
           break
          
       else:
           print("Incorrect choice.  Please try again.")
           option = input(MENU)
   
   return option
    
def open_file(s):
   ''' Asks for a filename and opens that file. Returns a file pointer. '''
   
   invalid = True
   
   # loops until a file can successfully be opened
   while invalid == True:
       try:
           fileName = input("Enter a {} file name: ".format(s))
           fp = open(fileName, "r")
           break
       
       except FileNotFoundError:
           print("File not found.  Try again.")
   
   return fp
        
def read_annot_file(fp1):
   ''' Reads a given file pointer (json file) into a dictionary. '''
   
   data_dictionary = json.load(fp1)
   
   return data_dictionary

def read_category_file(fp2):
   ''' Reads a given file pointer (txt file) into a dictionary. '''
   
   category_data = {}
   
   for line in fp2:
       line = line.split()
       
       category_data[int(line[0])] = line[1]
   
   return category_data

def collect_catogory_set(D_annot, D_cat):
   ''' Iterates through the json data and category data to find which categories are used in the json file. '''
   
   categories = []
   category_nums = []
   
   # adds every category for each image to a list
   for image in D_annot:
       for item in D_annot[image]["bbox_category_label"]:
           category_nums.append(item)
           
   for item in category_nums:
       categories.append(D_cat[item])
       
   # removes duplicates by turning the list into a set
   categories = set(categories)
   
   return categories

def collect_img_list_for_categories(D_annot, D_cat, cat_set):
   ''' Creates a list of images for each category used in the json file. '''
   
   category_lists = {}
   
   # looks at each category in the category set
   for category in cat_set:
       category_lists[category] = []
       
       # for each image in the json file dictionary (D_annot)
       for image in D_annot:
           for item in D_annot[image]["bbox_category_label"]:
               if D_cat[item] == category:
                   category_lists[category].append(image)
                   
   # sort the categories by value 
   for key in category_lists:
       category_lists[key].sort()
   
   return category_lists

def max_instances_for_item(D_image):
    ''' Finds the category with the most instances of itself in images. '''
    
    max_length = 0
    max_category = ""
    
    # finds the image category with the biggest length
    for category in D_image:
        if len(D_image[category]) > max_length:
            max_length = len(D_image[category])
            max_category = category
    
    return (max_length, max_category)

def max_images_for_item(D_image):
    ''' Finds the category with the most images that contain that category. '''
    
    max_length = 0
    max_category = ""
    
    # change each list of images to a set to remove duplicates, then set it back to a list and find the max length
    for category in D_image:
        new_list = set(D_image[category])
        
        if len(new_list) > max_length:
            max_length = len(new_list)
            max_category = category
    
    return (max_length, max_category)

def count_words(D_annot):
    ''' Counts the number of words and their instances (excluding 'boring' words) in the image descriptions. '''
    
    word_map = dict()
    word_list = []

    # iterates through each image in D_annot
    for image in D_annot:
        
        # iterates through each description for each image
        for description in D_annot[image]["cap_list"]:
            description = description.rsplit(string.punctuation)
            new_description = " ".join([str(item) for item in description])
            
            words = new_description.split()
            
            # iterates through the list of words and removes boring words
            for word in words:
                word = word.rstrip(string.punctuation)
                if word in STOP_WORDS:
                    continue
                
                # adds to the word count if it is in the map, otherwise adds it and sets the count to 1
                if word in word_map:
                    word_map[word] += 1
                else:
                    word_map[word] = 1
                    
    sorted_map = dict(sorted(word_map.items(), key = lambda x: x[1], reverse = True))

    for key in sorted_map:
        word_tup = (sorted_map[key], key)
        word_list.append(word_tup)

    word_list.sort(key = lambda x: (x[0], x[1]), reverse = True)
    
    return word_list

def main():    
    print("Images\n")

    # read the json image file
    D_annot = read_annot_file(open_file("JSON image"))
    
    # read the category txt file
    D_cat = read_category_file(open_file("category"))
    
    # categories used in json file
    cat_set = collect_catogory_set(D_annot, D_cat)
    
    # image list for categories
    D_image = collect_img_list_for_categories(D_annot, D_cat, cat_set)
    
    option = get_option()
    
    # quits the loop if option is q or Q
    while option != "q" and option != "Q":
            
        # display categories
        if option.lower() == "c":
            new_cat_set = list(cat_set)
            new_cat_set.sort()
            print("\nCategories:")
            print(*new_cat_set, sep = ", ")
            option = get_option()
            
        # find images by category
        if option.lower() == "f":
            new_cat_set = list(cat_set)
            new_cat_set.sort()
            print("\nCategories:")
            print(*new_cat_set, sep = ", ")
            
            category = input("Choose a category from the list above: ")
            
            while category not in new_cat_set:
                print("Incorrect category choice.")
                category = input("Choose a category from the list above: ")
                
            cat_list = D_image[category]
            
            cat_list = [int(x) for x in cat_list]
            sorted_category = sorted(set(cat_list))
                
            print("\nThe category {} appears in the following images:".format(category))
            print(*sorted_category, sep = ", ")
            
            option = get_option()
        
        # find max instances of categories
        if option.lower() == "i":
            number, category = max_instances_for_item(D_image)
            
            print("\nMax instances: the category {} appears {} times in images.".format(category, number))
            option = get_option()
            
        # find max number of image of categories
        if option.lower() == "m":
            number, category = max_images_for_item(D_image)
            
            print("\nMax images: the category {} appears in {} images.".format(category, number))
            option = get_option()
            
        # display the top ten words in captions
        if option.lower() == "w":
            num_words = input("\nEnter number of desired words: ")
            word_list = count_words(D_annot)
            
            while int(num_words) <= 0:
                print("Error: input must be a positive integer: ")
                num_words = input("\nEnter number of desired words: ")
                
            num_words = int(num_words)
                
            print("\nTop {} words in captions.".format(num_words))
            print("{:<14s}{:>6s}".format("word","count"))
            for i in range(0, num_words):
                print("{:<14s}{:>6d}".format(word_list[i][1], word_list[i][0]))
            
            option = get_option()
            
    print("\nThank you for running my code.") 
    
if __name__ == "__main__":
    main()     
