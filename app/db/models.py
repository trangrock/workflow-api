from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Define the database connection URL
# .env --> terraform --> aws
DATABASE_URL = "postgresql://postgres:postgres@postgres:5432/postgres"

# Create a base class for declarative models
Base = declarative_base()

# Create an SQLAlchemy engine
engine = create_engine(DATABASE_URL)
# engine = create_engine("sqlite:///workflow.db")


class Workflow(Base):
    __tablename__ = 'workflows'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Define one-to-many relationship with components
    components = relationship("Component", back_populates="workflow")


class Component(Base):
    __tablename__ = 'components'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    settings = Column(JSON)

    # Define many-to-one relationship with workflows
    workflow_id = Column(Integer, ForeignKey('workflows.id'))
    workflow = relationship("Workflow", back_populates="components")


# Create tables in the database
Base.metadata.create_all(engine)

# Create a session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
