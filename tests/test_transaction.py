import pytest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.transaction import Transaction
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
    Base.metadata.drop_all(engine)

def test_create_transaction(session):
    user = User(name="Alice", email="alice@example.com")
    session.add(user)
    session.commit()

    transaction = Transaction(
        user_id=user.id,
        category="Groceries",
        amount=500.0,
        date=datetime(2025, 8, 25, 22, 5, 22),
        type="expense"
    )
    session.add(transaction)
    session.commit()

    retrieved = session.query(Transaction).filter_by(user_id=user.id).first()
    assert retrieved.category == "Groceries"
    assert retrieved.amount == 500.0
    assert retrieved.type == "expense"
    assert retrieved.date == datetime(2025, 8, 25, 22, 5, 22)

def test_transaction_repr():
    transaction = Transaction(
        id=1,
        user_id=1,
        category="Groceries",
        amount=500.0,
        date=datetime(2025, 8, 25, 22, 5, 22),
        type="expense"
    )
    expected = (
        "Transaction(id=1, category='Groceries', amount=500.0, "
        "date='2025-08-25 22:05:22', type='expense')"
    )
    assert repr(transaction) == expected
