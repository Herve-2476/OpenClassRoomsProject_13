import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_view_index():
    client = Client()
    path = reverse("index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "Welcome to Holiday Homes"
    assert expected_content in content
    assert response.status_code == 200
