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


  def test_init(self):
    '''
    test_init test case that checks if credential instance were initialized correctly
    '''

    self.assertEqual(self.new_user_credential.cred_username, "Charlo")
    self.assertEqual(self.new_user_credential.cred_pass_code, "okunzo@123")


  