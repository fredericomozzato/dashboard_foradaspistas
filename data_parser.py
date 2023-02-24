import csv
import locale
from pathlib import Path
from datetime import datetime

from base_relatorio import (gravar_dados_gerais, 
                            gravar_lives, 
                            gravar_cabecalho,
                            gravar_materias)


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
                "views": int(video[3]),
                "tempo_exibicao": float(video[4]),
                "inscritos": int(video[5]),
                "receita": float(video[6])
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
                    "views": int(video[3]),
                    "tempo_exibicao": float(video[4]),
                    "inscritos": int(video[5]),
                    "receita": float(video[6])
                }
            top_materias.append(materia)

    return top_materias[:5]



def gravar_relatorio(totais, lives, materias):
    with open(f"./relatorio[{data_atual.year}_{data_atual.month}].txt", "w") as relatorio:
        relatorio.write(gravar_cabecalho(data_atual))
        relatorio.write(gravar_dados_gerais(totais))
        relatorio.write("Lives do mês\n")
        for live in lives:
            relatorio.write(gravar_lives(live))
        relatorio.write("\n\nTop 5 matérias:\n\n")
        counter = 1
        for materia in materias:
            relatorio.write(f"#{counter} | {gravar_materias(materia)}")
            counter += 1
        

def main():
    pass


if __name__ == "__main__":
    main()
