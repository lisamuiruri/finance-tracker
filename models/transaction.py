from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database.db import Base

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float)
    category = Column(String)
    type = Column(String)  
    date = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="transactions")

    def __repr__(self):
        return f"Transaction(id={self.id}, type='{self.type}', amount={self.amount}, category='{self.category}')"
