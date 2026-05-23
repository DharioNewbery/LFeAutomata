#Padrões em Regex para cada tipo de dado buscado
expressoes_arquivo = {
    "chat": r'^\[\d{2}/\d{2}/\d{4}\s\d{2}:\d{2}:\d{2}\]\s.+:',
}

expressoes_validadoras = {
    #Explicação: ^ Marca o início da String;
    #Explicação: [a-zA-Z0-9._%+-]+ Aceita letras, números e símbolos comuns antes do @;
    #Explicação: @ Caractere obrigatório do e-mail;
    #Explicação: [a-zA-Z0-9-]+ Domínio (gmail, outlook, institucional e etc), aceita letras, números e hífen, sem aceitar ponto no início;
    #Explicação: (\.[a-zA-Z0-9-]+)+ Ponto e continuação do domínio; exige pelo menos uma parte válida após o ponto, como com ou com.br;
    #Explicação: $ Marca o fim da String;
    "email" : r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$',

    #Explicação: \b marca o limite de uma palavra;
    #Explicação: (?:\+55\s?)? Código do Brasil opcional, com espaço opcional;
    #Explicação: (?:\(?\d{2}\)?\s?)? DDD opcional, podendo vir com ou sem parênteses e com espaço opcional;
    #Explicação: (?:9?\d{4}) Primeiro bloco do telefone, com o 9 opcional e mais 4 dígitos;
    #Explicação: [-\s]? Aceita hífen ou espaço opcional entre os blocos;
    #Explicação: \d{4} Últimos 4 dígitos do telefone;
    #Explicação: \b Fecha o limite da palavra;
    "telefone" : r'^\+?(?:55\s?)?\(?[1-9]{2}\)?\s?(?:9\d{4}|[2-8]\d{3})[-\s]?\d{4}$',

    #Explicação: \b marca o limite de uma palavra;
    #Explicação: \d{3} Três dígitos iniciais do CPF;
    #Explicação: \. Ponto literal entre os blocos do CPF;
    #Explicação: \d{3} Segundo bloco com três dígitos;
    #Explicação: \. Ponto literal entre os blocos do CPF;
    #Explicação: \d{3} Terceiro bloco com três dígitos;
    #Explicação: - Hífen antes dos dois últimos dígitos;
    #Explicação: \d{2} Dois dígitos finais do CPF;
    #Explicação: | Ou, permitindo CPF com pontuação ou sem pontuação;
    #Explicação: \b\d{11}\b CPF sem pontuação, com 11 dígitos seguidos;
    "cpf" :r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',

    #Explicação: \b marca o limite de uma palavra;
    #Explicação: https?:// Aceita http:// ou https://;
    #Explicação: [\w\-._~:/?#\[\]@!$&\'"()*+,;=%]+ Conjunto de caracteres comuns em URLs;
    #Explicação: | Ou, permitindo duas formas de URL;
    #Explicação: \bwww\. Captura URLs que começam com www.;
    #Explicação: \b Fecha o limite da palavra;
    "url" : r'^https?://[a-zA-Z0-9\-._~:/?#\[\]@!$&\'()*+,;=%]+\.[a-zA-Z]{2,}',
}

expressoes_permissivas = {
    #Explicação: \b marca o limite de uma palavra;
    #Explicação: https?:// Aceita o protocolo http:// ou https://;
    #Explicação: \S+ Captura sequências contínuas sem espaço (corpo da requisição);
    #Explicação: | Ou, para capturar o padrão sem protocolo inicial declarado;
    #Explicação: \bwww\. Captura diretamente inícios com www.;
    #Explicação: \S+ Captura o restante da URL sem espaços;
    "url" : r'\bhttps?://\S+|\bwww\.\S+',
    
    #Explicação: \b marca o limite de uma palavra;
    #Explicação: \d{3} Três primeiros dígitos;
    #Explicação: \.? Ponto literal opcional;
    #Explicação: \d{3} Segundo bloco de três dígitos;
    #Explicação: \.? Ponto literal opcional;
    #Explicação: \d{3} Terceiro bloco de três dígitos;
    #Explicação: -? Hífen opcional antes dos dígitos finais;
    #Explicação: \d{2} Dois dígitos terminais;
    #Explicação: \b Limite de palavra (fecha o formato 1);
    #Explicação: | Ou, permitindo o formato contínuo sem pontuação;
    #Explicação: \b\d{11}\b Captura exatamente os 11 dígitos cercados por limites de palavra;
    "cpf" : r'\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b|\b\d{11}\b',

    #Explicação: (?<!\d) Lookbehind negativo para garantir que não haja números conectados antes da cadeia;
    #Explicação: (?:\+?55\s?)? Aceita opcionalmente código DDI (+55 ou 55) seguido de espaço opcional;
    #Explicação: (?:\(?\d{2}\)?\s?)? Aceita opcionalmente DDD de dois dígitos (com ou sem parênteses) e espaço opcional;
    #Explicação: \d{4,5} Bloco inicial do terminal telefônico (móveis com 5 ou fixos com 4 dígitos);
    #Explicação: [-\s]? Hífen ou espaço opcional como divisor de blocos;
    #Explicação: \d{4} Bloco final numérico;
    #Explicação: \b Fecha o limite da palavra;
    "telefone" : r'(?<!\d)(?:\+?55\s?)?(?:\(?\d{2}\)?\s?)?\d{4,5}[-\s]?\d{4}\b',

    #Explicação: [\w._%+\-]+ Classe abrangente que engloba letras, números e símbolos permitidos para o nome de usuário;
    #Explicação: @ Caractere divisor obrigatório;
    #Explicação: [\w.\-]+ Domínio, aceitando letras, números, pontos e hifens para extração ampla;
    #Explicação: (?:\.[a-zA-Z]+)? Grupo opcional para capturar o sufixo final de domínio (TLD);
    "email" : r'[\w._%+\-]+@[\w.\-]+(?:\.[a-zA-Z]+)?',

    #Explicação: \b marca o limite de uma palavra;
    #Explicação: (?:0[1-9]|[12]\d|3[01]) Dia válido, de 01 a 31;
    #Explicação: [/-] Aceita barra ou hífen como separador;
    #Explicação: (?:0[1-9]|1[0-2]) Mês válido, de 01 a 12;
    #Explicação: [/-] Aceita barra ou hífen novamente;
    #Explicação: (?:19|20)\d{2} Ano com 4 dígitos, aceitando 1900 até 2099;
    #Explicação: \b Fecha o limite da palavra;
    "data": r'\b(?:0[1-9]|[12]\d|3[01])[/-](?:0[1-9]|1[0-2])[/-](?:19|20)\d{2}\b',

    #Explicação: \b marca o limite de uma palavra;
    #Explicação: R\$ Identifica o símbolo de moeda real;
    #Explicação: \s? Espaço opcional depois do símbolo;
    #Explicação: \d{1,3} Primeiro grupo de números, geralmente até 3 dígitos;
    #Explicação: (?:\.\d{3})* Grupos opcionais de milhar, como .000 ou .234;
    #Explicação: (?:,\d{2})? Centavos opcionais, como ,50;
    #Explicação: | Ou, permitindo também valores simples sem separador de milhar (Não pega cpf por causa do prefixo R$);
    #Explicação: \d+ Um ou mais dígitos;
    #Explicação: \b Fecha o limite da palavra;
    "valor_monetario": r'\bR\$\s?\d{1,3}(?:\.\d{3})*(?:,\d{2})?\b|\bR\$\s?\d+(?:,\d{2})?\b',

    #Explicação: \b marca o limite de uma palavra;
    #Explicação: [A-ZÁÀÂÃÉÈÊÍÏÓÔÕÖÚÜÇ] Primeira letra maiúscula, incluindo letras acentuadas;
    #Explicação: [a-záàâãéèêíïóôõöúüç]+ Restante da palavra com letras minúsculas e acentuadas;
    #Explicação: (?:\s+[A-ZÁÀÂÃÉÈÊÍÏÓÔÕÖÚÜÇ][a-záàâãéèêíïóôõöúüç]+)+ Exige pelo menos duas palavras com inicial maiúscula;
    #Explicação: Esse critério foi usado para aproximar nomes próprios no texto;
    #Explicação: \b Fecha o limite da palavra;
    "nome": r'\b[A-ZÁÀÂÃÉÈÊÍÏÓÔÕÖÚÜÇ][a-záàâãéèêíïóôõöúüç]+(?:\s+[A-ZÁÀÂÃÉÈÊÍÏÓÔÕÖÚÜÇ][a-záàâãéèêíïóôõöúüç]+)+\b',

    #Explicação: \b marca o limite de uma palavra;
    #Explicação: (?:[01]\d|2[0-3]) Hora válida, de 00 a 23;
    #Explicação: : Dois pontos separando hora e minuto;
    #Explicação: [0-5]\d Minutos válidos, de 00 a 59;
    #Explicação: (?::[0-5]\d)? Segundos opcionais, como :30 ou :59;
    #Explicação: \b Fecha o limite da palavra;
    "horario": r'\b(?:[01]\d|2[0-3]):[0-5]\d(?::[0-5]\d)?\b',

    #Explicação: \b marca o limite de uma palavra;
    #Explicação: A primeira parte do regex captura a data no formato dd/mm/aaaa ou dd-mm-aaaa;
    #Explicação: \s+ Um ou mais espaços entre a data e a hora;
    #Explicação: (?:[01]\d|2[0-3]) Hora válida, de 00 a 23;
    #Explicação: : Dois pontos separando hora e minuto;
    #Explicação: [0-5]\d Minutos válidos, de 00 a 59;
    #Explicação: (?::[0-5]\d)? Segundos opcionais;
    #Explicação: \b Fecha o limite da palavra;
    "data_horario": r'\b(?:0[1-9]|[12]\d|3[01])[/-](?:0[1-9]|1[0-2])[/-](?:19|20)\d{2}\s+(?:[01]\d|2[0-3]):[0-5]\d(?::[0-5]\d)?\b',
}