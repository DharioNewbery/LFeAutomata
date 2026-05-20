from enum import Enum
from expressoes import expressoes_arquivo
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

    for linha in amostra:
        if re.match(expressoes_arquivo["chat"], linha):
            pontuacao += 3

    if pontuacao < tamanho_amostra / 2:
        return Tipo.TXT

    return Tipo.CHAT
