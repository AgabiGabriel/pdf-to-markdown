import os
import pymupdf4llm
from markitdown import MarkItDown # Sugestão: Tente usar essa lib da Microsoft

# --- PROTEÇÃO DE DIRETÓRIO (Para funcionar de qualquer terminal) ---
DIRETORIO_SCRIPT = os.path.dirname(os.path.abspath(__file__))
PASTA_ENTRADA = os.path.join(DIRETORIO_SCRIPT, "entrada")
PASTA_SAIDA = os.path.join(DIRETORIO_SCRIPT, "saida")

# Garante que as pastas existem
os.makedirs(PASTA_ENTRADA, exist_ok=True)
os.makedirs(PASTA_SAIDA, exist_ok=True)
# -----------------------------------------------------------------

print(f" Lendo arquivos de: {PASTA_ENTRADA}")

arquivos = os.listdir(PASTA_ENTRADA)

# Inicializa o conversor da Microsoft (Opcional)
md_microsoft = MarkItDown()

for arquivo in arquivos:
    caminho_completo_pdf = os.path.join(PASTA_ENTRADA, arquivo)
    nome_novo = os.path.splitext(arquivo)[0] + ".md"
    caminho_completo_md = os.path.join(PASTA_SAIDA, nome_novo)
    
    texto_md = ""

    # CASO 1: PDF
    if arquivo.lower().endswith(".pdf"):
        print(f" Processando PDF: {arquivo}")
        
        try:
            # Usando PyMuPDF (Rápido)
            texto_md = pymupdf4llm.to_markdown(caminho_completo_pdf)
            
            # Usar MarkItDown da Microsoft
            # resultado = md_microsoft.convert(caminho_completo_pdf)
            # texto_md = resultado.text_content
            
        except Exception as e:
            print(f" Erro ao ler PDF: {e}")

    # CASO 2: Se não for PDF, pula
    else:
        continue

    # SALVAR
    if texto_md:
        with open(caminho_completo_md, "w", encoding="utf-8") as f:
            f.write(texto_md)
        print(f" Salvo em: {caminho_completo_md}")
    else:
        print(f" Arquivo gerado vazio (Talvez seja um PDF escaneado/imagem?)")

print("\n🏁 Processamento finalizado.")
