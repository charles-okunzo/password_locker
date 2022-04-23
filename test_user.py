import unittest

from user import User


class TestUser(unittest.TestCase):
  '''
  Test class that defines test cases for the User class behaviors

  Args:
  unittest.TestCase test case class that helps in creating test cases
  '''
  def setUp(self):
    '''
    setUp method that defines actions run before each test case
    '''
    self.new_user_account = User('Okunzo01', "0302$")

  def test_init(self):
    '''
    test_init test case to check if all new instances of the class are initialized properly
    '''
    self.assertEqual(self.new_user_account.username, "Okunzo01")
    self.assertEqual(self.new_user_account.pass_code, "0302$")

  def test_save_user_account(self):
    '''
    test case to check if a new acoount has been sucessfully saves in the user_accounts_list
    '''
    self.new_user_account.save_user_account()
    self.assertEqual(len(User.user_accounts_list), 1)
      


if __name__ == "__main__":
  unittest.main()