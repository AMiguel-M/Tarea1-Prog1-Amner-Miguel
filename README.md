# 🎓 Sistema de Gestión de Alumnos

Este es un programa interactivo en consola desarrollado en Python puro que permite administrar una base de datos de estudiantes en PostgreSQL. Cumple con operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sin el uso de ORMs ni frameworks adicionales.

## 📁 Estructura del Proyecto

El proyecto está modularizado en tres archivos principales para mantener un código limpio y organizado:

* **`main.py`**: Es el archivo principal que arranca la aplicación. Contiene la interfaz del menú interactivo y la lógica de validación de entradas.
* **`conexion.py`**: Módulo dedicado exclusivamente a establecer y gestionar la conexión segura con el servidor PostgreSQL.
* **`mibase.py`**: Contiene las funciones auxiliares (`execute_query` y `fetch_data`) encargadas de ejecutar las sentencias SQL de forma parametrizada y segura.

---

## ⚠️ Nota importante 

Dado que las credenciales de la base de datos varían según el entorno local, **es necesario actualizar las variables de conexión antes de ejecutar el programa**.

1. Abra el archivo `main.py`.
2. Busque la función `imprimir_menu()`.
3. Modifique las siguientes variables con sus credenciales locales de PostgreSQL:
   ```python
   HOST = "localhost"
   DATABASE = "su_base_de_datos"  # Cambiar por el nombre de su BD local
   USER = "postgres"              # Cambiar por su usuario
   PASSWORD = "su_password"       # Cambiar por su contraseña
   PORT = 5432
