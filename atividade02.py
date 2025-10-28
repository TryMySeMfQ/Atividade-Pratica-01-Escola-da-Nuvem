# ==========================================
# 🧮 ATIVIDADE PRÁTICA 02
# ==========================================

# ----- 1. Conversor de Moeda -----
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print("=== Conversor de Moeda ===")
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Em dólares: US$ {valor_dolar:.2f}")
print(f"Em euros: € {valor_euro:.2f}")
print()

# ----- 2. Calculadora de Desconto -----
produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

print("=== Calculadora de Desconto ===")
print("Produto:", produto)
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto_percentual}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
print()

# ----- 3. Calculadora de Média Escolar -----
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print("=== Calculadora de Média Escolar ===")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Média final: {media:.2f}")
print()

# ----- 4. Calculadora de Consumo de Combustível -----
distancia = 300
combustivel_gasto = 25

consumo_medio = distancia / combustivel_gasto

print("=== Consumo de Combustível ===")
print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
print()

# ----- 5. Calculadora de Soma com Entrada do Usuário -----
print("=== Calculadora de Soma ===")
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

X = A + B
print("X =", X)
print()

# ----- 6. Calculadora de Salário por Horas Trabalhadas -----
print("=== Cálculo de Salário ===")
numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite as horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor recebido por hora: "))

salario = horas_trabalhadas * valor_por_hora

print(f"NÚMERO = {numero_funcionario}")
print(f"SALÁRIO = R$ {salario:.2f}")
