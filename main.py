import sys
import re
from pathlib import Path
from dataclasses import dataclass, field

from expressoes import *
from tipificacao import *

sys.stdout.reconfigure(encoding='utf-8')

@dataclass
class Ocorrencia:
    n_linha: int
    linha: str
    valido: bool

@dataclass
class Arquivo:
    nome: str
    tipo: 'Tipo'
    n_linhas: int
    ocorrencias: dict[str, list[Ocorrencia]] = field(default_factory=dict)

    def adicionar_ocorrencia(self, tipo: str, ocorrencia: Ocorrencia):
        self.ocorrencias.setdefault(tipo, []).append(ocorrencia)

# Coleta os dados de todos os arquivos disponíveis no diretório
def coletar_dados(dir: Path) -> list[Arquivo]:
    arquivos = [f for f in dir.iterdir() if f.is_file()]
    dados = []

    for arquivo in arquivos:
        tipo = definir_tipo(str(arquivo))

        linhas = []
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
            linhas = conteudo.splitlines()

        n_linhas = len(linhas)
        nova_entrada = Arquivo(str(arquivo), tipo, n_linhas)


        # checa linha por linha
        for num, linha in enumerate(linhas, 1):
            # para todas as expressões regulares permissivas
            for nome, expressao in expressoes_permissivas.items():
                # encontra todas as ocorrencias na linha
                for caso in re.finditer(expressao, linha):
                    # verifica se a ocorrencia é passível de validação
                    if (nome in expressoes_validadoras):
                        # valida e registra a ocorrencia
                        if not re.match(expressoes_validadoras[nome], caso.group()): 
                            nova_ocorrencia = Ocorrencia(num, linha, False) 
                        else:
                            nova_ocorrencia = Ocorrencia(num, linha, True)
                        nova_entrada.adicionar_ocorrencia(nome, nova_ocorrencia)
        
        dados.append(nova_entrada)
    
    return dados


def main():
    pasta = Path("./arquivos/")
    dados = coletar_dados(pasta)

        
if (__name__ == "__main__"):
    main()