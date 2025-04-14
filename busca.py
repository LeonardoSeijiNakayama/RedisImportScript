import redis

r = redis.Redis(host='localhost', port=6379, db=0)

print("Registros com 'meio' = Impresso:\n" + "-"*40)

for key in r.scan_iter("acervo:*"):
    data = r.hgetall(key)
    decoded = {k.decode(): v.decode() for k, v in data.items()}
    
    if decoded.get("meio") == "Impresso":
        print(f"🔹 Chave: {key.decode()}")
        print(f"   Indicador 1: {decoded.get('indicador_1')}")
        print(f"   Indicador 2: {decoded.get('indicador_2')}")
        print(f"   Modelo de negócio: {decoded.get('modelo_negocio')}")
        print(f"   Tipo de indicador: {decoded.get('tipo_indicador')}")
        print(f"   Fonte: {decoded.get('fonte')}")
        print(f"   Mês de janeiro: {decoded.get('jan')}")
        print("-" * 40)
