# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: ……w1810194………………..…         
  
# Date:  ………2020-12-05…………..…

#importing system function
import sys
#define function to determine progression outcome
def progress(pas,defer,fail):

    if (pas + defer + fail) != 120:
        print("Total incorrect")
        #exit the program if the total does not equal to 120
        sys.exit()

#if pass value is lesser than or equal to 80 and fail value is lesser than or equal to 60,
#print("Do not progress - module trailer")
    if (pas <= 80 and fail <= 60):
        print("Do not Progress - module retriever")

#if fail value is greater than or equal to 80, print 'exclude'
    if (fail >= 80):
        print("Exclude")

#if pass value is equal to 120, print 'progress'
    if (pas == 120):
        print("Progress")

#if pass value is equal to 100 and both defer and fail values equal to 20,
#print 'progress(module trailer)'
    if (pas == 100 and (defer == 20 or fail == 20)):
        print("progress(module trailer)")

#creating variables for pass,defer and fail respectively
user_pass = 0
user_defer = 0
user_fail = 0

#creating a try except block where if the entered data type is wrong or not within the range 0,20,40,60,80,100 and 120
#the program displays an error mesage and exits

try:
    user_pass = int(input("Please enter your credits at pass: "))
except ValueError:
    print("Integer required")
    sys.exit()

if user_pass not in range(0,121,20):
    print("out of range")
    sys.exit()

try:
    user_defer = int(input("Please enter your credits at defer: "))
except ValueError:
    print("Integer required")
    sys.exit()

if user_defer not in range(0,121,20):
    print("out of range")
    sys.exit()

try:
    user_fail = int(input("Please enter your credits at fail: "))
except ValueError:
    print("Integer required")
    sys.exit()

if user_fail not in range(0,121,20):
    print("out of range")
    sys.exit()


 #calling the previously defined function, and using the user input as arguments   
progress(user_pass,user_defer,user_fail)
