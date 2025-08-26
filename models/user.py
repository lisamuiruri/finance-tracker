from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    created_at = Column(DateTime, default=datetime.now)

    transactions = relationship("Transaction", back_populates="user")
    budgets = relationship("Budget", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
