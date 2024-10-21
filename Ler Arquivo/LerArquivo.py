def lerArquivo(Nome_Arquivo):
    for uma_linha in open(Nome_Arquivo, 'r'):
        yield uma_linha.rstrip()

arquivo = (input('Digite o nome do Arquivo:'))
for linha in lerArquivo(arquivo):
    print(linha)
print('/fim do programa')

