import requests
import pytest
import logging
import sys

url = "https://swapi.dev"


@pytest.fixture(scope='module')
def get_film_id():
    film_id = -1
    response = requests.get(f"{url}/api/films")
    if response.status_code == 200:
        response_data = response.json()
        if response_data['count']>0:
            film_id = response_data['results'][response_data['count']-1]['episode_id']

    logging.info(f'film_id:{film_id}')

    return film_id

def test_films_id_use_correct_method(get_film_id):
    film_id = get_film_id  
    response = requests.get(f"{url}/api/films/{film_id}")
    assert response.status_code == 200

def test_films_id_use_incorrect_method(get_film_id):
    film_id = get_film_id
    response = requests.post(f"{url}/api/films/{film_id}")
    assert response.status_code == 405

def test_films_id_check_response_data(get_film_id):
    film_id = get_film_id
    response = requests.get(f"{url}/api/films/{film_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, dict)
    
    assert isinstance(response_data["title"], str)
    assert isinstance(response_data["episode_id"], int)
    assert isinstance(response_data["opening_crawl"], str)
    assert isinstance(response_data["director"], str)
    assert isinstance(response_data["producer"], str)
    assert isinstance(response_data["release_date"], str)
    assert isinstance(response_data["characters"], list)
    assert isinstance(response_data["planets"], list)
    assert isinstance(response_data["starships"], list)
    assert isinstance(response_data["vehicles"], list)
    assert isinstance(response_data["species"], list)
    assert isinstance(response_data["created"], str)
    assert isinstance(response_data["edited"], str)
    assert isinstance(response_data["url"], str)

def test_films_id_non_exist_id():
    response = requests.get(f"{url}/api/films/999999")
    assert response.status_code == 404

def test_films_id_maximun_int_id():
    max_int = sys.maxsize
    logging.info(f'max_int:{max_int}')
    response = requests.get(f"{url}/api/films/{max_int}")
    assert response.status_code == 404

def test_films_id_negative_int_id():
    response = requests.get(f"{url}/api/films/-1")
    assert response.status_code == 404

def test_films_id_zero_id():
    response = requests.get(f"{url}/api/films/0")
    assert response.status_code == 404

def test_films_id_response_time(get_film_id):
    film_id = get_film_id  
    response = requests.get(f"{url}/api/films/{film_id}")
    assert response.status_code == 200
    assert response.elapsed.total_seconds() <=1
    