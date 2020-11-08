from werkzeug.security import safe_str_cmp
from models.users import UserModel
def authenticate(username,password):
  """
  Functions that gets called when user hits the /auth endpoint
  with their username and password
  :param username:
  :param password:
  :return: A userModel object if authentication was successfull None otherwise
  """
  user = UserModel.find_by_username(username)
  if user and safe_str_cmp(user.password, password):
      return user

def identity(payload):
    """
    Function that gets called when user has already authenticated, and Flask-JWT,
    verified that their authorization header is correct
    :param payload:a dictionary with 'identity' key, which is user_id
    :return: A UserModel O
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)