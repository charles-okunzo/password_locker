import unittest

from credentials import Credentials


class TestCredentials(unittest.TestCase):
  '''
  TestCredentials test class that defines test cases for Credentials class behavior
  '''

  def setUp(self):
      '''
      set up method defines actions to be run before any test cases
      '''
      self.new_user_credential = Credentials("Charlo", "okunzo@123")

  def tearDown(self):
      '''
      tearDown method that performs clean up after each test case has run
      '''
      Credentials.user_cred_list = []


  def test_init(self):
    '''
    test_init test case that checks if credential instance were initialized correctly
    '''

    self.assertEqual(self.new_user_credential.cred_username, "Charlo")
    self.assertEqual(self.new_user_credential.cred_pass_code, "okunzo@123")

  def test_save_credentials(self):
    '''
    test_save_credentials test case to check if credentials are added to the user_cred_list
    '''

    self.new_user_credential.save_credential()
    self.assertEqual(len(Credentials.user_cred_list), 1)


  def test_save_multiple_contacts(self):
    '''
    test_save_multiple_contacts test case to check if we can store multiple oblects in our credentials list
    '''
    self.new_user_credential.save_credential()

    test_credential = Credentials("AngelBecky", "becky@123")
    test_credential.save_credential()

    self.assertEqual(len(Credentials.user_cred_list), 2)

  def test_delete_credential(self):
    '''
    test_delete_credential test case to remove saved credential from user_cred_list
    '''
    self.new_user_credential.save_credential()
    test_credential = Credentials("AngelBecky", "becky@123")
    test_credential.save_credential()

    self.new_user_credential.delete_credential()
    self.assertEqual(len(Credentials.user_cred_list), 1)



if __name__ == '__main__':
  unittest.main()


  