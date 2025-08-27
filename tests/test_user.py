import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User
from database.db import Base

engine = create_engine("sqlite:///:memory:")
TestingSession = sessionmaker(bind=engine)

@pytest.fixture(scope="module")
def session():
    Base.metadata.create_all(engine)
    s = TestingSession()
    yield s
    s.close()

def test_create_user(session):
    user = User(name="Alice", email="alice@example.com")
    session.add(user)
    session.commit()

    retrieved = session.query(User).filter_by(email="alice@example.com").first()
    assert retrieved.name == "Alice"
    assert retrieved.email == "alice@example.com"

