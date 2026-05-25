import psycopg2
from psycopg2 import sql, OperationalError

#Crea y devuelve una conexión a PostgreSQL.
#Maneja errores de conexión y devuelve None si falla.
def create_connection(host, database, user, password, port=5432):
   
    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        print("✅ Conexión exitosa a PostgreSQL")
        return conn
    except OperationalError as e:
        print(f"❌ Error al conectar a PostgreSQL: {e}")
        return None

