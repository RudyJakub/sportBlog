from hashlib import new
import pytest
from sportblog.models import User, Article
from sportblog import create_app, db, create_database


@pytest.fixture(scope="session")
def app():
    app = create_app({
        'TESTING': True,
        'DATABASE': 'sqlite:///test.db',
    })
    
    create_database(app)

    return app


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(scope='module')
def new_user():
    user = User('American Psycho', 'p.bateman@gmail.com', 'seaurchin1')
    return user

@pytest.fixture(scope='module')
def new_editor():
    editor = User('Michael', 'michael@gmail.com', '123', is_editor=True)
    return editor



@pytest.fixture(scope='module')
def new_article():
    editor = User('Michael', 'michael@gmail.com', '123', is_editor=True)
    article = Article('Header', 'Some Text here', editor=editor)
    return article
