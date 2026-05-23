# Trabalho de Linguagens Formais e Autômatos - Analisador de Padrões Textuais

Este repositório contém o código-fonte desenvolvido para o trabalho prático da disciplina de Linguagens Formais e Autômatos. O objetivo do projeto é utilizar Expressões Regulares (Regex) para identificar, extrair e validar padrões textuais e estruturas de dados em diversos arquivos textuais brutos.

## Descrição do Projeto

O sistema realiza a leitura de arquivos de entrada (como logs de servidores, conversas de chat, planilhas CSV e textos livres), identifica o tipo de arquivo analisado e varre linha por linha em busca de padrões pré-definidos de informação. O validador diferencia padrões gerais de formatos estritamente válidos, calculando a integridade estatística dos dados processados.

---

## Estrutura do Repositório

Abaixo está listada a estrutura de arquivos do trabalho:

```text
LFeAutomata/
├── arquivos/                           # Diretório contendo as bases de dados de entrada
│   ├── 01_atendimentos_baguncados.txt  # Relatório textual de atendimentos
│   ├── 02_logs_mistos.log              # Log de eventos e transações
│   ├── 03_mensagens_chat.txt           # Mensagens brutas obtidas de chat
│   └── 04_exportacao_suja.csv          # Banco de dados exportado em formato CSV
├── expressoes.py                       # Dicionários com as expressões regulares (Regex)
├── tipificacao.py                      # Funções para identificação de tipo de arquivo
├── main.py                             # Script principal de execução
├── ocorrencias.txt                     # Relatório detalhado das extrações (gerado após a execução)
└── analise_quantitativa.txt            # Resumo estatístico geral (gerado após a execução)
```

---

## Descrição dos Arquivos de Código

### main.py
É o ponto de entrada do programa. Ele lê os arquivos na pasta `arquivos/`, faz a classificação do tipo de cada um, executa as buscas e validações por expressões regulares de cada linha, e realiza a validação de formatação de colunas em arquivos CSV. Ao final, gera os dois relatórios de saída.

### expressoes.py
Centraliza todas as expressões regulares do projeto:
* **expressoes_arquivo**: Padrões usados para reconhecer a estrutura interna de linhas (como o cabeçalho de mensagens de chat).
* **expressoes_permissivas**: Regex flexíveis usadas para capturar potenciais candidatos de informação (ex. qualquer e-mail ou CPF, mesmo com formatação incorreta).
* **expressoes_validadoras**: Regex rígidas utilizadas para certificar se os dados capturados estão no formato correto especificado (ex. e-mail formal, CPF com máscara padrão).

### tipificacao.py
Implementa a lógica para definir o tipo de arquivo de entrada. Arquivos `.log` e `.csv` são tipificados pela extensão. Arquivos `.txt` passam por uma análise de amostragem estatística das primeiras 30 linhas para determinar se trata-se de um chat estruturado (padrão `CHAT`) ou um texto comum (`TXT`).

---

## Padrões de Informação Analisados

O trabalho identifica e analisa os seguintes tipos de informações:

* **CPF**: Busca CPFs formatados ou apenas números, validando o padrão oficial com máscara (xxx.xxx.xxx-xx).
* **E-mail**: Captura endereços eletrônicos comuns e os valida em conformidade com as regras básicas de domínio e sufixo.
* **Telefone**: Captura números telefônicos e valida formatos nacionais com ou sem DDD, com 8 ou 9 dígitos.
* **URL**: Identifica hiperlinks e valida se possuem prefixo obrigatório http/https ou www.
* **Data**: Extrai datas de calendário no formato dd/mm/aaaa ou dd-mm-aaaa.
* **Horário**: Extrai horas, minutos e segundos opcionais.
* **Data e Horário**: Reconhece registros de timestamp conjuntos.
* **Valor Monetário**: Reconhece representações de valores em Real (R$).
* **Nome**: Reconhece nomes próprios aproximados por sequências de palavras iniciadas em maiúscula.
* **Linhas de CSV**: Valida se todas as linhas da exportação CSV possuem o número correto de colunas em relação ao cabeçalho.

---

## Como Executar o Projeto

Este projeto foi construído utilizando exclusivamente a biblioteca padrão do Python, não necessitando de nenhuma instalação de pacotes externos.

### Pré-requisito
* Python 3.10 ou superior instalado no sistema.

### Passo a Passo
1. Abra o terminal na raiz do projeto (`LFeAutomata/`).
2. Execute o comando principal:

```bash
python main.py
```

*(Caso o sistema utilize comandos específicos de versão, pode ser necessário executar `python3 main.py`).*

### Resultados Esperados
Após o término do script, o programa salvará os seguintes arquivos na raiz do projeto:
* **`ocorrencias.txt`**: Listagem linha por linha com a classificação e o status (VÁLIDO ou INVÁLIDO) de cada ocorrência.
* **`analise_quantitativa.txt`**: Resumo das métricas de acerto geral e de integridade por arquivo e por tipo de dado.
