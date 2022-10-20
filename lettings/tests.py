import pytest
from django.test import Client
from django.urls import reverse, resolve
from django.core.management import call_command
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture()
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "lettings_address.json")
        call_command("loaddata", "lettings_letting.json")


def test_index_url(db, django_db_setup):
    path = reverse("lettings:index")
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"


def test_letting_url(db, django_db_setup):
    path = reverse("lettings:letting", kwargs={"letting_id": 1})
    assert path == "/lettings/1/"
    assert resolve(path).view_name == "lettings:letting"


def test_index_view(db, django_db_setup):
    client = Client()
    path = reverse("lettings:index")
    response = client.get(path)
    content = response.content.decode()
    expected_content_1 = "Lettings"
    expected_content_2 = "Joshua Tree Green Haus /w Hot Tub"
    assert expected_content_1 in content
    assert expected_content_2 in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


def test_letting_view(db, django_db_setup):
    client = Client()
    path = reverse("lettings:letting", kwargs={"letting_id": 1})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "Joshua Tree Green Haus /w Hot Tub"
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
