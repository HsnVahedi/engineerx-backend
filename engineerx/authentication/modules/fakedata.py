import logging
from django.contrib.auth import get_user_model
from faker import Faker

# logger = logging.getLogger(__name__)
logger = logging.getLogger("fake users:")
User = get_user_model()
fake = Faker()


class FakeUser:
    def __init__(self, fake_profile, password):
        name = fake_profile['name']
        name_words = name.split()
        (self.first_name, self.last_name) = (name_words[0], name_words[1:][0])
        self.username = fake_profile['username']
        self.email = fake_profile['mail']
        self.password = password


def create_user():
    user = FakeUser(fake_profile=fake.profile(), password=fake.password())
    user = User.objects.create_user(
        username=user.username, email=user.email, password=user.password,
        first_name=user.first_name, last_name=user.last_name,
    )
    logger.info(
        f'Successfully created user: {user.first_name} {user.last_name} with username: {user.username}'
    )
    return user


def create_users(size):
    users = []
    for i in range(size):
        users.append(create_user())
    return users
