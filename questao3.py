import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def q3_tratar_datas(data):
    """Tratar e converter datas para o formato americano AAAA-MM-DD."""
    formatos = [
        '%d/%m/%Y',            # Ex: '30/11/2022'
        '%d %b %Y',            # Ex: '01 dez 2022'
        '%d de %B de %Y',      # Ex: '31 de dezembro de 2022'
        '%d de %B de %Y',      # Ex: '1 de dezembro de 2022'
    ]
    
    for formato in formatos:
        try:
            data_formatada = datetime.strptime(data, formato)
            return data_formatada.strftime('%Y-%m-%d')
        except ValueError:
            continue
    return "Formato de data não reconhecido."

DATAS_PARA_TRATAR = [
    '30/11/2022',
    '01 dez 2022', 
    '25/12/2022', 
    '31 de dezembro de 2022'
]

for data in DATAS_PARA_TRATAR:
    print(q3_tratar_datas(data))
