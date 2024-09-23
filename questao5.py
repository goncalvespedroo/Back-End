from datetime import datetime, timedelta

def q5_calculo_prazo(data, prazo, tipo):
    """Calcula a data final a partir de uma data inicial e prazo em dias corridos ou úteis."""
    
    data_inicial = datetime.strptime(data, '%d/%m/%Y')
    
    data_atual = data_inicial + timedelta(days=1)
    
    dias_contados = 0
    
    if tipo.upper() == "UTEIS":
        while dias_contados < prazo:
            if data_atual.weekday() < 5:
                dias_contados += 1
            # Avança um dia
            data_atual += timedelta(days=1)
    
    elif tipo.upper() == "CORRIDOS":
        data_atual += timedelta(days=prazo)
    
    else:
        return "Tipo de prazo inválido. Use UTEIS ou CORRIDOS."
    
    return f"Data {data_inicial.strftime('%d/%m/%Y')}, prazo de {prazo} dias {tipo.lower()}, a data final é no dia {data_atual.strftime('%d/%m/%Y')}"

print(q5_calculo_prazo("16/09/2024", 7, "UTEIS"))
print(q5_calculo_prazo("16/09/2024", 7, "CORRIDOS"))
