print ("---------CADASTRO PRODUTO ----------")
codigo = input("Digite o código: ")
nome = input("Digite o nome: ")
strQuantidade = input("Digite a quantidade: ")
strValor = input("Digite o valor: ")

valor = int (strValor)
quantidade = int (strQuantidade)


print ("---------CARRINHO----------")
print ("Você está comprando o produto: ", nome)
print ("Código: ", codigo)
print ("Valor por item: ", valor)
print ("Quantidade desejada: ", quantidade)
print ("Totalizando: ", quantidade * valor, "$ reais.")
