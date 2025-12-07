from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
db_url="postgresql+psycopg2://postgres:AcademyRootPassword@localhost:5432/annesana"

engine=create_engine(db_url)
# binding engine
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()