#!/usr/bin/env python3.8

import random
import string
from keyring import set_password

import pyperclip
from credentials import Credentials
from user import User


#create new User account
def create_new_user_account(acc_user_name, pass_code):
  '''
  function to create new user account
  '''
  new_user_acc = User(acc_user_name, pass_code)
  return new_user_acc

#save new user accounts created 
def save_user_acc(acc):
  '''
  function to save new user accounts created
  '''
  acc.save_user_account()


#create new user credential

def create_new_cred(cred_username, cred_pass_code):
  '''
  function to create new instances of user's credentials
  '''
  new_cred = Credentials(cred_username, cred_pass_code)
  return new_cred

#save new user credentials created

def save_credential(cred):
  '''
  function to save new credential created
  '''
  cred.save_credential()


#delete axisting credentials

def delete_credential(cred):
  '''
  function that gets rid of unwanted user credentials
  '''
  cred.del_credential()

#search for existing credentials
def search_cred(name):
  '''
  function that searches for existing user credentials
  '''
  return Credentials.search_by_name(name)


#display existing credentials
def display_credentials():
  '''
  function that rerturns all saved credentials
  '''
  return Credentials.display_cred()


#generate random user passcode
def generate_random_passcode():
  '''
  function that generates random user passcode digits
  '''
  string_code = string.ascii_letters + string.digits + string.punctuation

  while True:
    try:
      code_length = int(input('Enter password length\n'))
      if code_length <4:
        print("-"*10)
        print("Length must be atleast 4 digits")
        print("-"*10)
        continue

      rand_code = random.sample(string_code, code_length)
    
    except ValueError:
      print("-"*10)
      print("Error::Please input a valid number")
      print("-"*10)
      continue

    else:
      gen_password = ''.join(rand_code)
      return gen_password


def main():
  print("\n")
  print("Hello! Welcome to Password Locker Application....\n")
  print("-"*25)
  print("Follow instructions below to proceed")
  print("-"*10+">")

  while True:
    print("\n")
    print("Choose options below.....")
    print("li----> to Login if already have an existing account")
    print("su----> to Sign up if you are new to the application")
    code= input("Answer: ").lower()

    #signup if user selects su
    if code == 'su':
      print("\n")
      print("CREATE PASSWORD LOCKER ACCOUNT")
      print("_"*30)
      user_name = input("Enter username: ")
      while user_name == "":
        print("-"*15)
        print("Incorrect input!!!")
        print("-"*15)
        user_name = input("Enter username: ")

      pass_code = input("Enter password: ")
      while len(pass_code)<4:
        print("----> Password too short. Must be atleast 4 characters.")
        print("-"*10)
        pass_code = input("Enter password: ")

      confirm_pass_code = input("Confirm password: ")
      #confirm if entered passwords match
      while pass_code != confirm_pass_code:
        print("-"*15)
        print("Error:: Passwords did not match. Retry!")
        print("-"*15)
        pass_code = input("Enter password: ")
        while len(pass_code)<4:
          print("----> Password too short. Must be atleast 4 characters.")
          print("-"*10)
          pass_code = input("Enter password: ")

        confirm_pass_code = input("Confirm password: ")

      else:
        created_user = create_new_user_account(user_name, pass_code)
        save_user_acc(created_user)
        print("\n")
        print(f"-----CONGRATULATIONS {user_name.upper()}!!! YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY-----")
        print("\n")
        print("------>Kindly proceed to LOGIN")
        print("\n")
        print("LOGIN INTO YOUR ACCOUNT")
        print("_"*25)
        keyedin_username = input("Enter your Username: ")
        keyedin_passcode = input("Enter your Password: ")

        #check if correct username and password have been entered
      while user_name != keyedin_username or pass_code != keyedin_passcode:
        print("-"*15)
        print("Invalid username or password")
        print("-"*15)
        keyedin_username = input("Enter your Username: ")
        keyedin_passcode = input("Enter your Password: ")

      else:
        print("\n")
        print(f"Logged In as {user_name.capitalize()}")
        print("_"*30)
        print(f"Hello {user_name.capitalize()}. Welcome to your Password Locker Account")
        print("-"*25)
        print("-----Keep all your account passwords safe and secure in one place-----")

        while True:
          print("\n")
          print("Choose an option below to proceed")
          print("\tcr--> to create new credential")
          print("\tdlt--> to delete existing credential")
          print("\tscr--> to search for an existing credential")
          print("\tdc--> to display all available credentials")
          print("\tcp--> to copy credential to clipboard")
          print("-"*10)
          option_code = input("Answer: ").lower()

          if option_code == "cr":
            print("\n")
            print("CREATE AND SAVE CREDENTIAL")
            print("_"*25)
            cred_username = input("Enter Account Name: ")

            while True:
              print("\n")
              print("Select option for password generation")
              print("-"*10)
              print("\tin--> to input the password yourself")
              print("\tgt--> to auto-generate password")
              print("\tex--> to leave prompt")

              p_code = input("Answer: ")

              if p_code == "in":
                print("\n")
                cred_password = input("Enter Account Password: ")
                print("-"*20)
                while len(cred_password)<4:
                  print("----> Password too short. Must be atleast 4 characters.")
                  print("-"*10)
                  cred_password = input("Enter Account Password: ")
                break

              elif p_code == "gt":
                cred_password = generate_random_passcode()
                print("-"*20)
                print("Password successfully generated")
                print("-"*20)
                break

              elif p_code == "ex":
                break

              else:
                print("Incorrect option. Try again!")
            #create and save credential
            created_credential = create_new_cred(cred_username, cred_password)
            save_credential(created_credential)
            print("\n")
            print("\tCredentials have been successfully created and saved!")

          elif option_code == "dlt":
            print("\n")
            print("DELETE CREDENTIAL")
            print("_"*20)
            cred_to_delete = input("Enter Account Name of the credential you want to delete: ")
            cred_found = search_cred(cred_to_delete)
            delete_credential(cred_found)
            print("Credential successfully deleted!")

          elif option_code == "dc":
            if display_credentials() == None:
              print("No credentials found yet")

            else:
              print("\n")
              print("AVAILABLE CREDENTIALS")
              print("_"*20)
              print("\tAccount Name ---|--- \tPassword")
              for cred in display_credentials():
                print(f"\t-->{cred.cred_username} ---|--- {cred.cred_pass_code}")

          elif option_code == "scr":
            print("\n")
            print("SEARCH AVAILABLE CREDENTIALS")
            print("_"*20)
            cred_to_search = input("Enter name to search: ")
            if search_cred(cred_to_search):
              found_cred = search_cred(cred_to_search)
              print(f"Password for Account {cred_to_search}: {found_cred.cred_pass_code}")
            else:
              print("-"*20)
              print("That Credential was not found!")
              print("-"*20)
              
          elif option_code == "cp":
            print("\n")
            print("COPY CREDENTIALS TO CLIPBOARD")
            print("_"*20)
            to_copy = input("Enter username to copy: ")
            found = search_cred(to_copy)
            pyperclip.copy(found)
            print("-"*20)
            print("\tCopied successfully")
            print("-"*20)

          elif option_code == "ex":
            print("\n")
            print("Are you sure you want to exit this application?\nY/N")
            response = input("Answer: ").upper()
            if response == "Y":
              print("-"*20)
              print("\tThank you for using this application. \nSee you again next time!")
              print("-"*20)
            elif response == "N":
              print("\n")
              print("Choose an option below to proceed")
              print("\tcr--> to create new credential")
              print("\tdlt--> to delete existing credential")
              print("\tscr--> to search for an existing credential")
              print("\tdc--> to display all available credentials")
              print("\tcp--> to copy credential to clipboard")
              print("-"*10)
              option_code = input("Answer: ").lower()

            else:
              print("-"*20)
              print("\tErr-->Invalid selection!")
              print("-"*20)


          else:
            print("-"*20)
            print("\tErr-->Invalid selection!")
            print("-"*20)


    elif code == "li":
      print("\n")
      print("LOGIN INTO YOUR ACCOUNT")
      print("_"*25)
      entered_username = input("Enter your Username: ")
      entered_passcode = input("Enter your Password: ")

      set_username = "Charlo254"
      set_password = "okunzo@123"


      #check if correct username and password have been entered
      while entered_username != set_username or entered_passcode != set_password:
        print("-"*15)
        print("Invalid username or password")
        print("-"*15)
        entered_username = input("Enter your Username: ")
        entered_passcode = input("Enter your Password: ")
    
      else:
        print("\n")
        print(f"Logged In as {entered_username.capitalize()}")
        print("_"*30)
        print(f"Hello {entered_username.capitalize()}. Welcome to your Password Locker Account")
        print("-"*25)
        print("-----Keep all your account passwords safe and secure in one place-----")

        while True:
          print("\n")
          print("Choose an option below to proceed")
          print("\tcr--> to create new credential")
          print("\tdlt--> to delete existing credential")
          print("\tscr--> to search for an existing credential")
          print("\tdc--> to display all available credentials")
          print("\tcp--> to copy credential to clipboard")
          print("-"*10)
          option_code = input("Answer: ").lower()

          if option_code == "cr":
            print("\n")
            print("CREATE AND SAVE CREDENTIAL")
            print("_"*25)
            cred_username = input("Enter Account Name: ")

            while True:
              print("\n")
              print("Select option for password generation")
              print("-"*10)
              print("\tin--> to input the password yourself")
              print("\tgt--> to auto-generate password")
              print("\tex--> to leave prompt")

              p_code = input("Answer: ")

              if p_code == "in":
                print("\n")
                cred_password = input("Enter Account Password: ")
                print("-"*20)
                while len(cred_password)<4:
                  print("----> Password too short. Must be atleast 4 characters.")
                  print("-"*10)
                  cred_password = input("Enter Account Password: ")
                break

              elif p_code == "gt":
                cred_password = generate_random_passcode()
                print("-"*20)
                print("Password successfully generated")
                print("-"*20)
                break

              elif p_code == "ex":
                break

              else:
                print("Incorrect option. Try again!")
            #create and save credential
            created_credential = create_new_cred(cred_username, cred_password)
            save_credential(created_credential)
            print("\n")
            print("\tCredentials have been successfully created and saved!")

          elif option_code == "dlt":
            print("\n")
            print("DELETE CREDENTIAL")
            print("_"*20)
            cred_to_delete = input("Enter Account Name of the credential you want to delete: ")
            cred_found = search_cred(cred_to_delete)
            delete_credential(cred_found)
            print("-"*20)
            print("Credential successfully deleted!")
            print("-"*20)

          elif option_code == "dc":
            if display_credentials() == None:
              print("No credentials found yet")

            else:
              print("\n")
              print("AVAILABLE CREDENTIALS")
              print("_"*20)
              print("\tAccount Name ---|--- \tPassword")
              for cred in display_credentials():
                print(f"\t-->{cred.cred_username} ---|--- {cred.cred_pass_code}")

          elif option_code == "scr":
            print("\n")
            print("SEARCH AVAILABLE CREDENTIALS")
            print("_"*20)
            cred_to_search = input("Enter name to search: ")
            if search_cred(cred_to_search):
              found_cred = search_cred(cred_to_search)
              print(f"Password for Account {cred_to_search}: {found_cred.cred_pass_code}")
            else:
              print("-"*20)
              print("That Credential was not found!")
              print("-"*20)

          elif option_code == "cp":
            print("\n")
            print("COPY CREDENTIALS TO CLIPBOARD")
            print("_"*20)
            to_copy = input("Enter username to copy: ")
            found = search_cred(to_copy)
            pyperclip.copy(found)
            print("-"*20)
            print("\tCopied successfully")
            print("-"*20)

          elif option_code == "ex":
            print("\n")
            print("Are you sure you want to exit this application?\nY/N")
            response = input("Answer: ").upper()
            if response == "Y":
              print("-"*20)
              print("\tThank you for using this application. \nSee you again next time!")
              print("-"*20)
            elif response == "N":
              print("\n")
              print("Choose an option below to proceed")
              print("\tcr--> to create new credential")
              print("\tdlt--> to delete existing credential")
              print("\tscr--> to search for an existing credential")
              print("\tdc--> to display all available credentials")
              print("\tcp--> to copy credential to clipboard")
              print("-"*10)
              option_code = input("Answer: ").lower()

            else:
              print("-"*20)
              print("\tErr-->Invalid selection!")
              print("-"*20)


          else:
            print("-"*20)
            print("\tErr-->Invalid selection!")
            print("-"*20)


        
    print("-"*20)
    print("\tErr-->Invalid selection!")
    print("-"*20)
if __name__ == '__main__':
  main()

  
