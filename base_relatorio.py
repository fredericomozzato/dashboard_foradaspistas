from datetime import datetime

def gravar_cabecalho(data):
    return f'''
Relatório Fora das Pistas | {datetime.strftime(data, "%B %y")}

'''

def gravar_dados_gerais(totais):
    return f''' 
 Dados gerais:
    
    * Views:\t\t{totais['total_views']:,}
    * Novos inscritos:\t{totais['total_novos_inscritos']:,}
    * Horas assistidas:\t{int(totais['total_horas']):,}
    * Receita (R$):\t{int(totais['total_receita']):,}   

    
'''

def gravar_lives(live):
    return f'''
{datetime.strftime(live['data'], '%d/%m')} | {live['titulo']}:\n
      * Views:\t{live['views']:,}
      * Pico:\t345

'''

def gravar_materias(materia):
    return f'''{materia['titulo']}

    * Views: {materia['views']:,}

    
'''