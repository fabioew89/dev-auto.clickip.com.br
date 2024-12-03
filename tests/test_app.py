import sys
import os

import pytest
from app import create_app
from app.controllers.forms import Form_Register, Network_Form
# from wtforms.validators import ValidationError

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False,  # Desabilita CSRF para facilitar os testes
    })
    return app


@pytest.fixture
def client(app):
    return app.test_client()


# Teste de validação do formulário de registro
def test_form_register_validation():
    form = Form_Register(
        username="fabio.ewerton",
        password="fabio12",
        password_confirm="fabio12"
    )
    assert form.validate() is True

    form_invalid = Form_Register(
        username="",
        password="short",
        password_confirm="different"
    )
    assert form_invalid.validate() is False


# Teste de validação do formulário de rede
def test_network_form_validation():
    form = Network_Form(
        hostname="Device1",
        username="admin",
        password="password123",
        unit_vlan=100,
        description="Test VLAN",
        bandwidth=100,
        ipv4_gw="192.168.1.1",
        ipv6_gw="2001:db8::1",
        ipv6_cli="2001:db8::2",
        ipv6_48="2001:db8::/48"
    )
    assert form.validate() is True

    form_invalid = Network_Form(
        hostname="",
        username="",
        password="",
        unit_vlan=5000,  # VLAN inválida
        ipv4_gw="999.999.999.999",  # IP inválido
        ipv6_gw="invalid_ipv6"  # IPv6 inválido
    )
    assert form_invalid.validate() is False


# Teste de resposta da rota principal
def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Config interface" in response.data


# Teste de envio de formulário
def test_form_submission(client):
    response = client.post("/submit", data={
        "hostname": "Device1",
        "username": "admin",
        "password": "password123",
        "unit_vlan": 100,
        "description": "Test",
        "bandwidth": 100.0,
        "ipv4_gw": "192.168.1.1",
        "ipv6_gw": "2001:db8::1",
        "ipv6_cli": "2001:db8::2",
        "ipv6_48": "2001:db8::/48"
    })
    assert response.status_code == 200
    assert b"Form submitted successfully" in response.data
