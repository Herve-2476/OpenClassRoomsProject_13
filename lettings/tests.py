import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_view_index():
    client = Client()
    path = reverse("lettings:index")
    print("BONJOUR", path)
    response = client.get(path)
    content = response.content.decode()
    expected_content = "Lettings"
    assert expected_content in content
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_letting():
    client = Client()
    path = reverse("lettings:index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "Joshua Tree Green Haus /w Hot Tub"
    assert expected_content in content
    assert response.status_code == 200
