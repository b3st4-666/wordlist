def cria_lista_numeros(n_inicial, n_final):

    # Le a quantidade de caracteres dos numeros da lista
    caracteres = 2 #len(str(n_final))

    lista_numeros = [f"{i:0{caracteres}}" for i in range (n_inicial, n_final + 1)]
    return lista_numeros

def salva_lista(lista):

    caminho_arquivo = "wordlist/Listas/lista_numeros.txt"
    # Abre o arquivo e escreve a lista no formato desejado
    with open(caminho_arquivo, "w") as arquivo:
        arquivo.write("\n".join(lista))

def main():
    n_inicial = int(input("Digite o número inicial da lista de números: "))
    n_final = int(input("Digite o número final da lista: "))

    lista_numeros = (cria_lista_numeros(n_inicial, n_final))

    salva_lista(lista_numeros)

main ()
