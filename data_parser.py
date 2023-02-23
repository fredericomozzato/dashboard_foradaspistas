import csv
import locale
from pathlib import Path
from datetime import datetime

data_atual = datetime.today()


def read_csv(filename):
    foo = []
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            foo.append(row)
    return foo


def get_totals(list):
    row = list[1]
    totais = {
        "total_views": int(row[3]),
        "total_horas": float(row[4]),
        "total_novos_inscritos": int(row[5]),
        "total_receita": float(row[6])
    }
    return totais
    


def parse_data(tabela):
    clean_list = [] 
    for row in tabela[2:]:
        select = []
        select.append(row[0])
        select.append(row[1])
        select.append(date_convert(row[2]))
        select.append(row[3])
        select.append(row[4])
        select.append(row[5])
        select.append(row[6])
        clean_list.append(select)

    return(clean_list)


def date_convert(date):
    format = "%b %d, %Y"
    return(datetime.strptime(date, format))


def get_lives(tabela):
    '''
    No momento esta função usa data automática para selecionar as lives.
    No futuro é possível usar uma variável para definir manualmente.
    '''
    lives = []
    for video in tabela:
        if video[1].startswith("LIVE") and video[2].month == data_atual.month and video[2].year == data_atual.year:
            live = {
                "id": video[0],
                "titulo": video[1],
                "data": video[2],
                "views": video[3],
                "tempo_exibicao": video[4],
                "inscritos": video[5],
                "receita": video[6]
            }
            lives.append(live)
        else:
            continue
    return lives


def get_top_materias(tabela):
    top_materias = []

    for video in tabela:
        if not video[1].startswith("LIVE"):
            materia = {
                    "id": video[0],
                    "titulo": video[1],
                    "data": video[2],
                    "views": video[3],
                    "tempo_exibicao": video[4],
                    "inscritos": video[5],
                    "receita": video[6]
                }
            top_materias.append(materia)

    return top_materias[:5]


def exportar_dados(totais, lives, materias):
    with open(f"./relatório[{data_atual.year}_{data_atual.month}].txt", "w") as relatorio:
        relatorio.write(f'''

Relatório Fora das Pistas - {datetime.strftime(data_atual, '%B/%y')}

Dados gerais:
    
    - Total de views:\t\t{totais['total_views']:,}
    - Total novos inscritos:\t{totais['total_novos_inscritos']:,}
    - Total horas assistidas:\t{int(totais['total_horas']):,}
    - Total de receita (R$):\t{int(totais['total_receita']):,}
    

    
''')

def main():
    pass


if __name__ == "__main__":
    main()




