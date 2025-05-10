import enum

class Periodos(enum.Enum):
    PRIMERO = 1
    SEGUNDO = 2
    TERCERO = 3
    CUARTO = 4

class EstadoAsistencia(enum.Enum):
    PRESENTE = 1
    TARDE = 2
    AUSENTE = 3
    EXCUSA = 4