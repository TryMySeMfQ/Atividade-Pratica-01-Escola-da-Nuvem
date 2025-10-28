# ==========================================
# 🧮 ATIVIDADE PRÁTICA 04
# ==========================================

def to_float(s: str) -> float:
    """Converte string para float aceitando vírgula ou ponto."""
    return float(s.replace(",", ".").strip())

# 1) CALCULADORA COM TRATAMENTO DE ERROS (+, -, *, /)
def calculadora():
    print("=== Calculadora ( +  -  *  / ) ===")
    while True:
        try:
            n1 = to_float(input("Digite o primeiro número: "))
        except ValueError:
            print("Erro: entrada inválida para o primeiro número. Tente novamente.")
            continue

        try:
            n2 = to_float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: entrada inválida para o segundo número. Tente novamente.")
            continue

        op = input("Digite a operação (+, -, *, /): ").strip()

        try:
            if op == "+":
                res = n1 + n2
            elif op == "-":
                res = n1 - n2
            elif op == "*":
                res = n1 * n2
            elif op == "/":
                # Pode lançar ZeroDivisionError
                res = n1 / n2
            else:
                raise ValueError("Operação inválida.")
        except ZeroDivisionError:
            print("Erro: divisão por zero. Informe outro segundo número.")
            continue
        except ValueError as e:
            print(f"Erro: {e} Tente novamente.")
            continue

        print(f"Resultado: {res}")
        print("Operação concluída com sucesso. Encerrando a calculadora.")
        break

# 2) REGISTRO DE NOTAS ATÉ 'fim' (0..10) E MÉDIA FINAL
def registrar_notas():
    print("=== Registro de Notas (digite 'fim' para encerrar) ===")
    notas = []
    while True:
        s = input("Nota (0 a 10) ou 'fim': ").strip().lower()
        if s == "fim":
            break
        try:
            n = to_float(s)
            if 0 <= n <= 10:
                notas.append(n)
            else:
                print("Nota inválida (fora do intervalo 0..10). Ignorada.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 0 e 10 ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"Quantidade de notas válidas: {len(notas)}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota válida registrada. Média não pode ser calculada.")

# 3) VERIFICAÇÃO DE SENHA FORTE (>= 8 e contém número) ATÉ VÁLIDA OU 'sair'
def senha_forte():
    print("=== Verificador de Senha Forte ===")
    print("Regras: pelo menos 8 caracteres e pelo menos 1 número.")
    while True:
        s = input("Digite uma senha (ou 'sair' para encerrar): ")
        if s.lower().strip() == "sair":
            print("Encerrando sem validar senha.")
            break

        tem_tamanho = len(s) >= 8
        tem_numero = any(ch.isdigit() for ch in s)

        if tem_tamanho and tem_numero:
            print("Senha forte! ✅")
            break
        else:
            print("Senha fraca. Deve ter pelo menos 8 caracteres e conter ao menos 1 número. Tente novamente.")

# 4) PARES/ÍMPARES ATÉ 'fim' + CONTAGEM FINAL
def pares_impares():
    print("=== Par ou Ímpar (digite 'fim' para encerrar) ===")
    pares = 0
    impares = 0
    while True:
        s = input("Número inteiro ou 'fim': ").strip().lower()
        if s == "fim":
            break
        try:
            n = int(s)
            if n % 2 == 0:
                print(f"{n} é par.")
                pares += 1
            else:
                print(f"{n} é ímpar.")
                impares += 1
        except ValueError:
            print("Erro: isso não é um número inteiro. Tente novamente.")
            continue

    print(f"Quantidade de pares: {pares}")
    print(f"Quantidade de ímpares: {impares}")

# ---------------- MENU ----------------
def menu():
    print("\n=== ATIVIDADE PRÁTICA 04 ===")
    print("1 - Calculadora (+, -, *, /) com tratamento de erros")
    print("2 - Registrar notas até 'fim' e mostrar média")
    print("3 - Verificar senha forte (até válida ou 'sair')")
    print("4 - Par/Ímpar até 'fim' + contagem final")
    print("0 - Sair")

def main():
    while True:
        menu()
        op = input("Escolha: ").strip()
        if op == "1":
            calculadora()
        elif op == "2":
            registrar_notas()
        elif op == "3":
            senha_forte()
        elif op == "4":
            pares_impares()
        elif op == "0":
            print("Encerrando o programa. 👋")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

