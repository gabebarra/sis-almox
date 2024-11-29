from datetime import datetime

def formatar_data(data_inicial, data_final):
    inicial_aux = data_inicial.split('-')
    final_aux = data_final.split('-')

    data_inicial = inicial_aux[2] + '/' + inicial_aux[1] + '/' + inicial_aux[0]
    data_final = final_aux[2] + '/' + final_aux[1] + '/' + final_aux[0]
    
    if data_inicial and data_final:
            data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y')
            data_final = datetime.strptime(data_final, '%d/%m/%Y')
    elif data_inicial:
        data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y')
        data_final = data_inicial
    elif data_final:
        data_final = datetime.strptime(data_final, '%d/%m/%Y')
        data_inicial = data_final
    else:
        data_final = data_inicial = datetime.today().strftime('%Y-%m-%d')

    return data_inicial, data_final