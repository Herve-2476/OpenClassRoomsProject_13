import pytest
from django.test import Client
from django.urls import reverse, resolve
from django.core.management import call_command
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture()
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "auth_user.json")
        call_command("loaddata", "profiles_profile.json")


def test_index_url(db, django_db_setup):
    path = reverse("profiles:index")
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:index"


def test_profile_url(db, django_db_setup):
    path = reverse("profiles:profile", kwargs={"username": "HeadlinesGazer"})
    assert path == "/profiles/HeadlinesGazer/"
    assert resolve(path).view_name == "profiles:profile"


def test_index_view(db, django_db_setup):
    client = Client()
    path = reverse("profiles:index")
    response = client.get(path)
    content = response.content.decode()
    expected_content_1 = "Profiles"
    expected_content_2 = "HeadlinesGazer"
    assert expected_content_1 in content
    assert expected_content_2 in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


def test_profile_view(db, django_db_setup):
    client = Client()
    path = reverse("profiles:profile", kwargs={"username": "HeadlinesGazer"})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "HeadlinesGazer"
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
