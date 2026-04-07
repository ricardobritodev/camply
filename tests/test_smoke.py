"""
Smoke tests — verifica que a aplicação inicializa e as rotas principais respondem.
"""
import pytest
from app import create_app
from app.extensions import db as _db


@pytest.fixture(scope="session")
def app():
    """Cria instância de teste com banco em memória."""
    app = create_app("testing")
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


# ------------------------------------------------------------------ #
# Smoke tests
# ------------------------------------------------------------------ #

def test_app_creates_successfully(app):
    """A aplicação deve ser criada sem erros."""
    assert app is not None


def test_home_returns_200(client):
    """A home page deve retornar HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_properties_list_returns_200(client):
    """A listagem de propriedades deve retornar HTTP 200."""
    response = client.get("/properties/")
    assert response.status_code == 200


def test_login_page_returns_200(client):
    """A página de login deve retornar HTTP 200."""
    response = client.get("/auth/login")
    assert response.status_code == 200


def test_register_page_returns_200(client):
    """A página de cadastro deve retornar HTTP 200."""
    response = client.get("/auth/register")
    assert response.status_code == 200


def test_admin_redirects_unauthenticated(client):
    """O painel admin deve retornar 403 para usuários não autenticados."""
    response = client.get("/admin/")
    assert response.status_code in (302, 403)


def test_my_bookings_redirects_unauthenticated(client):
    """Minhas reservas deve redirecionar para login se não autenticado."""
    response = client.get("/bookings/me")
    assert response.status_code == 302
