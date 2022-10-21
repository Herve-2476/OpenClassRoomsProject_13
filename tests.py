import pytest
from django.test import Client
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed


def test_index_url():
    path = reverse("index")
    assert path == "/"
    assert resolve(path).view_name == "index"


@pytest.mark.django_db
def test_view_index():
    client = Client()
    path = reverse("index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "Welcome to Holiday Homes"
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")
