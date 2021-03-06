market = {
    '010': 'VISTA',
    '012': 'EXERCÍCIO DE OPÇÕES DE COMPRA',
    '013': 'EXERCÍCIO DE OPÇÕES DE VENDA',
    '017': 'LEILÃO',
    '020': 'FRACIONÁRIO',
    '030': 'TERMO',
    '050': 'FUTURO COM RETENÇÃO DE GANHO',
    '060': 'FUTURO COM MOVIMENTAÇÃO CONTÍNUA',
    '070': 'OPÇÕES DE COMPRA',
    '080': 'OPÇÕES DE VENDA',
}

bdi = {
    '02': 'LOTE PADRÃO',
    '06': 'CONCORDATÁRIAS',
    '10': 'DIREITOS E RECIBOS',
    '12': 'FUNDOS IMOBILIÁRIOS',
    '14': 'CERTIFIC. INVESTIMENTO / DEBÊNTURES / TÍTULOS DIVIDA PÚBLICA',
    '18': 'OBRIGAÇÕES',
    '22': 'BÔNUS (PRIVADOS)',
    '26': 'APÓLICES / BÔNUS / TÍTULOS PÚBLICOS',
    '32': 'EXERCÍCIO DE OPÇÕES DE COMPRA DE ÍNDICE',
    '33': 'EXERCÍCIO DE OPÇÕES DE VENDA DE ÍNDICE',
    '38': 'EXERCÍCIO DE OPÇÕES DE COMPRA',
    '42': 'EXERCÍCIO DE OPÇÕES DE VENDA',
    '46': 'LEILÃO DE TÍTULOS NÃO COTADOS',
    '48': 'LEILÃO DE PRIVATIZAÇÃO',
    '50': 'LEILÃO',
    '51': 'LEILÃO FINOR',
    '52': 'LEILÃO FINAM',
    '53': 'LEILÃO FISET',
    '54': 'LEILÃO DE AÇÕES EM MORA',
    '56': 'VENDAS POR ALVARÁ JUDICIAL',
    '58': 'OUTROS',
    '60': 'PERMUTA POR AÇÕES',
    '61': 'META',
    '62': 'TERMO',
    '66': 'DEBÊNTURES COM DATA DE VENCIMENTO ATÉ 3 ANOS',
    '68': 'DEBÊNTURES COM DATA DE VENCIMENTO MAIOR QUE 3 ANOS',
    '70': 'FUTURO COM MOVIMENTAÇÃO CONTÍNUA',
    '71': 'FUTURO COM RETENÇÃO DE GANHO',
    '74': 'OPÇÕES DE COMPRA DE ÍNDICES',
    '75': 'OPÇÕES DE VENDA DE ÍNDICES',
    '78': 'OPÇÕES DE COMPRA',
    '82': 'OPÇÕES DE VENDA',
    '83': 'DEBÊNTURES E NOTAS PROMISSÓRIAS',
    '96': 'FRACIONÁRIO',
    '99': 'TOTAL GERAL',
}

indopc = {
    '1', ('US$', 'CORREÇÃO PELA TAXA DO DÓLAR'),
    '2', ('TJLP', 'CORREÇÃO PELA TJLP'),
    '3', ('TR', 'CORREÇÃO PELA TR'),
    '4', ('IPCR', 'CORREÇÃO PELO IPCR'),
    '5', ('SWA', 'OPÇÕES DE TROCA - SWOPTIONS'),
    '6', ('ÍNDICES (PONTOS)', 'OPÇÕES REFERENCIADAS EM PONTOS DE ÍNDICE'),
    '7', ('US$ (PROTEGIDAS)', 'CORREÇÃO PELA TAXA DO DÓLAR - OPÇÕES PROTEGIDAS'),
    '8', ('IGPM (PROTEGIDA)', 'CORREÇÃO PELO IGP-M - OPÇÕES PROTEGIDAS'),
    '9', ('URV', 'CORREÇÃO PELA URV'),
}

especi = {
    'ON': 'AÇÕES ORDINÁRIAS NOMINATIVAS',
    'PNA': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE A',
    'PNB': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE B',
    'PNC': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE C',
    'PND': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE D',
    'PNE': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE E',
    'PNF': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE F',
    'PNG': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE G',
    'PNH': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE H',
    'PN': 'AÇÕES PREFERENCIAIS NOMINATIVAS',
    'PNV': 'AÇÕES PREFERENCIAIS NOMINATIVAS COM DIREITO A VOTO',
    'OR': 'AÇÕES ORDINÁRIAS NOMINATIVAS RESGATÁVEIS',
    'PRA': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE A RESGATÁVEIS',
    'PRB': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE B RESGATÁVEIS',
    'PRC': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE C RESGATÁVEIS',
    'PRD': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE D RESGATÁVEIS',
    'PRE': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE E RESGATÁVEIS',
    'PRF': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE F RESGATÁVEIS',
    'PRG': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE G RESGATÁVEIS',
    'PRH': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE H RESGATÁVEIS',
    'PNR': 'AÇÕES PREFERENCIAIS NOMINATIVAS RESGATÁVEIS',
    'PRV': 'AÇÕES PREFERENCIAIS NOMINATIVAS COM DIREITO A VOTO RESG',
    'ON P': 'AÇÕES ORDINÁRIAS NOMINATIVAS COM DIREITOS DIFERENCIADOS',
    'PNA P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE A C/ DIREITOS DIFER',
    'PNB P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE B C/ DIREITOS DIFER',
    'PNC P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE C C/ DIREITOS DIFER',
    'PND P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE D C/ DIREITOS DIFER',
    'PNE P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE E C/ DIREITOS DIFER',
    'PNF P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE F C/ DIREITOS DIFER',
    'PNG P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE G C/ DIREITOS DIFER',
    'PNH P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE H C/ DIREITOS DIFER',
    'PN P': 'AÇÕES PREFERENCIAIS NOMINATIVAS COM DIREITOS DIFERENCIADOS',
    'PNV P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE V C/ DIREITOS DIFER',
    'ON P': 'AÇÕES ORDINÁRIAS NOMINATIVAS COM DIREITOS DIFERENCIADOS',
    'BDR': 'BDR',
    'UNT': 'CERTIFICADO DE DEPOSITO DE AÇÕES - MISCELÂNEA',
    'CDA': 'CERTIFICADO DE DEPOSITO DE AÇÕES ORDINÁRIAS',
    'CPA': 'CERTIFICADOS DE POTENCIAL ADICIONAL DE CONSTRUÇÃO E OPERAÇÃO',
    'RON': 'CESTA DE AÇÕES ORDINÁRIAS NOMINATIVAS',
    'R': 'CESTA DE AÇÕES NOMINATIVAS',
    'CI': 'FUNDO DE INVESTIMENTO',
    'DIR': 'DIREITOS DE SUBSCRIÇÃO MISCELÂNEA (BÔNUS, DEBÊNTURES, ETC)',
    'DIR ORD': 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES ORDINÁRIAS',
    'DIR P/A': 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE A',
    'DIR P/B': 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE B',
    'DIR P/C': 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE C',
    'DIR P/D': 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE D',
    'DIR P/E': 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE E',
    'DIR P/F': 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE F',
    'DIR P/G': 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE G',
    'DIR P/H': 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE H',
    'DIR PRE': 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS',
    'PRA REC': 'RECIBO DE SUBSCRIÇÃO EM AÇÕES RESGATÁVEIS PREF. CLASSE A',
    'PRB REC': 'RECIBO DE SUBSCRIÇÃO EM AÇÕES RESGATÁVEIS PREF. CLASSE B',
    'PRC REC': 'RECIBO DE SUBSCRIÇÃO EM AÇÕES RESGATÁVEIS PREF. CLASSE C',
    'M1 REC': 'RECIBO DE SUBSCRIÇÃO DE MISCELÂNEAS',
    'DIR PRA': 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES RESGATÁVEIS PREF. CLASSE A',
    'DIR PRB': 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES RESGATÁVEIS PREF. CLASSE B',
    'DIR PRC': 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES RESGATÁVEIS PREF. CLASSE C',
    'LFT': 'LETRA FINANCEIRA DO TESOURO',
    'BNS ORD': 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES ORDINÁRIAS',
    'BNS P/A': 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE A',
    'BNS P/B': 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE B',
    'BNS P/C': 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE C',
    'BNS P/D': 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE D',
    'BNS P/E': 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE E',
    'BNS P/F': 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE F',
    'BNS P/G': 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE G',
    'BNS P/H': 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE H',
    'BNS PRE': 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS',
    'PCD': 'POSIÇÃO CONSOLIDADA DA DIVIDA',
    'UP': 'PRECATÓRIO',
    'REC': 'RECIBO DE SUBSCRIÇÃO MISCELÂNEA',
    'ON REC': 'RECIBO DE SUBSCRIÇÃO EM AÇÕES ORDINÁRIAS',
    'PNA REC': 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE A',
    'PNB REC': 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE B',
    'PNC REC': 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE C',
    'PND REC': 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE D',
    'PNE REC': 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE E',
    'PNF REC': 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE F',
    'PNG REC': 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE G',
    'PNH REC': 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE H',
    'PN REC': 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS',
    'PNV REC': 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS C/ DIREITO VOTO',
    'UNT': 'UNITS',
    'WRT': 'WARRANTS DE DEBÊNTURES',
    'OR P': 'AÇÕES ORDINÁRIAS NOMINATIVAS RESGATÁVEIS C/ DIREITOS DIF',
    'PRA P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE A RESG. C/ DIR.DIF',
    'PRB P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE B RESG. C/ DIR.DIF',
    'PRC P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE C RESG. C/ DIR.DIF',
    'PRD P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE D RESG. C/ DIR.DIF',
    'PRE P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE E RESG. C/ DIR.DIF',
    'PRF P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE F RESG. C/ DIR.DIF',
    'PRG P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE G RESG. C/ DIR.DIF',
    'PRH P': 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE H RESG. C/ DIR.DIF',
    'PR P': 'AÇÕES PREFERENCIAIS NOMINATIVAS RESGATÁVEIS C/ DIREITOS DIF',
    'PRV P': 'AÇÕES PREFERENCIAIS NOMINATIVAS RESG. C/ DIR.DIF. E DIR.VOTO',
}
