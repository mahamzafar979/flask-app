from models.users import UserModel
from tests.base_test import BaseTest


class UsersTest(BaseTest):

    def test_crud(self):
        with self.app_context():
            user = UserModel('test-user','12345')

            self.assertIsNone(UserModel.find_by_username('test-user'),
                              "Found a user with username {}, but expected not to.".format(user.username))
            self.assertIsNone(UserModel.find_by_id(1))
            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test-user'))
            self.assertIsNotNone(UserModel.find_by_id(1))
