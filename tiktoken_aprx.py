# Guardar como contar_tokens.py
import os
import sys

def contar_tokens_detallado(archivo):
    """Cuenta tokens usando tiktoken con información detallada."""
    try:
        import tiktoken
    except ImportError:
        print("Instalando tiktoken...")
        os.system(f"{sys.executable} -m pip install tiktoken -q")
        import tiktoken
    
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Diferentes encodings para distintos modelos
    encodings = {
        "GPT-4/GPT-3.5 (cl100k_base)": tiktoken.get_encoding("cl100k_base"),
        "GPT-2 (gpt2)": tiktoken.get_encoding("gpt2"),
        "Codex (p50k_base)": tiktoken.get_encoding("p50k_base"),
    }
    
    print(f"📊 ANÁLISIS DE TOKENS: {archivo}")
    print("=" * 50)
    print(f"📏 Caracteres totales: {len(contenido):,}")
    print(f"📄 Líneas: {contenido.count(chr(10)):,}")
    print(f"📝 Palabras: {len(contenido.split()):,}")
    print()
    
    for modelo, encoding in encodings.items():
        tokens = len(encoding.encode(contenido))
        print(f"🔤 {tokens:,} tokens")


if __name__ == "__main__":
    archivo = sys.argv[1] if len(sys.argv) > 1 else "agentes/agent_1.md"
    contar_tokens_detallado(archivo)
    archivo = sys.argv[1] if len(sys.argv) > 1 else "agentes/agent_2.md"
    contar_tokens_detallado(archivo)
    archivo = sys.argv[1] if len(sys.argv) > 1 else "agentes/agent_3.md"
    contar_tokens_detallado(archivo)