from classroom.asignatura import Asignatura
   
class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=["Grupo de estudiantes"]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, as1="", as2="", as3=""):
        self._asignaturas.append(Asignatura(as1))
        self._asignaturas.append(Asignatura(as2))
        self._asignaturas.append(Asignatura(as3))

    def agregarAlumno(self, alumno, lista=[]):
        if "Kelly" in lista:
            lista.remove("Kelly")
        lista.append(alumno)
        self.listadoAlumnos = [] + lista
        

    def __str__(self):
        return self.listadoAlumnos[0] + ": " + self._grupo

    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 10"):
    #     cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 4"):
    #     cls.grado = nombre
