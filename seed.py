from database.db import Base, engine
from models.user import User
from models.transaction import Transaction
from models.budget import Budget

print("Creating database tables...")
Base.metadata.create_all(engine)
print("Done.")
