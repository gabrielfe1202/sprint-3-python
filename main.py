import random
from datetime import datetime, timedelta

def gerar_insumos(qtd=1):
    nomes = ["Tubo de ensaio", "Luvas de látex", "Reagente A", "Reagente B", "Seringa"]
    insumos = []
    for i in range(qtd):
        insumo = {
            "codigo": f"Id-{random.randint(100,999)}",
            "nome": random.choice(nomes),
            "quantidade": random.randint(1, 20),
            "validade": datetime.now() + timedelta(days=random.randint(10, 90))
        }
        insumos.append(insumo)
    return insumos

def enfileirar(fila, item):
    fila.append(item)

def desenfileirar(fila):
    if fila:
        return fila.pop(0)

def empilhar(pilha, item):
    pilha.append(item)

def desempilhar(pilha):
    if pilha:
        return pilha.pop()

def busca_sequencial(lista, chave):
    for item in lista:
        if item["nome"].lower() == chave.lower() or item["codigo"] == chave:
            return item
    return None

def busca_binaria(lista, chave):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio]["codigo"] == chave:
            return lista[meio]
        elif lista[meio]["codigo"] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None

def merge_sort(lista, chave="quantidade"):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)

    return merge(esquerda, direita, chave)

def merge(esquerda, direita, chave):
    resultado = []
    while esquerda and direita:
        if esquerda[0][chave] <= direita[0][chave]:
            resultado.append(esquerda.pop(0))
        else:
            resultado.append(direita.pop(0))
    resultado.extend(esquerda or direita)
    return resultado

def quick_sort(lista, chave="quantidade"):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [x for x in lista[1:] if x[chave] <= pivo[chave]]
    maiores = [x for x in lista[1:] if x[chave] > pivo[chave]]
    return quick_sort(menores, chave) + [pivo] + quick_sort(maiores, chave)


fila = []
pilha = []


while True:
    print("\n\n===== MENU =====")
    print("1 - Registrar consumo")
    print("2 - Mostrar consumo")
    print("3 - Mostrar últimos consumos")
    print("4 - Buscar insumo")
    print("5 - Buscar insumo")
    print("6 - Ordenar por quantidade")
    print("7 - Ordenar por validade")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novos = gerar_insumos(1)
        insumo = novos[0]
        enfileirar(fila, insumo)
        empilhar(pilha, insumo)
        print("Consumo registrado:", insumo)

    elif opcao == "2":
        print("\n--- Ordem cronológica ---")
        for i in fila:
            print(i)

    elif opcao == "3":
        print("\n--- Ultimos consumos ---")
        for i in reversed(pilha):
            print(i)

    elif opcao == "4":
        chave = input("Digite o nome ou código do insumo: ")
        resultado = busca_sequencial(fila, chave)
        print("Resultado:", resultado)

    elif opcao == "5":
        chave = input("Digite o código do insumo: ")
        ordenado = sorted(fila, key=lambda x: x["codigo"])
        resultado = busca_binaria(ordenado, chave)
        print("Resultado:", resultado)

    elif opcao == "6":
        print("\n--- Ordenado por quantidade ---")
        ordenado = merge_sort(fila.copy(), chave="quantidade")
        for i in ordenado:
            print(i)

    elif opcao == "7":
        print("\n--- Ordenado por validade ---")
        ordenado = quick_sort(fila.copy(), chave="validade")
        for i in ordenado:
            print(i)

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")

