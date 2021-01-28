from enum import IntEnum, unique


@unique
class TipoRegra(IntEnum):
    ALERTA = 1
    IMPEDITIVA = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

@unique
class Sexo(IntEnum):
    Masculino = 1
    Femenino = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
