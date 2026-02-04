# Servidor-MCP-pagila

# 📊 Servidor MCP Pagila – Consultas Inteligentes a Base de Datos

## 📌 Descripción del proyecto
Este proyecto implementa un **servidor MCP (Model Context Protocol)** conectado a la base de datos **Pagila (PostgreSQL)**, que permite realizar consultas seguras y controladas desde clientes compatibles como 

**Claude Desktop**.
El sistema está diseñado para ejecutar **consultas SQL de solo lectura (SELECT)** y sirve como puente entre un modelo de lenguaje y una base de datos relacional, garantizando seguridad, control y trazabilidad.

## 🎯 Objetivos
- Conectar un servidor MCP a una base de datos PostgreSQL (Pagila)
- Permitir consultas SQL controladas (solo SELECT)
- Bloquear operaciones peligrosas (INSERT, UPDATE, DELETE)
- Exponer herramientas MCP para:
  - Verificar conexión
  - Listar tablas
  - Listar columnas
  - Ejecutar consultas SQL
- Integrar el servidor con **Claude Desktop**
- Permitir consultas analíticas y en lenguaje natural

## 🛠️ Tecnologías utilizadas
- **Python 3.14**
- **PostgreSQL 17**
- **Base de datos Pagila**
- **Model Context Protocol (MCP)**
- **Claude Desktop**
- **MCP Inspector**
- **psycopg2 / psycopg (PostgreSQL driver)**

## 📂 Estructura del proyecto
pagila-mcp-server/
│
├── main.py # Servidor MCP principal
├── requirements.txt # Dependencias del proyecto


## 🚀 Funcionalidades principales

### ✔️ Herramientas MCP disponibles
- **check_db_status**  
  Verifica la conexión a la base de datos y devuelve información básica.

- **list_tables**  
  Lista las tablas disponibles en el esquema de Pagila.

- **list_columns**  
  Lista las columnas de una tabla específica.

- **sql_query**  
  Ejecuta consultas SQL **exclusivamente SELECT**, con límite de resultados y validación de seguridad.


## 🔐 Seguridad y control
El servidor implementa las siguientes medidas de seguridad:

- ❌ Bloqueo de consultas `INSERT`, `UPDATE`, `DELETE`, `DROP`, `ALTER`
- ✅ Validación de que la consulta comience con `SELECT`
- ⏱️ Control de tiempo de ejecución
- 🧾 Manejo de errores controlado
- 📜 Registro de consultas ejecutadas

Esto garantiza que el acceso a la base de datos sea **seguro y no destructivo**.


## 🤖 Integración con Claude Desktop
El servidor MCP se conecta correctamente a **Claude Desktop** mediante configuración local de servidores MCP.

Esto permite realizar:
- Consultas directas a la base de datos desde Claude
- Análisis de datos
- Consultas en lenguaje natural traducidas a SQL
- Generación de reportes y análisis gráficos


Cómo ejecutar el proyecto

1️⃣ Instalar dependencias
pip install -r requirements.txt

2️⃣ Ejecutar el servidor MCP
python main.py

3️⃣ Conectar desde Claude Desktop
Configurar el servidor MCP local apuntando al archivo main.py.

📎 Repositorio
Este repositorio contiene todo el código fuente, configuración y documentación necesarios para reproducir el proyecto.

👨‍🎓 Autor
Proyecto desarrollado como parte de un trabajo académico sobre Lenguajes de Programación / MCP / Bases de Datos, integrando modelos de lenguaje con sistemas de información reales.

Entregable 3 – Preparación de la base de datos
![WhatsApp Image 2026-02-03 at 18 14 43](https://github.com/user-attachments/assets/4406c75c-9786-4c68-ba74-46df59d619cb)

Entregable 4 – Implementación del servid
<img width="1600" height="730" alt="image" src="https://github.com/user-attachments/assets/9be8f9e7-d512-4a3b-9fe6-e3b3716e90d7" />

Entregable 5 – Seguridad y control
<img width="1600" height="737" alt="image" src="https://github.com/user-attachments/assets/b14dbd6b-1692-4932-9c96-4d2ec1e90b3e" />
<img width="1600" height="717" alt="image" src="https://github.com/user-attachments/assets/9888b678-ef7f-472f-9635-ad0c1e4b6440" />
<img width="1600" height="737" alt="image" src="https://github.com/user-attachments/assets/860c21c7-1600-4c3b-8578-492dc1b1b2e8" />
<img width="1600" height="728" alt="image" src="https://github.com/user-attachments/assets/6dd88f53-05ba-4b39-9b77-ae7066d55e8b" />
<img width="715" height="335" alt="image" src="https://github.com/user-attachments/assets/e0864b8c-867c-4e20-9a9b-447d6e12d73c" />

Entregable 6 – Consultas en lenguaje natural
<img width="1600" height="827" alt="image" src="https://github.com/user-attachments/assets/7e9eb360-9a03-4856-8de4-554d1fed6e79" />

EJECUCION DEL PROYECTO
![WhatsApp Image 2026-02-04 at 09 54 56](https://github.com/user-attachments/assets/085a507b-e8d7-4421-8052-3db2ded085d3)
![WhatsApp Image 2026-02-04 at 10 25 46](https://github.com/user-attachments/assets/66b332c1-2638-4314-af33-05b9dfa207a6)
![WhatsApp Image 2026-02-04 at 10 25 46](https://github.com/user-attachments/assets/6cd69962-3aad-4469-b3ad-5e5d16f20c6f)










