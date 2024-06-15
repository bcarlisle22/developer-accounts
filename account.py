# PROBLEM: code was running in terminal and it was really clustered and hard to find the output 
# SOLUTION: ensured code runner was installed then uncheck "run in terminal" and "show execution message" in extension settings check "whether to clear previous output before each run"

# PROBLEM: was not able to type responses in terminal.
# SOLUTION:  closed terminal downloading code runner ext then adjusting settings to allow typing in terminal then opening new terminal

import time, os, sys
def typingPrint (text):
    for character in text: 
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)


# while (input != ["yes", "no"]):
#     print("\n")
#     print("Please enter valid response")  # excuted but broke after asking, need to put in while loop
print("\n")
print("\n")
newUser = input("Is this your first time logging in? ") #IndentationError
if newUser.lower() == "yes":
    print("\n")
    createUser = input("Would you like to create an account? ")
    if createUser.lower() == "yes":
        print("\n")
        newUserName = input("What is your name? ")
        newUserTitle = input("What is your title? ")
        if [newUserName] == " ":
            print("Welcome to the club " + newUserName + " !") #IndentationError
    if createUser.lower() == "no":
        print("\n")
        print("Oh...then what are ya doin here? lol ")
if newUser.lower() == "no":
    print("Welcome back!")
    print("\n") #IndentationError
    userName = input("Username: ")
    if userName.upper() == "brianna":  # set password to be brianna
        passWord = input("Password: ")  # set username to be code
    if passWord.upper() == "code": # PROBLEM: second if statement was not running SOLUTION: indentation error # got it run but now..passWord not defined 
        print("Hey, " + userName + "!")

        print("\n")

    def display_menu():
        print(UserName)
        print("\n")
        print("COMMAND MENU")
        print("LIST- List all projects")
        print("ADD - Add a project")
        print("DELETE - Delete a project")
        print("EXIT - Exit program")
        print("\n")
        
    print (display_menu)
else:
    typingPrint("Password incorrect")

    
    
    




