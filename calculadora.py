def calculadora():
    print(" Calculadora Básica ")

   
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira apenas números válidos.")
        return operacao = input("Escolha a operação (+, -, *, /): ")

   
    if operacao == "+":
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif operacao == "-":
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif operacao == "*":
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida. Por favor, use +, -, * ou /.")


calculadora()
