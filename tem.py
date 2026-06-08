import sqlite3
import json

DB = r"C:\Users\USER\.local\share\opencode\opencode.db"

def get_last_session():
    con = sqlite3.connect(DB)
    cur = con.cursor()

    row = cur.execute("""
        SELECT
            id,
            title,
            model,
            tokens_input,
            tokens_output,
            tokens_reasoning,
            tokens_cache_read,
            tokens_cache_write,
            cost
        FROM session
        ORDER BY time_updated DESC
        LIMIT 1
    """).fetchone()

    con.close()
    return row

def get_last_prompt(session_id):
    con = sqlite3.connect(DB)
    cur = con.cursor()

    row = cur.execute("""
        SELECT p.data
        FROM part p
        JOIN message m ON p.message_id = m.id
        WHERE m.session_id = ?
          AND json_extract(m.data, '$.role') = 'user'
        ORDER BY p.time_created DESC
        LIMIT 1
    """, (session_id,)).fetchone()

    con.close()

    if not row:
        return None

    try:
        data = json.loads(row[0])
        return data.get("text", "")
    except Exception:
        return None

def fmt(n):
    return f"{n:,}" if n else "0"

session = get_last_session()

if not session:
    print("No se encontraron sesiones.")
    exit()

(
    session_id,
    title,
    model,
    tokens_input,
    tokens_output,
    tokens_reasoning,
    tokens_cache_read,
    tokens_cache_write,
    cost
) = session

try:
    model_id = json.loads(model).get("id", model)
except:
    model_id = model

prompt = get_last_prompt(session_id)

print("=" * 60)
print("ÚLTIMA SESIÓN")
print("=" * 60)
print(f"Título          : {title}")
print(f"Modelo          : {model_id}")
print()
print("PROMPT:")
print("-" * 60)
print(prompt or "(vacío)")
print("-" * 60)
print()
print(f"Input Tokens    : {fmt(tokens_input)}")
print(f"Output Tokens   : {fmt(tokens_output)}")
print(f"Reasoning       : {fmt(tokens_reasoning)}")
print(f"Cache Read      : {fmt(tokens_cache_read)}")
print(f"Cache Write     : {fmt(tokens_cache_write)}")
print(f"Costo           : ${cost:.6f}")
print()
print(f"TOTAL TOKENS    : {fmt((tokens_input or 0) + (tokens_output or 0))}")