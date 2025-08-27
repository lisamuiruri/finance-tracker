import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.budget import Budget
from models.user import User
from database.db import Base

engine = create_engine("sqlite:///:memory:")
TestingSession = sessionmaker(bind=engine)

@pytest.fixture(scope="module")
def session():
    Base.metadata.create_all(engine)
    session = TestingSession()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_create_budget(session):
    user = User(name="Bob", email="bob@example.com")
    session.add(user)
    session.commit()

    budget = Budget(user_id=user.id, category="Groceries", limit=500.0, month="August")
    session.add(budget)
    session.commit()

    retrieved = session.query(Budget).filter_by(user_id=user.id).first()
    assert retrieved is not None
    assert retrieved.category == "Groceries"
    assert retrieved.limit == 500.0
    assert retrieved.month == "August"

def test_budget_repr():
    budget = Budget(user_id=1, category="Groceries", limit=500.0, month="August")
    expected = "Budget(id=None, category='Groceries', limit=500.0, month='August')"
    assert repr(budget) == expected
