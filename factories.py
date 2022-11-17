from datetime import date

import factory

from ads.models import Selection, Ad
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    first_name = "test_first_name",
    last_name = "test_last_name",
    username = "test_username",
    email = "test@test.com",
    password = "1374SSS",
    birth_date = date.today().strftime("%Y-%m-%d")

    class Meta:
        model = User


class AdsFactory(factory.django.DjangoModelFactory):
    name = "test_Ads"
    author = factory.SubFactory(UserFactory)
    price = 1

    class Meta:
        model = Ad


class SelectionFactory(factory.django.DjangoModelFactory):
    owner = factory.SubFactory(UserFactory),
    name = "test_name"

    class Meta:
        model = Selection
