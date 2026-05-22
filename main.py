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
    valor: str

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
                        valor = caso.group()

                        # valida a ocorrencia
                        valido = bool(re.match(expressoes_validadoras[nome],valor))
                        
                        # registra a ocorrencia
                        nova_ocorrencia = Ocorrencia(n_linha=num, linha=linha, valor=valor, valido=valido)
                        nova_entrada.adicionar_ocorrencia(nome, nova_ocorrencia)
        
        dados.append(nova_entrada)
    
    return dados

def exportar_ocorrencias(dados: list[Arquivo]):
    with open("ocorrencias.txt", "w", encoding="utf-8") as arquivo_saida:
        arquivo_saida.write("=" * 100 + "\n")
        arquivo_saida.write("Listagem Completa de Ocorrências\n")
        arquivo_saida.write("=" * 100 + "\n")

        for arquivo in dados:
            arquivo_saida.write("\n")
            arquivo_saida.write("=" * 100 + "\n")
            arquivo_saida.write(f"Arquivo: {arquivo.nome}\n")
            arquivo_saida.write("=" * 100 + "\n")

            if not arquivo.ocorrencias:
                arquivo_saida.write("nenhuma ocorrencia encontrada")
                continue
            
            for tipo, ocorrencias in arquivo.ocorrencias.items():
                arquivo_saida.write("\n")
                arquivo_saida.write("-" * 100 + "\n")
                arquivo_saida.write(f"TIPO DE DADO: {tipo}\n")
                arquivo_saida.write(f"TOTAL DE OCORRÊNCIAS: {len(ocorrencias)}\n")
                arquivo_saida.write("-" * 100 + "\n")

                for ocorrencia in ocorrencias:
                    status = ("VÁLIDO" if ocorrencia.valido else "INVÁLIDO")

                    arquivo_saida.write(f"\nLinha: {ocorrencia.n_linha}\n")
                    arquivo_saida.write(f"Valor extraído: {ocorrencia.valor}\n")
                    arquivo_saida.write(f"Classificação: {status}\n")
                    arquivo_saida.write("Linha original:\n")
                    arquivo_saida.write(f"{ocorrencia.linha}\n")

                    arquivo_saida.write("-" * 100 + "\n")


def main():
    pasta = Path("./arquivos/")
    dados = coletar_dados(pasta)
   
    estatisticas = {}
    total_dados = 0

    for arquivos in dados:
        for tipo,ocorrencias in arquivos.ocorrencias.items():
            if tipo not in estatisticas:
                estatisticas[tipo] = {
                    "total": 0,
                    "validas": 0,
                    "invalidas": 0,
                    "quantidade_por_arquivo": {}
                }

            if arquivos.nome not in estatisticas[tipo]["quantidade_por_arquivo"]:
                estatisticas[tipo]["quantidade_por_arquivo"][arquivos.nome] = {
                    "total" : 0,
                    "validas": 0,
                    "invalidas": 0
            }

            for ocorrencia in ocorrencias:
                estatisticas[tipo]["total"] += 1
                estatisticas[tipo]["quantidade_por_arquivo"][arquivos.nome]["total"] += 1
                total_dados += 1

                if ocorrencia.valido:
                    estatisticas[tipo]["validas"] += 1
                    estatisticas[tipo]["quantidade_por_arquivo"][arquivos.nome]["validas"] += 1
                else:
                    estatisticas[tipo]["invalidas"] += 1
                    estatisticas[tipo]["quantidade_por_arquivo"][arquivos.nome]["invalidas"] += 1

    print("\n" + "=" * 100)
    print("Analise quantitativa")
    print("=" * 100)

    print(f"total de dados: {total_dados}")
        
    for tipo,info in estatisticas.items():
        total = info["total"]
        validas = info["validas"]
        invalidas = info["invalidas"]

        porcentagem_validas = (validas / total) * 100
        porcentagem_invalidas = (invalidas / total) * 100
        
        print("\n" + "=" * 100)
        print(f"tipo do dado: {tipo}")
        print("=" *100)

        print(f"TOTAL: {total}")
        print(f"VÁLIDAS: {validas} ({porcentagem_validas:.2f}%)")
        print(f"INVÁLIDAS: {invalidas} ({porcentagem_invalidas:.2f}%)")
        

        print("\nDistribuição por arquivo: ")
        print("-" * 100)

        arquivos_ordenados = sorted(
            info["quantidade_por_arquivo"].items(),
            key=lambda item: item[1]["total"],
            reverse=True
        )
        
        for nome_arquivo, dados_arquivo in arquivos_ordenados:
            total_arquivo = dados_arquivo["total"]
            validas_arquivo = dados_arquivo["validas"]
            invalidas_arquivo = dados_arquivo["invalidas"]

            porcentagem_invalida_arquivo = (invalidas_arquivo / total_arquivo) * 100
            porcentagem_valida_arquivo = (validas_arquivo / total_arquivo) * 100

            print(f"\nArquivo: {nome_arquivo}")
            print(f"Total: {total_arquivo}")
            print(f"Válidas: {validas_arquivo}")
            print(f"Inválidas: {invalidas_arquivo}")
            print(f"Taxa de inválidas: {porcentagem_invalida_arquivo:.2f}%")
            print(f"Taxa de nválidas: {porcentagem_valida_arquivo:.2f}%")
    exportar_ocorrencias(dados)

             
if (__name__ == "__main__"):
    main()
