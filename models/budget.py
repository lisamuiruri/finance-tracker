from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Budget(Base):
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category = Column(String)
    amount_limit = Column(Float)
    month = Column(String)  

    user = relationship("User", back_populates="budgets")

    def __repr__(self):
        return f"Budget(id={self.id}, category='{self.category}', limit={self.amount_limit}, month='{self.month}')"
