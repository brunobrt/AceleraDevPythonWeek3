from main import get_temperature
from unittest.mock import patch
import pytest


def valid_entries():
    """
    entries is a list of tuples (lat, lng, temperatures, expected) values for correct entries:
        1- Base test (positive int)
        2- positive float temperatures
        3- negative int temperatures
        4- negative float temperatures
        5- temperature == 0
    :return: entries
    """
    testing_entries = [
        (-14.235004, -51.92528, 62, 16),
        (-14.256346, -52.92528, 62.04, 16),
        (25.836463, 17.35874, -13, -25),
        (25.836463, 17.35874, -13.04, -25),
        (22.852623, 17.35874, 0, -17)]
    return testing_entries


entries = valid_entries()


@patch('main.requests.get')
@pytest.mark.parametrize("lat, lng, temperature, expected", entries)
def test_get_temperature_by_lat_lng(mock_request, lat, lng, temperature, expected):
    mock_request.return_value.json.return_value = {"currently": {"temperature": temperature}}
    response = get_temperature(lat, lng)
    assert expected == response, "The result was {}".format(response)

