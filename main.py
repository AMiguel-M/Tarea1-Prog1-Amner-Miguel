from conexion import create_connection
from mibase import fetch_data, execute_query

#Función para crear la tabla si no existe
def crear_tabla_si_no_existe(conexion):
    print("\n⚙️ Verificando si la tabla 'alumnos' existe...")
    query = """
    CREATE TABLE IF NOT EXISTS alumnos (
        id SERIAL PRIMARY KEY,
        carnet VARCHAR(100) UNIQUE NOT NULL,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        carrera VARCHAR(150),
        email VARCHAR(150),
        telefono VARCHAR(20),
        fecha_registro DATE
    );
    """
    execute_query(conexion, query)

def imprimir_menu():
    # 1. Configuramos las credenciales
    HOST = "localhost"
    DATABASE = "Tarea1"
    USER = "postgres"
    PASSWORD = "miniyo132"
    PORT = 5432
    
    # 2. Abrimos la conexión UNA SOLA VEZ
    conexion = create_connection(HOST, DATABASE, USER, PASSWORD, PORT)
    
    if conexion is None:
        print("❌ No se pudo iniciar el sistema. Revisa tu base de datos.")
        return

    # 3.Construimos la tabla antes de abrir el menú
    crear_tabla_si_no_existe(conexion)

    # 4. Iniciamos el bucle del menú interactivo
    while True:
        print("\n" + "="*35)
        print("      MENÚ DE GESTIÓN DE ALUMNOS")
        print("="*35)
        print("1. Agregar alumno")
        print("2. Modificar datos de un alumno por carnet")
        print("3. Listar todos los alumnos")
        print("4. Eliminar alumno por carnet")
        print("5. Salir")
        print("="*35)
        
        opcion = input("👉 Ingrese el número de la opción deseada: ")

        # --- OPCIÓN 1: AGREGAR ALUMNO ---
        if opcion == '1':
            print("\n--- AGREGAR NUEVO ALUMNO ---")
            carnet = input("Carnet: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carrera = input("Carrera: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            fecha_registro = input("Fecha de registro (YYYY-MM-DD): ") 
            
            query = """
                INSERT INTO alumnos (carnet, nombre, apellido, carrera, email, telefono, fecha_registro) 
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            valores = (carnet, nombre, apellido, carrera, email, telefono, fecha_registro)
            execute_query(conexion, query, valores)

        # --- OPCIÓN 2: MODIFICAR ALUMNO ---
        elif opcion == '2':
            print("\n--- MODIFICAR ALUMNO ---")
            carnet_buscar = input("Ingrese el CARNET del alumno a modificar: ")
            
            # Pedimos los nuevos datos
            print("Ingrese los nuevos datos (presione Enter si no desea cambiar algún campo):")
            nuevo_nombre = input("Nuevo Nombre: ")
            nuevo_apellido = input("Nuevo Apellido: ")
            nueva_carrera = input("Nueva Carrera: ")
            nuevo_email = input("Nuevo Email: ")
            nuevo_telefono = input("Nuevo Teléfono: ")
            
            # Usamos COALESCE y NULLIF para mantener el dato original si se envía vacío
            query = """
                UPDATE alumnos 
                SET 
                    nombre = COALESCE(NULLIF(%s, ''), nombre),
                    apellido = COALESCE(NULLIF(%s, ''), apellido),
                    carrera = COALESCE(NULLIF(%s, ''), carrera),
                    email = COALESCE(NULLIF(%s, ''), email),
                    telefono = COALESCE(NULLIF(%s, ''), telefono)
                WHERE carnet = %s;
            """
            valores = (nuevo_nombre, nuevo_apellido, nueva_carrera, nuevo_email, nuevo_telefono, carnet_buscar)
            execute_query(conexion, query, valores)
            
        # --- OPCIÓN 3: LISTAR ALUMNOS ---
        elif opcion == '3':
            print("\n--- LISTADO DE ALUMNOS ---")
            query = "SELECT * FROM alumnos;"
            filas = fetch_data(conexion, query)
            
            if filas:
                for fila in filas:
                    # Desempaquetamos la tupla en variables individuales
                    id_al, carnet, nombre, apellido, carrera, email, tel, fecha = fila
                    
                    # Imprimimos con un formato ordenado y limpio
                    print(f"🎓 Carnet: {carnet} | Nombre: {nombre} {apellido} | Carrera: {carrera} | Registro: {fecha}")
            else:
                print("⚠️ No hay alumnos registrados en la base de datos.")

        # --- OPCIÓN 4: ELIMINAR ALUMNO ---
        elif opcion == '4':
            print("\n--- ELIMINAR ALUMNO ---")
            carnet_eliminar = input("Ingrese el CARNET del alumno que desea ELIMINAR: ")
            
            query = "DELETE FROM alumnos WHERE carnet = %s;"
            valores = (carnet_eliminar,) # Nota: La coma es obligatoria para que Python lo tome como tupla
            execute_query(conexion, query, valores)

        # --- OPCIÓN 5: SALIR ---
        elif opcion == '5':
            print("\nSaliendo del sistema...")
            break # Esto rompe el ciclo while y salta a la línea de cerrar conexión

        # --- OPCIÓN INVÁLIDA ---
        else:
            print("\n❌ Opción no válida. Por favor, ingrese un número del 1 al 5.")

    # 4. Cerramos la conexión de forma segura SOLO cuando el bucle termine (al elegir 5)
    conexion.close()
    print("🔒 Conexión a la base de datos cerrada correctamente.")

# Ejecutamos la función
if __name__ == "__main__":
    imprimir_menu()