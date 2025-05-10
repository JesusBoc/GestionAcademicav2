from app import db
import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum

class Periodos(enum.Enum):
    PRIMERO = 1
    SEGUNDO = 2
    TERCERO = 3
    CUARTO = 4

class Nivel(db.Model):
    __tablename__ = 'niveles'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)
    grados = db.relationship('Grado', backref='nivel', lazy=True)
    asignaturas = db.relationship('Asignatura', backref='nivel', lazy=True)


class Grado(db.Model):
    __tablename__ = 'grados'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)
    nivel_id = Column(Integer, ForeignKey('niveles.id'), nullable=False)
    salones = db.relationship('Salon', backref='grado', lazy=True)
    criterios = db.relationship('Criterio', 'grado')

class Salon(db.Model):
    __tablename__ = 'salones'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    grado_id = Column(Integer, ForeignKey('grados.id'), nullable=False)
    estudiantes = db.relationship('Estudiante', backref='salon', lazy=True)
    clases = db.relationship('Clase', backref='salon', lazy=True)


class Profesor(db.Model):
    __tablename__ = 'profesores'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    clases = db.relationship('Clase', backref='profesor', lazy=True)


class Asignatura(db.Model):
    __tablename__ = 'asignaturas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    nivel_id = Column(Integer, ForeignKey('niveles.id'), nullable=False)
    criterios = db.relationship('Criterio', backref='asignatura', lazy=True)
    clases = db.relationship('Clase', backref='asignatura', lazy=True)


class Clase(db.Model):
    __tablename__ = 'clases'

    id = Column(Integer, primary_key=True)
    salon_id = Column(Integer, ForeignKey('salones.id'), nullable=False)
    profesor_id = Column(Integer, ForeignKey('profesores.id'), nullable=False)
    asignatura_id = Column(Integer, ForeignKey('asignaturas.id'), nullable=False)
    actividades = db.relationship('Actividad', backref='clase', lazy=True)

    @property
    def nombre_generado(self):
        return "f{self.asignatura.nombre} - {self.salon.nombre}"


class Estudiante(db.Model):
    __tablename__ = 'estudiantes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    salon_id = Column(Integer, ForeignKey('salones.id'), nullable=False)

class Criterio(db.Model):
    __tablename__ = 'estudiantes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)
    peso = Column(Integer, nullable=False)
    periodo = Column(Enum(Periodos))
    asignatura_id = Column(Integer, ForeignKey('asignaturas.id'), nullable=False)
    grado_id = Column(Integer, ForeignKey('grados.id'), nullable=False)
    actividades = db.relationship('Actividad', backref='criterio')

class Actividad(db.Model):
    __tablename__ = 'estudiantes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    clase_id = Column(Integer, ForeignKey('clases.id'), nullable=False)
