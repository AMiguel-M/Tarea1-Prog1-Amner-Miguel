#Ejecuta una consulta SQL de forma segura usando parámetros.
def execute_query(conn, query, params=None): 
    
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            conn.commit()
            print("✅ Consulta ejecutada correctamente")
    except Exception as e:
        print(f"❌ Error al ejecutar la consulta: {e}")
        conn.rollback()

#Ejecuta una consulta SELECT y devuelve los resultados.
def fetch_data(conn, query, params=None): 
    
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            return cur.fetchall()
    except Exception as e:
        print(f"❌ Error al obtener datos: {e}")
        return []
