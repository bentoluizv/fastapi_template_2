import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import Session

from hackathon.app import app
from hackathon.database import get_session
from hackathon.models import Base, User
from hackathon.security import get_password_hash


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    Base.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def user(session):
    password = 'testtest'
    user = User(
        username='bentoluizv',
        password=get_password_hash(password),
        email='bentoluizv@gmail.com',
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = 'testtest'  # type: ignore

    return user


@pytest.fixture
def other_user(session):
    password = 'testtest'
    user = User(
        username='teste',
        password=get_password_hash(password),
        email='teste@gmail.com',
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = 'testtest'  # type: ignore

    return user


@pytest.fixture
def token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    return response.json()['access_token']
