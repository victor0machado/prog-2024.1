# Pedidos das ACs

Abaixo estão indicados os pedidos para cada AC do curso. Consulte os prazos em http://estudante.ibmec.br, e as orientações gerais para entrega [aqui](https://victor0machado.github.io/prog/orientacao_entregas.html).

## AC1

### Exercício 1: equações de segundo grau

Elabore um código em Python que resolva uma equação do segundo grau `ax² + bx + c = 0`. O programa deve ler os parâmetros `a`, `b` e `c` da equação e deve calcular as raízes pela fórmula de Bhaskara.

Considere que as raízes dadas pelo usuário são sempre reais, e os valores passados pelo usuário são sempre numéricos.

#### Exemplos

``` cmd
Informe o parâmetro a da equação: 1
Informe o parâmetro b da equação: -6
Informe o parâmetro c da equação: 8
A primeira raiz da equação é 4.0
A segunda raiz da equação é 2.0
```

``` cmd
Informe o parâmetro a da equação: 2
Informe o parâmetro b da equação: 16
Informe o parâmetro c da equação: 3
A primeira raiz da equação é -0.19211344706804567
A segunda raiz da equação é -7.807886552931954
```

### Exercício 2: anos bissextos

Elabore um programa em Python que leia uma variável inteira `ano`. Em seguida, exiba na tela o resultado da expressão lógica que indica se um ano é ou não bissexto. Um ano é bissexto se ele é múltiplo de quatro. No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

O programa deve utilizar **apenas** as funções `print()`, `input()` e `int()`, além dos operadores lógicos `and`, `or` ou `not` e de operadores aritméticos ou de comparação necessários.

#### Exemplos

``` cmd
Informe o ano: 1995
False
```

``` cmd
Informe o ano: 2012
True
```

``` cmd
Informe o ano: 1900
False
```

``` cmd
Informe o ano: 2000
True
```
