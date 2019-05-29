#import necessary modules
import csv #parang include whatever para gumana si csv.reader function

Username = input("Please enter your username: ")
#input user

Password = input("Please enter your password: ")
#input password

check = False

if Username == "": #check if no input
    print("Your input is blank")
    check = True
    
else:    
    with open('test.csv')as csv_file: #read ung csv file
      csv_reader = csv.reader(csv_file, delimiter=',')  #csv.reader comes from import csv
      line_count = 0 
      
      for row in csv_reader:
            if line_count == 0: #para iskip yung first column
                line_count += 1
            elif line_count >= 1: #Sesearch buong column at first row for the user
                if Username == row[0]:
                    print("USER FOUND")
                    if Password == row[1]: #pag nahanap, search kung equal password
                        print("Password is correct!")
                        print("The name of the user", Username, "is" , row[2], row[3]) #output first name last name
                        check = True
                        break
                    else:    
                        print("Password was incorrect!")
                        check = True
                        break
                line_count += 1
                
if check == False:
    print("USER NOT FOUND")                
                
print("TAPOS NA MGA BOBO")