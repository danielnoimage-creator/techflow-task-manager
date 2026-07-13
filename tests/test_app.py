import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../src"
        )
    )
)

from app import app

# Testa se a página inicial é carregada corretamente.
def test_home_page():

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

# Testa se a página de criação de tarefas é carregada corretamente.
def test_create_page():

    client = app.test_client()

    response = client.get("/create")

    assert response.status_code == 200