from models.bd.postgress.alumno import AlumnoModel as AlumnoPostgres
from models.bd.sqlite3.alumno import AlumnoModel as AlumnoSqlite3
class AlumnoController:
    def __init__(self,typedb) -> None:
        self.__typedb=typedb
    def select_db(self):
        if self.__typedb=="postgres":
            return AlumnoPostgres()
        elif self.__typedb=="sqlite3":
            return AlumnoSqlite3()
            