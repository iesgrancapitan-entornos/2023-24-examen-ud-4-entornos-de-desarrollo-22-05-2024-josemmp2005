"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Jaime Rabasco
Refactorización
Extrae una superclase con los campos
	nombre
	apellidos
	nif
"""


class Persona:

    """Creacion de personas"""

    apellidos = "Apellidos";
    nombre = "Nombre";
    nif = "11111111Z";


class Estudiante(Persona):
    """Creacion de Estudiantes que hereda de persona"""
    curso = "Primaria";

    def __init__(self):
        """Constructor"""
        pass;

    def __init__(self, nif, curso, nombre, apellidos):
        """
        Constructor estudiante
        :param nif: identificador,
        :param curso: curso,
        :param nombre: nombre,
        :param apellidos: apellidos,
        """
        self.nif = nif;
        self.curso = curso;
        self.nombre = nombre;
        self.apellidos = apellidos;

    @property
    def nif(self):
        """

        :return: identificador
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        """

        :param value:
        :return: value
        """
        self.__nif = value

    @property
    def curso(self):
        """

        :return: curso
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        """

        :param value:
        :return: value
        """
        self.__curso = value

    @property
    def nombre(self):
        """

        :return: nombre
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        """

        :param value:
        :return: value
        """
        self.__nombre = value

    @property
    def apellidos(self):
        """

        :return: apellidos
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        """

        :param value:
        :return: value
        """
        self.__apellidos = value

