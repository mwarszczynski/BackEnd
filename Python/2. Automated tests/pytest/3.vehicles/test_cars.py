from cars import CarDB
import pytest


@pytest.fixture(scope='module')
def db():
    print('-------------SETUP-------------')
    db = CarDB()
    db.connect('data.json')
    yield db
    print('-------------FINISH-------------')
    db.close()


def test_audi_data(db):
    audi_data = db.get_data('Audi')
    assert audi_data['id'] == 1
    assert audi_data['model'] == 'Audi'
    assert audi_data['production_year'] == 2019
    assert audi_data['available'] == 'true'


def test_mercedes_data(db):
    mercedes_data = db.get_data('Mercedes')
    assert mercedes_data['id'] == 2
    assert mercedes_data['model'] == 'Mercedes'
    assert mercedes_data['production_year'] == 2018
    assert mercedes_data['available'] == 'false'


def test_bmw_data(db):
    bmw_data = db.get_data('BMW')
    assert bmw_data['id'] == 3
    assert bmw_data['model'] == 'BMW'
    assert bmw_data['production_year'] == 2019
    assert bmw_data['available'] == 'true'
