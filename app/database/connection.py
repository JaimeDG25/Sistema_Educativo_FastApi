# database/connection.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = (
    #"postgresql://postgres.ymzpidqxydwtibwgrqwn:#Arquimedes@aws-1-us-west-2.pooler.supabase.com:5432/postgres"
    "postgresql://postgres.ibjisohwwpsitlgapjfe:#Arquimedes@aws-0-us-east-1.pooler.supabase.com:5432/postgres"
    #"postgresql+psycopg://postgres.xxx:#Arquimedes"
    #"@aws-1-us-west-2.pooler.supabase.com:6543/postgres"
)
engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# engine = create_engine(
#     DATABASE_URL,
#     connect_args={"check_same_thread": False}
# )

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# def get_db():
#     db = SessionLocal()

#     try:
#         yield db
#     finally:
#         db.close()