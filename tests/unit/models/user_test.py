from tests.unit.unit_base_test import UnitBaseTest

from models.users import UserModel


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('testuser', 'test-pwd')

        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, 'test-pwd')
