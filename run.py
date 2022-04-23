#!/usr/bin/env python3.8



#create new User account

from user import User


def create_new_user_account(acc_user_name, pass_code):
  '''
  function to create new user account
  '''
  new_user_acc = User(acc_user_name, pass_code)

