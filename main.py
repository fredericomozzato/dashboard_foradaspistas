from pathlib import Path
import sqlite3

from data_parser import (parse_data, 
                         get_totals, 
                         read_csv, 
                         get_lives, 
                         get_top_materias,
                         exportar_dados)


#TODO use the working directory as the path
PATH = Path("downloads/Conteúdo 2023-01-26_2023-02-23 Fora das Pistas")
FILENAME = Path("Dados da tabela.csv")
DATABASE = "./database/fdp_database.db"

con = sqlite3.connect(DATABASE)
cur = con.cursor()


def main():
    tabela_raw = read_csv(PATH / FILENAME)
    
    totais = get_totals(tabela_raw)
    tabela_clean = parse_data(tabela_raw)
    lives = get_lives(tabela_clean)
    materias = get_top_materias(tabela_clean)

    exportar_dados(totais, lives, materias)

    # print(totais)
    # print(lives)
    # print(materias)



    
    
    


if __name__ == "__main__":
    main()