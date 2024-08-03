import pytest
import requests
import logging

url = "https://swapi.dev"

def test_films_use_correct_method():
    response = requests.get(f"{url}/api/films")
    assert response.status_code == 200

def test_films_use_incorrect_method():
    response = requests.post(f"{url}/api/films")
    assert response.status_code == 405

def test_films_path_not_exist():
    response = requests.get(f"{url}/test/")
    assert response.status_code == 404


def test_films_check_response_data():
    response = requests.get(f"{url}/api/films")
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, dict)
    assert isinstance(response_data['count'], int)
    assert isinstance(response_data['results'], list)
    for film in response_data['results']:
        assert isinstance(film["title"], str)
        assert isinstance(film["episode_id"], int)
        assert isinstance(film["opening_crawl"], str)
        assert isinstance(film["director"], str)
        assert isinstance(film["producer"], str)
        assert isinstance(film["release_date"], str)
        assert isinstance(film["characters"], list)
        assert isinstance(film["planets"], list)
        assert isinstance(film["starships"], list)
        assert isinstance(film["vehicles"], list)
        assert isinstance(film["species"], list)
        assert isinstance(film["created"], str)
        assert isinstance(film["edited"], str)
        assert isinstance(film["url"], str)

def test_films_response_time():
    response = requests.get(f"{url}/api/films")
    assert response.status_code == 200
    assert response.elapsed.total_seconds() <=1

if __name__ == "__main__":
    
    # test_films_response_time()
    pass