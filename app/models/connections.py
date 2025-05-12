from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Float, Date
from .enums import Periodos, EstadoAsistencia

class Nivel(db.Model):
    """
    Crea un nuevo nivel del modelo de base de datos

    Args:
        nombre (str): El nombre del nivel
    """
    __tablename__ = 'niveles'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)
    grados = db.relationship('Grado', backref='nivel', lazy=True)
    asignaturas = db.relationship('Asignatura', backref='nivel', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
        }

    def to_dict_deep(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'grados': [grado.to_dict() for grado in self.grados]
        }


class Grado(db.Model):
    """
    Crea un nuevo grado del modelo de base de datos

    Args:
        nombre (str): El nombre del grado
        nivel_id (int): Id del nivel al que pertenece
    """
    __tablename__ = 'grados'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)
    nivel_id = Column(Integer, ForeignKey('niveles.id'), nullable=False)
    salones = db.relationship('Salon', backref='grado', lazy=True)
    criterios = db.relationship('Criterio', backref='grado', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'nivel': self.nivel.nombre
        }
    
    def to_dict_deep(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'nivel': self.nivel.nombre,
            'salones': [salon.to_dict() for salon in self.salones],
            'criterios': [criterio.to_dict() for criterio in self.criterios]
        }

class Salon(db.Model):
    """
    Crea una nueva nota del modelo de base de datos

    Args:
        nombre (str): El nombre del salón
        grado_id (int): Id del grado al que pertenece el salón
        actividad_id (int): Id de la actividad calificada
    """
    __tablename__ = 'salones'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    grado_id = Column(Integer, ForeignKey('grados.id'), nullable=False)
    estudiantes = db.relationship('Estudiante', backref='salon', lazy=True)
    clases = db.relationship('Clase', backref='salon', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'grado': self.grado.nombre
        }
    
    def to_dict_deep(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'grado': self.grado.nombre,
            'estudiantes': [estudiante.to_dict() for estudiante in self.estudiantes],
            'clases': [clase.to_dict() for clase in self.clases]
        }

class Profesor(db.Model):
    """
    Crea un nuevo profesor del modelo de base de datos

    Args:
        nombre (str): Nombre del profesor
        apellido (str): Apellido del profesor
    """
    __tablename__ = 'profesores'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    clases = db.relationship('Clase', backref='profesor', lazy=True)

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido
        }
    
    def to_dict_deep(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'clases': [clase.to_dict() for clase in self.clases]
        }

class Asignatura(db.Model):
    """
    Crea una nueva asignatura del modelo de base de datos

    Args:
        nombre (str): El nombre de la asignatura
        nivel_id (int): Id del nivel al que pertenece la asignatura
    """
    __tablename__ = 'asignaturas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    nivel_id = Column(Integer, ForeignKey('niveles.id'), nullable=False)
    criterios = db.relationship('Criterio', backref='asignatura', lazy=True)
    clases = db.relationship('Clase', backref='asignatura', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'nivel': self.nivel.nombre
        }
    
    def to_dict_deep(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'nivel': self.nivel.nombre,
            'criterios': [criterio.to_dict() for criterio in self.criterios],
            'clases': [clase.to_dict() for clase in self.clases]
        }

class Clase(db.Model):
    """
    Crea una nueva clase del modelo de base de datos

    Args:
        salon_id (int): Id del salón al que pertenece
        profesor_id (int): Id del profesor encargado de la clase
        asignatura_id (int): Id de la asignatura dictada en esta clase
    """
    __tablename__ = 'clases'

    id = Column(Integer, primary_key=True)
    salon_id = Column(Integer, ForeignKey('salones.id'), nullable=False)
    profesor_id = Column(Integer, ForeignKey('profesores.id'), nullable=False)
    asignatura_id = Column(Integer, ForeignKey('asignaturas.id'), nullable=False)
    actividades = db.relationship('Actividad', backref='clase', lazy=True)
    asistencias = db.relationship('Asistencia', backref='clase', lazy=True)

    @property
    def nombre_generado(self):
        return f"{self.asignatura.nombre} - {self.salon.nombre}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre_generado,
            'profesor': self.profesor.nombre_completo
        }
    
    def to_dict_deep(self):
        return {
            'id': self.id,
            'nombre': self.nombre_generado,
            'profesor': self.profesor.nombre_completo,
            'actividades': [actividad.to_dict() for actividad in self.actividades]
        }

class Estudiante(db.Model):
    """
    Crea un nuevo estudiante del modelo de base de datos

    Args:
        nombre (str): El nombre
        apellido (str): El apellido del estudiante
        salon_id (int): El id del salón al que pertenece
    """
    __tablename__ = 'estudiantes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    salon_id = Column(Integer, ForeignKey('salones.id'), nullable=False)
    notas = db.relationship('Nota', backref='estudiante')
    asistencias = db.relationship('Asistencia', backref='estudiante', lazy=True)

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'salon': self.salon.nombre,
        }
    
    def to_dict_deep(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'salon': self.salon.nombre,
            'notas': [nota.to_dict() for nota in self.notas]
        }

class Criterio(db.Model):
    """
    Crea un nuevo criterio del modelo de base de datos

    Args:
        nombre (str): El nombre
        peso (int): El peso porcentual del criterio en su asignatura
        periodo (Periodos): El enum del periodo al que pertenece ese criterio
        asignatura_id (int): Id de la asignatura al que pertenece el criterio
        grado_id (int): Id del grado al que pertenece
    """
    __tablename__ = 'criterios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)
    peso = Column(Integer, nullable=False)
    periodo = Column(Enum(Periodos))
    asignatura_id = Column(Integer, ForeignKey('asignaturas.id'), nullable=False)
    grado_id = Column(Integer, ForeignKey('grados.id'), nullable=False)
    actividades = db.relationship('Actividad', backref='criterio')

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'peso': self.peso,
            'periodo': self.periodo,
            'asignatura': self.asignatura.nombre,
            'grado': self.grado.nombre,
        }
    
    def to_dict_deep(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'peso': self.peso,
            'periodo': self.periodo,
            'asignatura': self.asignatura.nombre,
            'grado': self.grado.nombre,
            'actividades': [actividad.to_dict() for actividad in self.actividades]
        }

class Actividad(db.Model):
    """
    Crea una nueva actividad del modelo de base de datos

    Args:
        nombre (str): El nombre
        clase_id (int): Id de la clase a la que pertenece la actividad
        criterio_id (int): Id del criterio al que pertenece
    """
    __tablename__ = 'actividades'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    clase_id = Column(Integer, ForeignKey('clases.id'), nullable=False)
    criterio_id = Column(Integer, ForeignKey('criterios.id'), nullable=False)
    notas = db.relationship('Nota', backref='actividad', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'clase': self.clase.nombre,
            'criterio': self.criterio.nombre,
        }
    
    def to_dict_deep(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'clase': self.clase.nombre,
            'criterio': self.criterio.nombre,
            'notas': [nota.to_dict() for nota in self.notas]
        }

class Nota(db.Model):
    """
    Crea una nueva nota del modelo de base de datos

    Args:
        calificacion (float): El valor numérico de la calificación
        estudiante_id (int): Id del estudiante al que pertenece la calificación
        actividad_id (int): Id de la actividad calificada
    """
    __tablename__ = 'notas'

    id = Column(Integer, primary_key=True)
    calificacion = Column(Float)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'), nullable=False)
    actividad_id = Column(Integer, ForeignKey('actividades.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'calificacion': self.calificacion,
            'estudiante': self.estudiante.nombre,
            'actividad': self.actividad.nombre,
        }

class Asistencia(db.Model):
    """
    Crea un nuevo registro de asistencia del modelo de base de datos

    Args:
        estudiante_id (int): Id del estudiante al que se le toma la asistencia
        clase_id (int): Id de la clase en que se toma la asistencia
        estado (EstadoAsistencia): Enum del estado de asistencia
        fecha (Date): fecha en la que se toma la asistencia
    """
    __tablename__ = 'asistencias'

    id = Column(Integer, primary_key=True)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'), nullable=False)
    clase_id = Column(Integer, ForeignKey('clases.id'), nullable=False)
    estado = Column(Enum(EstadoAsistencia), nullable=False)
    fecha = Column(Date, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'estudiante': self.estudiante.nombre,
            'clase': self.clase.nombre,
            'actividad': self.actividad.nombre,
        }