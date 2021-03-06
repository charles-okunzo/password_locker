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


  def del_credential(self):
    '''
    delete_credential method that helps remove stored credential from user_cred_list
    '''
    Credentials.user_cred_list.remove(self)

    
  @classmethod
  def search_by_name(cls, username):
    '''
    class method that loops into user_cred_list and returns credential details
    '''
    for credential in cls.user_cred_list:
      if credential.cred_username == username:
        return credential


  @classmethod
  def display_cred(cls):
    '''
    display_cred method that returns a list of all saved credentials
    '''
    return cls.user_cred_list