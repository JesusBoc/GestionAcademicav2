from app import db
from sqlalchemy import Column, Integer, String, ForeignKey


class Nivel(db.Model):
    __tablename__ = 'niveles'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    grados = db.relationship('Grado', backref = 'nivel', lazy = True)
    asignaturas = db.relationship('Asignatura', backref = 'nivel', lazy = True)
    
class Grado(db.Model):
    __tablename__ = 'grados'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    nivel_id = Column(Integer, ForeignKey('niveles.id'), nullable=False)
    salones = db.relationship('Salon', backref='grado', lazy=True)

class Salon(db.Model):
    __tablename__ = 'salones'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    grado_id = Column(Integer, ForeignKey('grados.id'), nullable=False)
    estudiantes = db.relationship('Estudiante', backref = 'salon', lazy = True)
    clases = db.relationship('Clase', backref = 'salon', lazy = True)

class Profesor(db.Model):
    __tablename__ = 'profesores'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)

class Asignatura(db.Model):
    __tablename__ = 'asignaturas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    nivel_id = Column(Integer, ForeignKey('niveles.id'), nullable=False)

    
class Clase(db.Model):
    __tablename__ = 'clases'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    salon_id = Column(Integer, ForeignKey('salones.id'), nullable=False)
    profesor_id = Column(Integer, ForeignKey('profesores.id'), nullable=False)

class Estudiante(db.Model):
    __tablename__ = 'estudiantes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(25), nullable=False)
    apellido = Column(String(25),nullable=False)