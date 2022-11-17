import json
import pytest

from django.urls import reverse
from rest_framework import status


# Создание объявления
@pytest.mark.django_db
def test_add_new_ads(api_client, user):
    data = {
        "name": "NewTestingAds",
        "author": user.id,
        "price": 100
    }

    url = reverse("create_ad")
    response = api_client.post(url, data=json.dumps(data), content_type="application/json")

    assert response.json()["name"] == data["name"]
    assert response.json()["author"] == data["author"]
    assert response.json()["price"] == data["price"]


# Выдача списка объявлений (без фильтров)
@pytest.mark.django_db
def test_get_all_ads(api_client):
    url = reverse("all_ads")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK


# Выдачу одного объявления по id
@pytest.mark.django_db
def test_get_one_ads(api_client, ad):
    url = reverse("ad_detail", kwargs={"pk": ad.id})
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == ad.id
