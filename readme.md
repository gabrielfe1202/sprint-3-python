# Sistema de Controle de Consumo de Insumos

Este projeto simula o controle de insumos em unidades de diagnóstico


---

## Integrantes do grupo

- Gabriel Ferreira Flora Carvalheiro - RM 556476
- Herbert de Sousa Vilela  - RM 555701
- Felipe Soares Xavier - RM 556931

---

## Funcionalidades
- Registrar consumo de insumos
- Listar insumos em ordem cronológica
- Listar últimos consumos
- Buscar insumos por nome ou código
- Ordenar insumos por quantidade ou validade
- Simular inserções e consultas em tempo real

---

## Estruturas de Dados Utilizadas

### 1. **Fila**
- **Uso no sistema:** Armazena os insumos na ordem em que foram consumidos, permitindo listagem cronológica.

### 2. **Pilha**
- **Uso no sistema:** Mantém o histórico de consumo de forma que seja possível visualizar os últimos insumos utilizados

## Algoritmos

### 3. **Busca Sequencial**
- **Uso no sistema:** Permite encontrar um insumo pelo nome ou pelo código dentro da lista de consumos.

### 4. **Busca Binária**
- **Uso no sistema:** Busca insumos pelo código, mas exige que a lista esteja ordenada. Sendo muito mais rápida que a busca sequencial em listas grandes, pois divide o espaço de busca pela metade a cada iteração.

### 5. **Merge Sort**
- **Uso no sistema:** Ordena os insumos pelo campo quantidade. Algoritmo com complexidade O(n log n).

### 6. **Quick Sort**
- **Uso no sistema:** Ordena os insumos pela data de validade. Algoritmo com complexidade O(n²).

### 7. **Recursão Simples**
- **Uso no sistema:** Calcula o custo mínimo de reabastecimento testando todas as combinações possíveis de pedidos e estoques. Apesar de funcional, tem alto custo computacional por recalcular subproblemas repetidos.

### 8. **Programação Dinâmica**
#### 8.1 **Função Recursiva **
- **Uso no sistema:**  Testa todas as combinações possíveis de pedidos e estoques para encontrar o custo mínimo.  

#### 8.2 **Função com Memoização**
- **Uso no sistema:** Evita recomputar subproblemas já resolvidos, reduzindo o número de chamadas recursivas e aumentando a eficiência.  

#### 8.3 **Função Iterativa** 
- **Uso no sistema:**  Parte do caso base (último dia) e avança de forma crescente até o primeiro dia, acumulando os menores custos possíveis.  


