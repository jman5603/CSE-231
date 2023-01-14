############################################################
#   Project 03
#   
#   Tuition Calculator
#       Enter grade level (freshman, sophomore, etc.)
#       Answer questions about your enrollment
#       Enter amount of credits
#       Display tuition costs
#       
#       Ask if user wants to run program again
############################################################

calculateAgain = "yes"
jamesMadison = ""
engineering = ""
college = ""
gradeLevels = "freshman, sophomore, junior, senior"
collegeNames = "business, engineering, health, sciences"
tuition = 0

# header
print("2021 MSU Undergraduate Tuition Calculator.")
print()

# start the calculations
while calculateAgain == "yes":
    
    # ask user what grade they are in
    grade = input("Enter Level as freshman, sophomore, junior, senior: ")
    grade = grade.lower()
    
    while not grade in gradeLevels:
        print("Invalid input. Try again.")
        grade = input("Enter Level as freshman, sophomore, junior, senior: ")
        grade = grade.lower()
    
    # ask about colleges for underclassmen
    if grade.lower() == "freshman" or grade.lower() == "sophomore":
        
        # ask user if they are in these programs
        engineering = input("Are you admitted to the College of Engineering (yes/no): ")
        
        # ask if user is in engineering college
        if engineering.lower() == "no":
            
            # if not, ask if user is in James Madison college
            jamesMadison = input("Are you in the James Madison College (yes/no): ")
        
    # ask about colleges for upperclassmen
    elif grade.lower() == "junior" or grade.lower() == "senior":
        college = input("Enter college as business, engineering, health, sciences, or none: ")
    
        # ask if in James Madison college    
        if grade.lower() == "junior": 
            if not college.lower() in collegeNames:
                jamesMadison = input("Are you in the James Madison College (yes/no): ")
                jamesMadison = jamesMadison.lower()
            
    # ask how many credits the user is taking this semester
    numCredits = input("Credits: ")
    
    # print an error message if a number isnt entered
    while not numCredits.isnumeric() or int(numCredits) < 1:
        print("Invalid input. Try again.")
        numCredits = input("Credits: ")
        
    # calculations for freshman
    if grade.lower() == "freshman":
        if int(numCredits) > 12:
            tuition = (int(numCredits) * 482)
        
        if 11 < int(numCredits) < 19:
            tuition = 7230
            
        if int(numCredits) > 18:
            tuition = 7230 + ((int(numCredits) - 18) * 482)
        
        if engineering.lower() == "yes":
            if int(numCredits) <= 4:
                tuition += 402
            
            if int(numCredits) > 4:
                tuition += 670
        
        # james madison college tax
        if jamesMadison.lower() == "yes":
            tuition += 7.50
            
        # state news tax
        if int(numCredits) >= 6:
            tuition += 5
            
        # ASMSU and FM radio taxes
        if int(numCredits) > 0:
            tuition += 24
            
        print("Tuition is ${:,.2f}.".format(tuition))
        calculateAgain = input("Do you want to do another calculation (yes/no): ")
        calculateAgain = calculateAgain.lower()
    
    # calculations for sophomores
    if grade.lower() == "sophomore":
        
        # if less than 12 credits
        if int(numCredits) > 12:
            tuition = (int(numCredits) * 494)
        
        # if between 12 and 18 credits
        if 11 < int(numCredits) < 19:
            tuition = 7410
            
        # if more than 18 credits
        if int(numCredits) > 18:
            tuition = 7410 + ((int(numCredits) - 18) * 494)
        
       # if in engineering college
        if engineering.lower() == "yes":
            if int(numCredits) <= 4:
                tuition += 402
            
            if int(numCredits) > 4:
                tuition += 670
        
        # james madison college tax
        if jamesMadison.lower() == "yes":
            tuition += 7.50
            
        # state news tax
        if int(numCredits) >= 6:
            tuition += 5
            
        # ASMSU and FM radio taxes
        if int(numCredits) > 0:
            tuition += 24
            
        print("Tuition is ${:,.2f}.".format(tuition))
        calculateAgain = input("Do you want to do another calculation (yes/no): ")
        calculateAgain = calculateAgain.lower()
        
    # calculations for juniors
    if grade.lower() == "junior":
        
        # if in engineering college
        if college.lower() == "engineering":
            
            # if less than 12 credits
            if int(numCredits) > 12:
                tuition = (int(numCredits) * 573)
        
            # if between 12 and 18 credits
            if 11 < int(numCredits) < 19:
                tuition = 8595
            
            # if more than 18 credits
            if int(numCredits) > 18:
                tuition = 8595 + ((int(numCredits) - 18) * 573)
            
            if int(numCredits) <= 4:
                tuition += 402
            
            if int(numCredits) > 4:
                tuition += 670
                
            # state news tax
            if int(numCredits) >= 6:
                 tuition += 5
                 
            # ASMSU and FM radio taxes
            if int(numCredits) > 0:
                 tuition += 24
                
            print("Tuition is ${:,.2f}.".format(tuition))
            calculateAgain = input("Do you want to do another calculation (yes/no): ")
            calculateAgain = calculateAgain.lower()
        
        # if in business college
        elif college.lower() == "business":
            
            # if less than 12 credits
            if int(numCredits) > 12:
                tuition = (int(numCredits) * 573)
        
            # if between 12 and 18 credits
            if 11 < int(numCredits) < 19:
                tuition = 8595
            
            # if more than 18 credits
            if int(numCredits) > 18:
                tuition = 8595 + ((int(numCredits) - 18) * 573)
            
            if int(numCredits) <= 4:
                tuition += 113
            
            if int(numCredits) > 4:
                tuition += 226
                
            # state news tax
            if int(numCredits) >= 6:
                 tuition += 5
                 
            # ASMSU and FM radio taxes
            if int(numCredits) > 0:
                 tuition += 24
                
            print("Tuition is ${:,.2f}.".format(tuition))
            calculateAgain = input("Do you want to do another calculation (yes/no): ")
            calculateAgain = calculateAgain.lower()
        
        # if in college of health or in college of sciences, because the costs are the same
        elif college.lower() == "health" or college.lower() == "sciences":
            
            # if less than 12 credits
            if int(numCredits) > 12:
                tuition = (int(numCredits) * 555)
        
            # if between 12 and 18 credits
            if 11 < int(numCredits) < 19:
                tuition = 8325
            
            # if more than 18 credits
            if int(numCredits) > 18:
                tuition = 8325 + ((int(numCredits) - 18) * 555)
            
            if int(numCredits) <= 4:
                tuition += 50
            
            if int(numCredits) > 4:
                tuition += 100
                
            # state news tax
            if int(numCredits) >= 6:
                 tuition += 5
                 
            # ASMSU and FM radio taxes
            if int(numCredits) > 0:
                 tuition += 24
                
            print("Tuition is ${:,.2f}.".format(tuition))
            calculateAgain = input("Do you want to do another calculation (yes/no): ")
            calculateAgain = calculateAgain.lower()
        
        # if not in a college
        elif not college.lower() == "business" or college.lower() == "engineering" or college.lower() == "health" or college.lower() == "sciences":
            
            # if less than 12 credits
            if int(numCredits) < 12:
                tuition = (int(numCredits) * 555)
        
            # if between 12 and 18 credits
            if 11 < int(numCredits) < 19:
                tuition = 8325
            
            # if more than 18 credits
            if int(numCredits) > 18:
                tuition = 8325 + ((int(numCredits) - 18) * 555)
                
            # state news tax
            if int(numCredits) >= 6:
                 tuition += 5
                 
            # ASMSU and FM radio taxes
            if int(numCredits) > 0:
                 tuition += 24
                 
            # james madison college tax
            if jamesMadison.lower() == "yes":
                tuition += 7.50
                
            print("Tuition is ${:,.2f}.".format(tuition))
            calculateAgain = input("Do you want to do another calculation (yes/no): ")
            calculateAgain = calculateAgain.lower()
            
    # calculations for seniors
    if grade.lower() == "senior":
            
        # if in engineering college
        if college.lower() == "engineering":
                
            # if less than 12 credits
            if int(numCredits) < 12:
                tuition = (int(numCredits) * 573)
            
            # if between 12 and 18 credits
            if 11 < int(numCredits) < 19:
                tuition = 8595
                
            # if more than 18 credits
            if int(numCredits) > 18:
                tuition = 8595 + ((int(numCredits) - 18) * 573)
                
            if int(numCredits) <= 4:
                tuition += 402
                
            if int(numCredits) > 4:
                tuition += 670
                    
            # state news tax
            if int(numCredits) >= 6:
                tuition += 5
                     
            # ASMSU and FM radio taxes
            if int(numCredits) > 0:
                    tuition += 24
            
            print("Tuition is ${:,.2f}.".format(tuition))
            calculateAgain = input("Do you want to do another calculation (yes/no): ")
            calculateAgain = calculateAgain.lower()
                
        # if in business college
        elif college.lower() == "business":
                
            # if less than 12 credits
            if int(numCredits) > 12:
                tuition = (int(numCredits) * 573)
            
            # if between 12 and 18 credits
            if 11 < int(numCredits) < 19:
                tuition = 8595
                
            # if more than 18 credits
            if int(numCredits) > 18:
                tuition = 8595 + ((int(numCredits) - 18) * 573)
                
            if int(numCredits) <= 4:
                tuition += 113
                
            if int(numCredits) > 4:
                tuition += 226
                    
            # state news tax
            if int(numCredits) >= 6:
                tuition += 5
                     
            # ASMSU and FM radio taxes
            if int(numCredits) > 0:
                tuition += 24
                    
            print("Tuition is ${:,.2f}.".format(tuition))
            calculateAgain = input("Do you want to do another calculation (yes/no): ")
            calculateAgain = calculateAgain.lower()
            
        # if in college of health or in college of sciences, because the costs are the same
        elif college.lower() == "health" or college.lower() == "sciences":
                
            # if less than 12 credits
            if int(numCredits) > 12:
                tuition = (int(numCredits) * 555)
            
            # if between 12 and 18 credits
            if 11 < int(numCredits) < 19:
                tuition = 8325
                
            # if more than 18 credits
            if int(numCredits) > 18:
                tuition = 8325 + ((int(numCredits) - 18) * 555)
                
            if int(numCredits) <= 4:
                tuition += 50
                
            if int(numCredits) > 4:
                tuition += 100
                    
            # state news tax
            if int(numCredits) >= 6:
                tuition += 5
                     
            # ASMSU and FM radio taxes
            if int(numCredits) > 0:
                tuition += 24
                    
            print("Tuition is ${:,.2f}.".format(tuition))
            calculateAgain = input("Do you want to do another calculation (yes/no): ")
            calculateAgain = calculateAgain.lower()
            
        else:
    
            # if less than 12 credits
            if int(numCredits) > 12:
                tuition = (int(numCredits) * 555)
            
            # if between 12 and 18 credits
            if 11 < int(numCredits) < 19:
                tuition = 8325
                
            # if more than 18 credits
            if int(numCredits) > 18:
                tuition = 8325 + ((int(numCredits) - 18) * 555)
                    
            # state news tax
            if int(numCredits) >= 6:
                tuition += 5
                     
            # ASMSU and FM radio taxes
            if int(numCredits) > 0:
                tuition += 24
                    
            print("Tuition is ${:,.2f}.".format(tuition))
            calculateAgain = input("Do you want to do another calculation (yes/no): ")
            calculateAgain = calculateAgain.lower()
            
            
            
