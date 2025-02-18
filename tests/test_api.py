from asteroids.api import get_asteroids
import pytest

date_list = ["2021-01-01", "2021-01-02", "2021-01-03", "2021-01-04", "2021-01-05","2021-01-06", "2021-01-07", "2021-01-08", "2021-01-09", "2021-01-10"]

result = []
def test_asteroids():
    for date in date_list:
        asteroids_per_date = get_asteroids(date)
        result.append(asteroids_per_date)
    if not result:
        assert False, "No asteroids found"
    else:
        assert True, "Asteroids found"
