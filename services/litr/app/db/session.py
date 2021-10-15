from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"
SQLALCHEMY_DATABASE_URI = "postgresql://odin:odin@192.168.1.41:5432/cdp"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
)

SessionLocal = sessionmaker(engine)
