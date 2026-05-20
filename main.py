import sys
sys.stdout.reconfigure(encoding='utf-8')

from enum import Enum
from pathlib import Path
from expressoes import *
import re

class Tipo(Enum):
    CSV  = 0
    LOG  = 1
    TXT  = 2
    CHAT = 3 
    NDF  = -1

# Identificando através da extensão do arquivo
def definir_tipo(nome_arquivo: str) -> Tipo:
    
    if (nome_arquivo.endswith(".log")): return Tipo.LOG
    if (nome_arquivo.endswith(".csv")): return Tipo.CSV
    if (nome_arquivo.endswith(".txt")):
        with open(nome_arquivo) as f:   return identificar_txt(f.read())

    return Tipo.NDF

# Determina se o arquivo .txt é do tipo chat (CHAT) ou texto livre (TXT)
def identificar_txt(conteudo) -> Tipo:
    # transforma o texto em uma amostra de linhas.
    tamanho_amostra = 30
    amostra = conteudo.splitlines()[:tamanho_amostra]

    # contador de pontuação para verificar qual tipo de arquivo tá sendo tratado.
    pontuacao = 0

    #expressão regular para chat ( peguei da internet mesmo )
    padrao_chat = r'^\[\d{2}/\d{2}/\d{4}\s\d{2}:\d{2}:\d{2}\]\s.+:'

    for linha in amostra:
        if re.match(padrao_chat, linha):
            pontuacao += 3

    if pontuacao < tamanho_amostra / 2:
        return Tipo.TXT

    return Tipo.CHAT

def main():
    arquivos = [f for f in Path('./arquivos').iterdir() if f.is_file()]

    for arquivo in arquivos:
        tipo = definir_tipo(str(arquivo))

        conteudo = ""
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()

        linhas = conteudo.splitlines()

        with open(f"resultados/{arquivo.name}", "w", encoding="utf-8") as f:
            f.write(f"Arquivo: {arquivo}\n")
            f.write(f"Quantidade de linhas: {len(linhas)}\n")
            f.write(f"Tipo identificado: {tipo.name}\n")
            f.write("\nAmostra do conteúdo:\n")

            for linha in linhas[:5]:
                f.write(linha + '\n')
            f.write("\n\n\n")
            f.write("Ocorrencias:")

            for nome, expressao in expressoes.items():
                f.write(f"\n\n================ {nome} ================\n")

                for num, linha in enumerate(linhas, 1):
                    for item in re.finditer(expressao, linha):
                        f.write(f"{num} {item.group()}\n")


            """
            for nome, expressao in expressoes.items():

                f.write(f"\n\n================ {nome} ================\n")
                for item in re.finditer(expressao, conteudo):

                    num_linha = conteudo.count('\n', 0, item.start()) + 1
                    f.write(f"{num_linha} {item.group()}\n")
            """
        

if (__name__ == "__main__"):
    main()