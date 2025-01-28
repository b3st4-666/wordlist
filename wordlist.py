# Importar os pacotes nescessario
import os

# Função para ler uma lista de um arquivo .txt
def ler_lista(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        return [linha.strip() for linha in arquivo]

# Caminho para a pasta Listas
caminho_listas = os.path.join("~/VScode/wordlist/Listas")

# Lendo as listas dos arquivos
lista_palavras = ler_lista(os.path.join(caminho_listas, "lista_palavras.txt"))
lista_numeros = ler_lista(os.path.join(caminho_listas, "lista_numeros.txt"))
lista_caracteres = ler_lista(os.path.join(caminho_listas, "lista_caracteres"))
    
print(lista_palavras)
print(lista_numeros)
print(lista_caracteres)
