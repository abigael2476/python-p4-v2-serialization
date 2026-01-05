#!/usr/bin/env python3
#server/testing/codegrade_test.py
import pytest
from app import app
from models import db, Pet

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.app_context():
        db.create_all()
        # Add test data
        test_pet = Pet(name='TestPet', species='Dog')
        db.session.add(test_pet)
        db.session.commit()
        # Store the ID for tests
        test_pet_id = test_pet.id
        
    with app.test_client() as client:
        yield client, test_pet_id

def test_codegrade_placeholder():
    """Codegrade placeholder test"""
    assert 1 == 1

def test_pet_to_dict_method(client):
    """Test that Pet instances have a to_dict() method"""
    client, test_pet_id = client
    with app.app_context():
        pet = Pet.query.first()
        result = pet.to_dict()
        assert isinstance(result, dict)
        assert 'id' in result
        assert 'name' in result
        assert 'species' in result
        assert result['id'] == test_pet_id
        assert result['name'] == 'TestPet'
        assert result['species'] == 'Dog'

def test_pet_by_id_route_valid(client):
    """Test /pets/<int:id> route with valid ID"""
    client, test_pet_id = client
    response = client.get(f'/pets/{test_pet_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == test_pet_id
    assert data['name'] == 'TestPet'
    assert data['species'] == 'Dog'

def test_pet_by_id_route_not_found(client):
    """Test /pets/<int:id> route with invalid ID"""
    client, _ = client
    response = client.get('/pets/9999')
    assert response.status_code == 404
    data = response.get_json()
    assert 'message' in data
    assert 'not found' in data['message']

def test_pet_by_species_route_valid(client):
    """Test /species/<string:species> route with valid species"""
    client, _ = client
    response = client.get('/species/Dog')
    assert response.status_code == 200
    data = response.get_json()
    assert 'count' in data
    assert 'pets' in data
    assert isinstance(data['pets'], list)
    assert data['count'] >= 1
    # Check that at least one pet has species 'Dog'
    dog_found = any(pet['species'] == 'Dog' for pet in data['pets'])
    assert dog_found

def test_pet_by_species_route_no_matches(client):
    """Test /species/<string:species> route with species that doesn't exist"""
    client, _ = client
    response = client.get('/species/Whale')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] == 0
    assert len(data['pets']) == 0

def test_index_route(client):
    """Test the index route"""
    client, _ = client
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Welcome to the pet directory!'
