class Credentials:

  '''
  Credentials class that will help us create new instances of user credentials
  '''

  user_cred_list = []

  def __init__(self, cred_username, cred_pass_code):
      self.cred_username = cred_username
      self.cred_pass_code = cred_pass_code


  def save_credential(self):
    '''
    save_credential method that stores created credential in the user_cred_list
    '''
    Credentials.user_cred_list.append(self)