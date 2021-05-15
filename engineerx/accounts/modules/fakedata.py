import time
from accounts.models import *
from faker import Faker
from random import random
import logging

from django.contrib.auth.models import Group
from django.conf import settings

from wagtail.images import get_image_model

from accounts.models import PersonalPageRelatedAccount, PersonalPage, PersonalPages, Education, Experience, Skill
from common.modules.fakedata import create_fake_richtext

fake = Faker()
Image = get_image_model()
logger = logging.getLogger("fake personal pages:")


def create_new_social_account(page, social_media):
    account = PersonalPageRelatedAccount(
        page=page, social_media=social_media, url='https://google.com'
    )
    account.save()
    logger.info(f'Created social media account: {social_media}')

    return account


def create_new_social_accounts(page):
    for social_network in PersonalPageRelatedAccount.SOCIAL_NETWORKS:
        if random() > 0.5:
            create_new_social_account(page, social_network)
            time.sleep(settings.SLEEP_TIME)
    page.save()
    page.save_revision().publish()


def create_new_education(page):
    education = Education(page=page)
    if random() > 0.5:
        education.degree = f'{fake.word()} {fake.word()} {fake.word()}'
    if random() > 0.5:
        education.institution = f'{fake.word()} {fake.word()} {fake.word()}'
    if random() > 0.5:
        education.location = fake.address()
    if random() > 0.5:
        end = fake.date_object()
        education.begin = fake.date_object(end_datetime=end)
        education.end = end
    education.save()
    logger.info(f'Created Education #{education.id}')
    # page.save()
    # page.save_revision().publish()
    return education


def create_new_educations(page):
    for i in range(10):
        if random() > 0.8:
            create_new_education(page)
            time.sleep(settings.SLEEP_TIME)
    page.save()
    page.save_revision().publish()


def create_new_experience(page):
    experience = Experience(page=page)
    if random() > 0.5:
        experience.company = f'{fake.word()}'
    if random() > 0.5:
        experience.location = fake.address()
    if random() > 0.5:
        end = fake.date_object()
        experience.begin = fake.date_object(end_datetime=end)
        experience.end = end
    if random() > 0.25:
        experience.role = create_fake_richtext(size=5)
    experience.save()
    logger.info(f'Created Experience #{experience.id}')
    # page.save()
    # page.save_revision().publish()
    return experience


def create_new_experiences(page):
    for i in range(10):
        if random() > 0.8:
            create_new_experience(page)
            time.sleep(settings.SLEEP_TIME)
    page.save()
    page.save_revision().publish()


def create_new_skill(page):
    skill = Skill(page=page)
    skill.name = f'{fake.word()} {fake.word()}'
    skill.description = create_fake_richtext(size=5)
    skill.save()
    logger.info(f'Created Skill: {skill.name}')
    # page.save()
    # page.save_revision().publish()
    return skill


def create_new_skills(page):
    for i in range(15):
        if random() > 0.8:
            create_new_skill(page)
            time.sleep(settings.SLEEP_TIME)
    page.save()
    page.save_revision().publish()


def create_new_personal_page(owner):
    personal_page = PersonalPage(title=fake.job(), owner=owner)
    list_page = PersonalPages.objects.first()
    list_page.add_child(instance=personal_page)
    personal_page = PersonalPage.objects.get(slug=personal_page.slug)
    if random() >= 0.5:
        images = Image.objects.all()
        personal_page.image = images[int(random() * len(images))]

    personal_page.save()
    personal_page.save_revision().publish()

    return personal_page


def create_new_personal_pages():
    moderators_group = Group.objects.get(name='Moderators')
    moderators = moderators_group.user_set.all()

    editors_group = Group.objects.get(name='Editors')
    editors = editors_group.user_set.all()

    pages = []
    for moderator in moderators:
        pages.append(create_new_personal_page(moderator))
        time.sleep(settings.SLEEP_TIME)
    for editor in editors:
        pages.append(create_new_personal_page(editor))
        time.sleep(settings.SLEEP_TIME)

    for page in pages:
        create_new_social_accounts(page)
        create_new_educations(page)
        create_new_experiences(page)
        create_new_skills(page)
        time.sleep(settings.SLEEP_TIME)

    return pages
