# ==========================================
# 🧮 ATIVIDADE PRÁTICA 03 
# ==========================================

# Dica: você pode usar vírgula ou ponto em números decimais.
def to_float(txt):
    return float(txt.replace(",", ".").strip())

# 1) Área da circunferência (A=π*r^2) com 4 casas decimais — saída: A=xxxx.xxxx
def exercicio1():
    PI = 3.14159265
    raio = to_float(input())
    area = PI * (raio ** 2)
    print(f"A={area:.4f}")

# 2) Classificador de Idade
def exercicio2():
    idade = int(input("Digite a idade: ").strip())
    if 0 <= idade <= 12:
        print("Criança")
    elif 13 <= idade <= 17:
        print("Adolescente")
    elif 18 <= idade <= 59:
        print("Adulto")
    else:
        print("Idoso")

# 3) Calculadora de IMC
def exercicio3():
    peso = to_float(input("Peso (kg): "))
    altura = to_float(input("Altura (m): "))
    imc = peso / (altura ** 2)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"
    print(f"IMC: {imc:.2f} — {classificacao}")

# 4) Conversor de Temperatura (C, F, K)
def exercicio4():
    valor = to_float(input("Temperatura: "))
    de = input("Unidade de origem (C/F/K): ").strip().upper()
    para = input("Converter para (C/F/K): ").strip().upper()

    # Converte de origem para Celsius
    if de == "C":
        c = valor
    elif de == "F":
        c = (valor - 32) * 5/9
    elif de == "K":
        c = valor - 273.15
    else:
        print("Unidade de origem inválida.")
        return

    # Converte de Celsius para destino
    if para == "C":
        res = c
    elif para == "F":
        res = c * 9/5 + 32
    elif para == "K":
        res = c + 273.15
    else:
        print("Unidade de destino inválida.")
        return

    print(f"Resultado: {res:.2f} {para}")

# 5) Verificador de Ano Bissexto
def exercicio5():
    ano = int(input("Ano: ").strip())
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    print("Bissexto" if bissexto else "Não bissexto")

# 6) Calculadora de Comissão (15%)
# Saída padrão: TOTAL = R$ xx.yy
def exercicio6():
    nome = input("Nome do vendedor: ").strip()
    salario_fixo = to_float(input("Salário fixo: R$ "))
    vendas = to_float(input("Total de vendas no mês: R$ "))
    total = salario_fixo + (vendas * 0.15)
    print(f"TOTAL = R$ {total:.2f}")

# 7) Calculadora da Média (pesos 2,3,4,1) + exame (saídas com 1 casa decimal)
def exercicio7():
    # Entrada: quatro números de ponto flutuante (uma casa decimal)
    N1 = to_float(input())
    N2 = to_float(input())
    N3 = to_float(input())
    N4 = to_float(input())

    media = (2*N1 + 3*N2 + 4*N3 + 1*N4) / 10
    print(f"Media: {media:.1f}")

    if media >= 7.0:
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        nota_exame = to_float(input())
        print(f"Nota do exame: {nota_exame:.1f}")
        media_final = (media + nota_exame) / 2
        if media_final >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print(f"Media final: {media_final:.1f}")

def menu():
    print("\n=== ATIVIDADE PRÁTICA 03 ===")
    print("1 - Área da circunferência (saída: A=xxxx.xxxx)")
    print("2 - Classificador de Idade")
    print("3 - Calculadora de IMC")
    print("4 - Conversor de Temperatura (C/F/K)")
    print("5 - Verificador de Ano Bissexto")
    print("6 - Calculadora de Comissão (TOTAL = R$ xx.yy)")
    print("7 - Calculadora da Média (pesos 2,3,4,1)")
    print("0 - Sair")

def main():
    while True:
        menu()
        op = input("Escolha: ").strip()
        if op == "1":
            exercicio1()
        elif op == "2":
            exercicio2()
        elif op == "3":
            exercicio3()
        elif op == "4":
            exercicio4()
        elif op == "5":
            exercicio5()
        elif op == "6":
            exercicio6()
        elif op == "7":
            exercicio7()
        elif op == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

