import unittest
from models.user import User
class UserTestCase(unittest.TestCase):
    def setUp(self):
        User.objects.create(name="user1", birthday='1970-01-01', number=5)

    def tearDown(self):
        User.objects.all().delete()

    def test_birthday_null(self):
        try:
            User.objects.create(name='test', number=5)
            self.fail("birthday should not be null")
        except:
            pass

    # Test 2 helpers(get_eligibility and get_bizzfuzz)
    def test_helpers(self):
        user = User.objects.get(name="user1")
        self.assertEqual(user.get_eligibility(), 'allowed')
        self.assertEqual(user.get_bizzfuzz(), 'Fuzz')
