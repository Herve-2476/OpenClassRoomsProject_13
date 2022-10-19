import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_view_index():
    client = Client()
    path = reverse("profiles:index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "Profiles"
    assert expected_content in content
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_view_profile():
#     client = Client()
#     path = reverse("profiles:profile")
#     response = client.get(path)
#     content = response.content.decode()
#     expected_content = "Favorite city:"
#     assert expected_content in content
#     assert response.status_code == 200
