import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://swapi.dev/api/films"

def test_movies_count_is_6():
    response = requests.get(BASE_URL, verify=False)
    assert response.status_code == 200, "API call failed"
    data = response.json()["results"]
    assert len(data) == 6

def test_3rd_movie_director_is_richard_marquand():
    response = requests.get(BASE_URL, verify=False)
    assert response.status_code == 200
    data = response.json()["results"]
    third_movie = data[2]
    assert third_movie["director"] == "Richard Marquand"

def test_5th_movie_producers_are_not_gary_and_george():
    response = requests.get(BASE_URL, verify=False)
    assert response.status_code == 200
    data = response.json()["results"]
    fifth_movie = data[4]
    assert fifth_movie["producer"] != "Gary Kurtz, George Lucas"