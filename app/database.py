from sqlalchemy import Column, Integer, String, Float, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./flight_data.db"

Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)


class FlightSearch(Base):
    __tablename__ = "flight_searches"

    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String)
    destination = Column(String)
    route = Column(String)
    price = Column(Float)
    departure_date = Column(Date)
    stops = Column(Integer)
    duration = Column(String)
    airline = Column(String)



def init_db():
    Base.metadata.create_all(bind=engine)
