# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: ……w1810194………………..…         
  
# Date:  ………2020-12-05…………..…

#decalring variables to functions as counters for each progress method
prog = 0
trail = 0
ret = 0
exc = 0
total = 0

#define function to determine progression outcome
def progress(pas,defer,fail):

    #declaring the previously created variables as global variables,
    #to be used inside the function
    global prog
    global trail
    global ret
    global exc
    global total

    #create a while true loop to break after printing the respective progression outcome,
    #incrementing the respective counter, and incrementing the total value after each cycle
    while True:
        if(pas + defer + fail) != 120:
            print("Total incorrect")
            #break the loop if the total is incorrect
            break

        #if pass value is lesser than or equal to 80 and fail value is lesser than or equal to 60,
        #print("Do not progress - module trailer")
        elif (pas <= 80 and fail <=60):
            print("Do not Progress - module retriever")
            ret += 1

        #if fail value is greater than or equal to 80, print 'exclude'        
        elif (fail >= 80):
            print("Exclude")
            exc += 1

        #if pass value is equal to 120, print 'progress'
        elif (pas == 120):
            print("Progress")
            prog += 1

        #if pass value is equal to 100 and both defer and fail values equal to 20,
        #print 'progress(module trailer)'
        elif (pas == 100 and (defer == 20 or fail == 20)):
            print("Progress(module trailer)")
            trail += 1

        total += 1
        break

 #creating variables for pass,defer and fail respectively   
user_pass = 0
user_defer = 0
user_fail = 0


#creating a loop where if the entered data type is wrong or not within the range 0,20,40,60,80,100 and 120
#the program displays an error mesage reprompts the user for input
while True:
    try:
        user_pass = int(input("Please enter your credits at pass: "))
    except ValueError:
        print("Integer required")
        continue
    if user_pass not in range(0,121,20):
        print("out of range")
        continue

    try:
        user_defer = int(input("Please enter your credits at defer: "))
    except ValueError:
        print("Integer required")
        continue
    if user_defer not in range(0,121,20):
        print("out of range")
        continue

    try:
        user_fail = int(input("Please enter your credits at fail: "))
    except ValueError:
        print("Integer required")
        continue
    if user_fail not in range(0,121,20):
        print("out of range")
        continue

     #calling the previously defined function, and using the user input as arguments   
    progress(user_pass,user_defer,user_fail)
    #asking the user if they want to quit and display the results or enter another set of data
    print("Would you like to enter another set of data?")
    #declaring a variable in advance to be used for the while loop condition
    end_cycle = ""
    #as long as the users input does not equal 'y' or 'q' reprompt the user for input
    while end_cycle != 'q' and end_cycle != 'y':
        end_cycle = input("Enter 'y' for yes or 'q' to quit and view results: ")

    #if the user enters 'q' display the horizontal histogram,
    #and end the program
    if end_cycle == "q":
        print("Horizontal Histogram")
        print("Progress",prog,":",(prog*'*'))
        print("Trailer",trail,":",(trail*'*'))
        print("Retriever",ret,":",(ret*'*'))
        print("Excluded",exc,":",(exc*'*'))
        print("")
        if total == 1:
            print("1 outcome in total")
        else:
            print(total," outcomes in total")
        break

    #if user enters 'y' go to the top of the loop and ask users for another set of data
    if end_cycle == 'y':
        continue
        


       


        



    
    
