import pytest
from rest_framework.test import APIClient

from scripts.load_csv import load_gaia_source_csv

pytest_plugins = [
]


@pytest.fixture
@pytest.mark.django_db
def api_client():
    load_gaia_source_csv('tests/gaia_source.csv')
    client = APIClient()
    return client
