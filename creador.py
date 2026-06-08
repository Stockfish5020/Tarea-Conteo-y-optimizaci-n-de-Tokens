import requests

# =====================================================================
# CONFIGURACIÓN DEL ENTORNO LOCAL (OLLAMA)
# =====================================================================
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL_NAME = "gemma4:E4B"  # Cambia por el modelo que tengas en ollama list

# =====================================================================
# CONEXIÓN CLIENTE API CON OLLAMA LOCALHOST
# =====================================================================
def consultar_ollama(prompt_sistema: str, prompt_usuario: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": prompt_usuario}
        ],
        "temperature": 0.7  # Más creatividad para inventar proyectos
    }
    headers = {"Content-Type": "application/json"}

    try:
        respuesta = requests.post(OLLAMA_URL, json=payload, headers=headers, timeout=120)
        respuesta.raise_for_status()
        datos = respuesta.json()
        return datos["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ Error de conexión con Ollama: {e}"


# =====================================================================
# PROMPT DEL SISTEMA — ROL DE LA IA
# =====================================================================
PROMPT_SISTEMA = """
Eres un Arquitecto Senior de Sistemas de Inteligencia Artificial con amplia experiencia
en diseño de sistemas multi-agente. Tienes total libertad creativa.

Tu tarea tiene DOS partes:

--- PARTE 1: INVENTA EL PROYECTO ---
Imagina un proyecto de software original e interesante. Puede ser cualquier cosa:
una app, un sistema de análisis, una herramienta de automatización, un juego, etc.
Descríbelo en 3-5 líneas. Sé específico y creativo. No elijas algo genérico.

--- PARTE 2: DISEÑA LOS AGENTES ---
Basándote en el proyecto que inventaste, define cuántos agentes necesitas.
NO hay un número fijo — usa los que el problema realmente requiera y justifica por qué.

Para cada agente, escribe:
  - Nombre y letra identificadora (A, B, C, ...)
  - Rol principal (una línea)
  - Responsabilidades detalladas (3-5 puntos)
  - Herramientas o librerías que usaría
  - Con quién se comunica (qué agente le envía trabajo y a quién le devuelve)

--- PARTE 3: FLUJO DE TRABAJO ---
Describe el flujo completo en texto narrativo, como si le explicaras a un desarrollador
junior cómo viajan los datos desde que el usuario inicia el sistema hasta que obtiene
el resultado final. Incluye qué pasa en cada paso y por qué el flujo tiene ese orden.

--- PARTE 4: POR QUÉ ESE NÚMERO DE AGENTES ---
Justifica por qué elegiste esa cantidad. ¿Por qué no menos? ¿Por qué no más?

Responde en español. Usa formato legible con secciones claras. No uses JSON.
"""

PROMPT_USUARIO = """
Inventa un proyecto completamente nuevo desde cero y diseña su arquitectura de agentes.
Crear un conjunto de agentes que puedan codificar codigo, y validadrrlo con pruebas unitarias, 
y luego integrarlo en un sistema completo. El proyecto debe ser interesante y desafiante, no algo trivial. 
Describe cada agente con detalle y explica el flujo de trabajo entre ellos.
"""


# =====================================================================
# EJECUCIÓN
# =====================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("🤖 GENERADOR DE ARQUITECTURAS MULTI-AGENTE — MODO LIBRE")
    print("=" * 65)
    print(f"📡 Conectando a Ollama ({MODEL_NAME})...\n")

    respuesta = consultar_ollama(PROMPT_SISTEMA, PROMPT_USUARIO)

    print(respuesta)
    print("\n" + "=" * 65)

    with open("respuesta_ollama.txt", "w", encoding="utf-8") as f:
        f.write(respuesta)

    print("✅ Generación completada.")