# Programa: Gerador de Wordlist
Criei um programa em Python chamado wordlist.py que combina três listas de arquivos .txt em uma única lista de senhas. As listas são:

1. lista_palavras.txt:

    - Contém palavras, como:
    ```
    abacaxi
    amora
    morango
    ```

2. `lista_numeros.txt`:
    - Contém números, como:
    ```
    01
    02
    03
    ```

3. `lista_caracteres.txt`:
    - Contém caracteres especiais, como:
    ```
    @
    #
    $
    ```

## Como o programa funciona
O programa lê as três listas, combina cada palavra com todos os números e caracteres especiais, e gera uma lista de senhas no seguinte formato:
```
palavra + número + caractere
```

## Exemplo de saída:
Após executar o programa `wordlist.py`, a lista de senhas gerada será:
```
abacaxi01@, abacaxi01#, abacaxi01$, abacaxi02@, abacaxi02#, abacaxi02$, abacaxi03@, abacaxi03#, abacaxi03$, amora01@, amora01#, amora01$, amora02@, amora02#, amora02$, amora03@, amora03#, amora03$, morango01@, morango01#, morango01$, morango02@, morango02#, morango02$, morango03@, morango03#, morango03$
```

## Explicação:
- Cada **palavra** é combinada com todos os **números** e **caracteres especiais**.
- O processo é repetido até que todas as combinações possíveis sejam geradas.

## Resultado
O programa gera todas as combinações possíveis, criando uma wordlist completa para uso em testes de segurança, por exemplo.