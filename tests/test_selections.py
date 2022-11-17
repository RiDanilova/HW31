import json
import pytest

from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_add_new_selection(api_client, user, ad):
    data = {
        "owner": user.id,
        "name": "NewTestingSelections",
        "items": [ad.id]
    }

    url = reverse("create_selection")
    response = api_client.post(url, data=json.dumps(data), content_type="application/json")

    assert response.json()["owner"] == data["owner"]
    assert response.json()["name"] == data["name"]
    assert response.json()["items"] == data["items"]

    assert response.status_code == status.HTTP_201_CREATED
