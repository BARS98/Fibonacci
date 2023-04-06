primeiro_num = 0
segundo_num = 1
cont = 0

num_escolhido = int(input("Digite um número para descobrir se ele pertence à sequência de Fibonacci\n>>> "))

for n in range(num_escolhido + 1):
    print(primeiro_num)
    soma_num = primeiro_num + segundo_num
    primeiro_num = segundo_num
    cont += 1
    segundo_num = soma_num
    if primeiro_num > num_escolhido:
        print(f"O número {num_escolhido} não pertence a sequência de Fibonacci")
        break
    elif primeiro_num != num_escolhido:
        continue
    else:
        print(primeiro_num)
        print(f"O número {num_escolhido} esta na sequência de Fibonacci na {cont}° colocação")
        break
