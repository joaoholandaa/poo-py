from repositorio import Repositorio
from databases import PostgresBD

db_conn = PostgresBD()
repo = Repositorio()

repo.insert(db_conn)
repo.select(db_conn)