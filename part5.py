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
data_list = [[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],
             [20,20,80],[20,0,100],[0,0,120]]

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

#iterate through each element in the previously defined data list
for i in data_list:
    #iterate through each element inside each sublist
    val1 = i[0]
    val2 = i[1]
    val3 = i[2]
    #parse each element to the 'progress' function as arguments 
    progress(val1,val2,val3)

#print the horizontal histogram
print("\nProgress",prog,":",(prog*'*'))
print("Trailing",trail,":",(trail*'*'))
print("Retriever",ret,":",(ret*'*'))
print("Excluded",exc,":",(exc*'*'))
print("\n",total,"outcomes in total")


        


       


        



    
    
