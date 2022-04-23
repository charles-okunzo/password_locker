class User:
  '''
  User class that will help generate all users' instances
  '''
  user_accounts_list = [] #empty list of user accounts

  def __init__(self, username, pass_code):
      self.username = username
      self.pass_code = pass_code