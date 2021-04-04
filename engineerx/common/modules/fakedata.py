from random import random
from faker import Faker

fake = Faker()


def create_fake_richtext(size=10):
    text_size = int(random() * size) + 1
    richtext = ''
    for i in range(text_size):
        richtext += f'<p>{fake.text()}</p>'
    return richtext
