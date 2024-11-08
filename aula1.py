n= int(input('|Digite o tamanho da matriz:'))
matriz = []
for i in range(n):
    linha=[]
    for j in range(n):
        valor = int(input(f'Digite o valor para posição[{i}][{j}]:'))
        linha.append(valor)
    matriz.append(linha)
for linha in matriz:
    print(linha)
for i in range(n):
    print(matriz[i][i])