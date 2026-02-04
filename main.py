import os
import re
import time
from typing import Any, Dict

import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

from mcp.server.fastmcp import FastMCP

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "pagila")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
STATEMENT_TIMEOUT_MS = int(os.getenv("DB_STATEMENT_TIMEOUT_MS", "5000"))

mcp = FastMCP("Pagila MCP Server", json_response=True)

FORBIDDEN = re.compile(
    r"\b(insert|update|delete|drop|alter|create|truncate|grant|revoke|copy|call|do)\b",
    re.IGNORECASE,
)

def validate_sql(query: str) -> str:
    if not query or not query.strip():
        raise ValueError("La consulta está vacía.")

    q = query.strip()

    # bloquea múltiples sentencias
    if ";" in q:
        raise ValueError("Solo se permite 1 sentencia. Quita el ';'.")

    # solo SELECT o WITH
    first = q.split(None, 1)[0].lower()
    if first not in ("select", "with"):
        raise ValueError("Solo se permiten consultas SELECT (o WITH ... SELECT).")

    if FORBIDDEN.search(q):
        raise ValueError("Consulta rechazada: contiene operaciones no permitidas.")

    return q

def db_connect():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        cursor_factory=RealDictCursor,
        options=f"-c statement_timeout={STATEMENT_TIMEOUT_MS}",
    )
    conn.autocommit = True
    return conn

@mcp.tool()
def check_db_status() -> Dict[str, Any]:
    """Verifica conexión y devuelve información básica."""
    t0 = time.time()
    conn = db_connect()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT current_database() AS db, current_user AS user;")
            row = cur.fetchone()
        return {
            "ok": True,
            "db": row["db"],
            "user": row["user"],
            "latency_ms": int((time.time() - t0) * 1000),
        }
    finally:
        conn.close()

@mcp.tool()
def list_tables(schema: str = "public") -> Dict[str, Any]:
    """Lista tablas del esquema indicado."""
    conn = db_connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = %s AND table_type='BASE TABLE'
                ORDER BY table_name;
                """,
                (schema,),
            )
            rows = cur.fetchall()
        return {"schema": schema, "tables": [r["table_name"] for r in rows]}
    finally:
        conn.close()

@mcp.tool()
def list_columns(table: str, schema: str = "public") -> Dict[str, Any]:
    """Lista columnas de una tabla."""
    conn = db_connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT column_name, data_type, is_nullable
                FROM information_schema.columns
                WHERE table_schema = %s AND table_name = %s
                ORDER BY ordinal_position;
                """,
                (schema, table),
            )
            cols = cur.fetchall()
        return {"schema": schema, "table": table, "columns": cols}
    finally:
        conn.close()

@mcp.tool()
def sql_query(query: str, limit: int = 200) -> Dict[str, Any]:
    """Ejecuta un SELECT controlado (solo lectura)."""
    q = validate_sql(query)

    # aplica limit si no existe
    if " limit " not in q.lower():
        q = f"{q.rstrip()} LIMIT {int(limit)}"

    conn = db_connect()
    try:
        with conn.cursor() as cur:
            cur.execute(q)
            rows = cur.fetchall()
        return {"ok": True, "row_count": len(rows), "rows": rows, "applied_limit": int(limit)}
    finally:
        conn.close()

if __name__ == "__main__":
    mcp.run()
