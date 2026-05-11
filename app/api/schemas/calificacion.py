from pydantic import BaseModel

class calificacionesCreate(BaseModel):
    alumno: str
    materia: str
    calificaciones: float

class calificacionesResponder(calificacionesCreate):
    id: int

    class config:
        orm_mode = True
