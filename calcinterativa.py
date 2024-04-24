import formulas

print("Calculadora Cientifica Interativa")
print("Alunos: Jonathan Neves\nRômulo Fonseca\nRodrigo Teixeira")
print("Versão 1.0")
print("")
print("Vamos começar!")
print("Digite um número (ou a palavra 'pi' para o valor de pi): ")
num = input()
if num.lower() == 'pi':
    num = formulas.pi()
else:
    num = float(num)
formulas.menu()
opcao = int(input("Digite a opção desejada: "))
while True:
    match opcao:
        case 1:
            print("Digite o segundo número ou 'pi' para usar o valor de Pi: ")
            input_value = input()
            if input_value.lower() == 'pi':
                num2 = formulas.pi()
            else:
                num2 = float(input_value)
            num = num + num2
            print("Resultado: ", num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))
        case 2:
            print("Digite o segundo número ou 'pi' para usar o valor de Pi: ")
            input_value = input()
            if input_value.lower() == 'pi':
                num2 = formulas.pi()
            else:
                num2 = float(input_value)
            num = num - num2
            print("Resultado: ", num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))
        case 3:
            print("Digite o segundo número ou 'pi' para usar o valor de Pi: ")
            input_value = input()
            if input_value.lower() == 'pi':
                num2 = formulas.pi()
            else:
                num2 = float(input_value)
            num = num * num2
            print("Resultado: ", num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))
        case 4:
            print("Digite o segundo número ou 'pi' para usar o valor de Pi: ")
            input_value = input()
            if input_value.lower() == 'pi':
                num2 = formulas.pi()
            else:
                num2 = float(input_value)
            num = num / num2
            print("Resultado: ", num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))
        case 5:
            print("Digite o segundo número ou 'pi' para usar o valor de Pi: ")
            input_value = input()
            if input_value.lower() == 'pi':
                num2 = formulas.pi()
            else:
                num2 = float(input_value)
            num = num ** num2
            print("Resultado: ", num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))
        case 6:
            num = formulas.senx(num)
            print("Resultado: ", num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))
        case 7:
            num = formulas.cosx(num)
            print("Resultado: ", num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))
        case 8:
            num = formulas.tanx(num)
            print("Resultado: ", num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))
        case 9:
            num = formulas.exponencialx(num)
            print("Resultado: ", num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))
        case 10:
            num = formulas.ln_using_mercator(num)
            print("Resultado: ", num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))
        case 11:
            num = formulas.sqrt_newton(num)
            print("Resultado: ", num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))
        case 12:
            num = formulas.fatorial(num)
            print("Resultado: ", num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))
        case 13:
            num = formulas.log_base10(num)
            print("Resultado: ", num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))
        case 14:
            num = 0
            print("Calculadora resetada")
            print("Resultado: ", num)
            print("Digite um número (ou a palavra 'pi' para o valor de pi): ")
            num = input()
            if num.lower() == 'pi':
                num = formulas.pi()
            else:
                num = float(num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))
        case 15:
            print("Até mais!")
            break
        case _:
            print("Opção inválida")
            print("O seu resultado manteve o valor anterior")
            print("Resultado: ", num)
            formulas.menu()
            opcao = int(input("Digite a opção desejada: "))