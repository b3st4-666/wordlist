# Importar os pacotes necessários
import os

# Função para ler uma lista de um arquivo .txt
def ler_lista(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        return [linha.strip() for linha in arquivo]

# Função que junta as listas
def junta_palavras(lista_palavras, lista_numeros, lista_caracteres):
    resultado = []
    for item_1 in lista_palavras:
        for item_2 in lista_numeros:
            for item_3 in lista_caracteres:

                resultado.append(item_1+item_2+item_3)

    return resultado

# Salvar arquivo
def salva_lista(lista):
    caminho_arquivo = "wordlist/Resultado/lista_completa.txt"

    # Abre o arquivo e escreve a lista
    with open(caminho_arquivo, "w") as arquivo:
        arquivo.write("\n".join(lista))

def main():

    # Caminho para a pasta Listas
    caminho_listas = os.path.expanduser("wordlist/Listas")

    # Lendo listas
    lista_palavras = ler_lista(os.path.join(caminho_listas, "lista_palavras.txt"))
    lista_numeros = ler_lista(os.path.join(caminho_listas, "lista_numeros.txt"))
    lista_caracteres = ler_lista(os.path.join(caminho_listas, "lista_caracteres.txt"))

    # Unindo as listas
    lista_juntada = junta_palavras(lista_palavras, lista_numeros, lista_caracteres)

    # Salvar arquivo
    salva_lista(lista_juntada)
    
main()