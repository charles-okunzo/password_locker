#!/usr/bin/env python3.8




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
