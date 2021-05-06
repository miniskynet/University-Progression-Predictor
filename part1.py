# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: ……w1810194………………..…         
  
# Date:  ………2020-12-05…………..…

#define function to determine progression outcome with three parameters
#each user input for credits at pass, credits at defer and credits at fail will be used as arguments
def progress(pas,defer,fail):
    if (pas <= 80 and fail <= 60):
        print("Do not Progress - module retriever")

#if fail value is equal to or greater than 80, print 'exclude'
    if (fail >= 80):
        print("Exclude")

#if pass value is equal to 120 , print 'progress'
    if (pas == 120):
        print("Progress")

#if pass value equals to 100 and both defer and fail values equal to 20,
#print 'progress(module trailer)'
    if (pas == 100 and (defer == 20 or fail == 20)):
        print("progress(module trailer)")

#take user input for credits at pass
user_pass = int(input("Please enter your credits at pass: "))

#take user input for credit at defer
user_defer = int(input("Please enter your credit at defer: "))

#take user input for credits at fail
user_fail = int(input("Please enter your credit at fail: "))

#call the function
progress(user_pass,user_defer,user_fail)

