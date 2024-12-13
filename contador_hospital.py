texto = input("Digite um conjunto de palavras, separadas por vírgula: ")

palavras = texto.split(',')

contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

palavra_mais_frequente = max(contagem_palavras, key=contagem_palavras.get)
maior_quantidade = contagem_palavras[palavra_mais_frequente]

if palavra_mais_frequente == "zero":
    palavra_mais_frequente = 0
    print(palavra_mais_frequente)

else:
    print(maior_quantidade)
