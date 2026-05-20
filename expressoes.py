#Padrões em Regex para cada tipo de dado buscado
expressoes_arquivo = {
    "chat": r'^\[\d{2}/\d{2}/\d{4}\s\d{2}:\d{2}:\d{2}\]\s.+:',
    "padrao_log": (
        r'^\d{2}/\d{2}/\d{4}\s'
        r'\d{2}:\d{2}:\d{2}\s'
        r'\[(INFO|DEBUG|ERROR|WARN)\].*'
        r'(services=|service=|module=|user=|session=|seq=)'
    )
}

expressoes_validadoras = {
    #Explicação: \b marca o limite de uma palavra;
    #Explicação: [a-zA-Z0-9._%+-]+ Aceita letras, números e símbolos comuns antes do @;
    #Explicação: @ caractere obrigatório do e-mail;
    #Explicação: [a-zA-Z0-9.-]+ Domínio (gmail, outlook, institucional e etc), aceita letras, números, ponto e hífen;
    #Explicação: \. Ponto antes da extensão do domínio;
    #Explicação: [A-Za-z]{2,} Extensão do domínio (com, org, br) com critério mínimo de 2 letras;
    #Explicação: \b Fecha o limite da palavra;
    #"email": r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}\b',
    "email" : r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$',

    #Explicação: \b marca o limite de uma palavra;
    #Explicação: (?:\+55\s?)? Código do Brasil opcional, com espaço opcional;
    #Explicação: (?:\(?\d{2}\)?\s?)? DDD opcional, podendo vir com ou sem parênteses e com espaço opcional;
    #Explicação: (?:9?\d{4}) Primeiro bloco do telefone, com o 9 opcional e mais 4 dígitos;
    #Explicação: [-\s]? Aceita hífen ou espaço opcional entre os blocos;
    #Explicação: \d{4} Últimos 4 dígitos do telefone;
    #Explicação: \b Fecha o limite da palavra;
    #"telefone": r'\b(?:\+55\s?)?(?:\(?\d{2}\)?\s?)?(?:9?\d{4})[-\s]?\d{4}\b',
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
    #"cpf": r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b|\b\d{11}\b',
    "cpf" :r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',

    #Explicação: \b marca o limite de uma palavra;
    #Explicação: (?:0[1-9]|[12]\d|3[01]) Dia válido, de 01 a 31;
    #Explicação: [/-] Aceita barra ou hífen como separador;
    #Explicação: (?:0[1-9]|1[0-2]) Mês válido, de 01 a 12;
    #Explicação: [/-] Aceita barra ou hífen novamente;
    #Explicação: (?:19|20)\d{2} Ano com 4 dígitos, aceitando 1900 até 2099;
    #Explicação: \b Fecha o limite da palavra;
    "data": r'\b(?:0[1-9]|[12]\d|3[01])[/-](?:0[1-9]|1[0-2])[/-](?:19|20)\d{2}\b',

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
    
    #Explicação: \b marca o limite de uma palavra;
    #Explicação: https?:// Aceita http:// ou https://;
    #Explicação: [\w\-._~:/?#\[\]@!$&\'"()*+,;=%]+ Conjunto de caracteres comuns em URLs;
    #Explicação: | Ou, permitindo duas formas de URL;
    #Explicação: \bwww\. Captura URLs que começam com www.;
    #Explicação: \b Fecha o limite da palavra;
    #"url": r'\bhttps?://[\w\-._~:/?#\[\]@!$&\'"()*+,;=%]+\b|\bwww\.[\w\-._~:/?#\[\]@!$&\'"()*+,;=%]+\b',
    "url" : r'^https?://[a-zA-Z0-9\-._~:/?#\[\]@!$&\'()*+,;=%]+\.[a-zA-Z]{2,}',

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
}

expressoes_permissivas = {
    # URL válida: começa com http:// ou https:// e possui um TLD reconhecível (2+ letras após último ponto)
    # Justificativa: "http://" sozinho ou sem TLD não é endereço acessível
    "url" : r'\bhttps?://\S+|\bwww\.\S+',
    
    # CPF bem formatado: exatamente no padrão 000.000.000-00
    # Justificativa: qualquer outra forma (só dígitos, separadores errados) é mal formatada
    "cpf" : r'\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b|\b\d{11}\b',

    # Telefone válido: DDD com primeiro dígito entre 1–9 (sem 00), seguido de 8 ou 9 dígitos
    # Justificativa: DDD brasileiro começa em 11; números com menos de 8 dígitos são inválidos
    "telefone" : r'(?<!\d)(?:\+?55\s?)?(?:\(?\d{2}\)?\s?)?\d{4,5}[-\s]?\d{4}\b',

    # E-mail válido: deve ter usuário + @ + domínio + ponto + extensão de 2+ letras
    # Justificativa: descarta casos como "usuario@", "@dominio", "usuario@dominio" sem TLD
    "email" : r'[\w._%+\-]+@[\w.\-]+(?:\.[a-zA-Z]+)?',
}