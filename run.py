#!/usr/bin/env python3.8

import random
import string
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
  cred.delete_credential()

#search for existing credentials
def search_cred(name):
  '''
  function that searches for existing user credentials
  '''
  Credentials.search_by_name(name)


#display existing credentials
def display_credentials():
  '''
  function that rerturns all saved credentials
  '''
  Credentials.display_cred()


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
  
  
