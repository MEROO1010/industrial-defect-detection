from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class DefectLog(Base):
    __tablename__ = "defect_logs"
    id = Column(Integer, primary_key=True)
    defect_type = Column(String)
    confidence = Column(Float)
    timestamp = Column(DateTime, default=datetime.now)
    image_path = Column(String)

engine = create_engine("sqlite:///defects.db")
Base.metadata.create_all(engine)