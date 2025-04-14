import csv
import redis


r = redis.Redis(host='localhost', port=6379, db=0) 


csv_file_path = "acervo_da_biblioteca_2021.csv"

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    
    for i, row in enumerate(reader):
        key = f"acervo:{i+1}"

        data = {
            "indicador_1": row["Indicador 1"],
            "indicador_2": row["Indicador 2"],
            "meio": row["Meio"],
            "modelo_negocio": row["Modelo de negócio"],
            "fonte": row["Fonte"],
            "tipo_indicador": row["Tipo de Indicador"],
            "jan": row["Jan"],
            "fev": row["Fev"],
            "mar": row["Mar"],
            "abr": row["Abr"],
            "mai": row["Mai"],
            "jun": row["Jun"],
            "jul": row["Jul"],
            "ago": row["Ago"],
            "set": row["Set"],
            "out": row["Out"],
            "nov": row["Nov"],
            "dez": row["Dez"]
        }

        
        data = {k: v for k, v in data.items() if v.strip()}
        
        r.hset(key, mapping=data)

print("Importação concluída com sucesso!")

print(r.hgetall("acervo:1"))
