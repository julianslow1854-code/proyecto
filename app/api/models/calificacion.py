from sqlalchemy import Column, Integer, String, Float
from core.database import Base

class Calificacion(Base):
    __tablename__ = "calificaciones"

    id = Column(Integer, primary_key=True, index=True)
    alumno = Column(String, index=True)
    materia = Column(String)
    calificacion = Column(Float)
    



