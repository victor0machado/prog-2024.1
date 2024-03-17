# Pedidos das ACs

Abaixo estão indicados os pedidos para cada AC do curso. Consulte os prazos em http://estudante.ibmec.br, e as orientações gerais para entrega [aqui](https://victor0machado.github.io/prog/orientacao_entregas.html).

* [AC1](#ac1)
* [AC2](#ac2)
* [AC3](#ac3)
* [AC4](#ac4)
* [AC5](#ac5)
* [AC6](#ac6)

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

## Pedido AC2

### Exercício 1: revisite a AC1

Desenvolva duas funções em Python:

* `eq_seg_grau(a, b, c)`, que recebe três valores reais e retorna as raízes de uma equação de segundo grau no formato `ax² + bx + c = 0`, supondo as raízes sempre reais;
* `bissexto(ano)`, que recebe um valor inteiro e retorna um valor booleano, informando se o ano é bissexto ou não.

### Exercício 2: salário

Desenvolva uma função em Python cujo nome é `calcula_salario`. Essa função recebe dois parâmetros posicionais reais, `valor_hora` e `num_horas`, que correspondem ao valor do salário por hora e o número de horas trabalhadas no mês, respectivamente. Além disso, a função tem um parâmetro-chave `irpf`, que calcula o imposto de renda a ser deduzido, cujo valor padrão é `0.275`. A função retorna o salário líquido de um funcionário, calculado como o produto do valor por hora pelo número de horas, reduzido o percentual do imposto de renda dado.

## AC3

### Exercício 1: triângulos

Desenvolva uma função `determina_tipo_triangulo` que recebe três lados de um triângulo e retorna uma string, `"Escaleno"`, `"Isósceles"` ou `"Equilátero"`, conforme o tipo do triângulo. A função deve retornar `"Não é um triângulo"` se os três lados não formarem um triângulo. Use a função abaixo como teste:

``` python
def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo
```

### Exercício 2: dia da semana

Desenvolva uma função `dia_semana` que recebe um número inteiro e retorna uma string indicando o dia da semana equivalente, considerando que o dia da semana igual a 1 é o domingo, 2 é segunda-feira, etc. A função deve retornar uma string vazia caso o número seja inválido. Use a função abaixo como teste:

``` python
def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia
```

### Exercício 3: calculadora simples

Desenvolva funções de operações aritméticas `soma`, `subtracao`, `multiplicacao` e `divisao`, que recebem dois números cada uma e retornam o resultado da operação indicada. Em seguida, crie uma função que elabora uma interface por linha de comando (CLI), que lê dois números e uma operação e exibe na tela o valor do resultado, ou exibe "operação inválida" se o usuário inserir uma mensagem diferente das quatro operações.

#### Exemplos

```
Informe um número: 5.5
Informe outro número: 10
Informe a operação: soma
Resultado: 15.5
```

```
Informe um número: 5.5
Informe outro número: 10
Informe a operação: multiplicação
Resultado: 55.0
```

```
Informe um número: 5.5
Informe outro número: 10
Informe a operação: abcd
operação inválida
```

## AC4

Desenvolva uma versão inicial de CLI (_command-line interface_) para analisar se um aluno foi ou não aprovado em uma disciplina. A aplicação deve atender aos seguintes requisitos:

* A CLI deve perguntar ao usuário o seu nome. Caso a resposta do usuário seja um texto vazio, o programa deve ser encerrado;
* Em seguida, o programa deve calcular a média do usuário. Para isso, o programa deve ler as notas de AP1, AP2, AS e AC. Em seguida, deve exibir na tela a média final do aluno. Considere que a média é calculada como `(AP1 + AP2) * 0.4 + AC * 0.2`, sendo que a AS pode substituir a AP1 ou a AP2 (a menor dentre as duas);
* Por fim, a aplicação deve exibir na tela se o aluno foi aprovado ou reprovado, baseado na sua média. A média para aprovação é 7.0.

Organize o seu código em funções com responsabilidades distintas (uma para o cálculo de nota, uma para exibição de informações, uma para leitura de dados, etc.). Caso as notas passadas sejam inválidas (menores que 0 ou maiores que 10), o programa não deve calcular nada e deve ser encerrado.

## AC5

Pesquise sobre o módulo `random`, em particular sobre a função `randint()` ([veja aqui a documentação oficial](https://docs.python.org/3/library/random.html#random.randint)). Entendendo como essa função é utilizada, elabore um jogo por CLI e que você controla um aventureiro e está lutando contra um monstro. Considere os seguintes requisitos:

* O aventureiro possui uma vida inicial igual a 100, seu ataque é um valor aleatório entre 10 e 20, e sua defesa é um valor aleatório entre 1 e 5;
* O monstro possui uma vida aleatória entre 60 e 80, seu ataque é um valor aleatório entre 20 e 30, e não possui defesa;
* Após a definição dos atributos do aventureiro e do monstro, o programa deve exibir os atributos iniciais e em seguida rodar um loop até que a vida de um dos dois fique igual ou abaixo de zero;
* No loop, considere as seguintes ações:
  * O programa escreve o número da rodada do combate;
  * O aventureiro ataca o monstro, reduzindo da vida do monstro um valor aleatório entre 1 e o ataque do aventureiro;
  * Se a vida do monstro ficar igual ou abaixo de zero, o programa deve escrever na tela que o monstro morreu e encerrar o loop;
  * Em seguida, o monstro ataca o aventureiro, reduzindo da vida deste um valor aleatório entre 1 e o ataque do monstro, menos a defesa do aventureiro;
  * Se a vida do aventureiro ficar igual ou abaixo de zero, o programa deve escrever na tela que o aventureiro morreu e encerrar o loop;
  * Por fim, o programa deve escrever os atributos do aventureiro e do monstro.

O programa não deve possuir inputs do usuário, ele apenas deve exibir as informações. Faça o exercício em uma única função, `main()`.

### Exemplos

```
Aventureiro: vida 100 - att 20 - def 1
Monstro: vida 77 - att 24
Rodada 1
Aventureiro: vida 81 - att 20 - def 1
Monstro: vida 72 - att 24
Rodada 2
Aventureiro: vida 71 - att 20 - def 1
Monstro: vida 70 - att 24
Rodada 3
Aventureiro: vida 67 - att 20 - def 1
Monstro: vida 61 - att 24
Rodada 4
Aventureiro: vida 66 - att 20 - def 1
Monstro: vida 44 - att 24
Rodada 5
Aventureiro: vida 50 - att 20 - def 1
Monstro: vida 42 - att 24
Rodada 6
Aventureiro: vida 43 - att 20 - def 1
Monstro: vida 29 - att 24
Rodada 7
Aventureiro: vida 27 - att 20 - def 1
Monstro: vida 15 - att 24
Rodada 8
Aventureiro: vida 25 - att 20 - def 1
Monstro: vida 10 - att 24
Rodada 9
O monstro morreu!
```

```
Aventureiro: vida 100 - att 20 - def 1
Monstro: vida 79 - att 22
Rodada 1
Aventureiro: vida 87 - att 20 - def 1
Monstro: vida 73 - att 22
Rodada 2
Aventureiro: vida 76 - att 20 - def 1
Monstro: vida 64 - att 22
Rodada 3
Aventureiro: vida 56 - att 20 - def 1
Monstro: vida 54 - att 22
Rodada 4
Aventureiro: vida 49 - att 20 - def 1
Monstro: vida 51 - att 22
Rodada 5
Aventureiro: vida 43 - att 20 - def 1
Monstro: vida 31 - att 22
Rodada 6
Aventureiro: vida 39 - att 20 - def 1
Monstro: vida 28 - att 22
Rodada 7
Aventureiro: vida 36 - att 20 - def 1
Monstro: vida 23 - att 22
Rodada 8
Aventureiro: vida 34 - att 20 - def 1
Monstro: vida 4 - att 22
Rodada 9
O monstro morreu!
```

```
Aventureiro: vida 100 - att 14 - def 1
Monstro: vida 75 - att 24
Rodada 1
Aventureiro: vida 88 - att 14 - def 1
Monstro: vida 71 - att 24
Rodada 2
Aventureiro: vida 66 - att 14 - def 1
Monstro: vida 58 - att 24
Rodada 3
Aventureiro: vida 54 - att 14 - def 1
Monstro: vida 55 - att 24
Rodada 4
Aventureiro: vida 35 - att 14 - def 1
Monstro: vida 52 - att 24
Rodada 5
Aventureiro: vida 22 - att 14 - def 1
Monstro: vida 44 - att 24
Rodada 6
Aventureiro: vida 20 - att 14 - def 1
Monstro: vida 39 - att 24
Rodada 7
Aventureiro: vida 2 - att 14 - def 1
Monstro: vida 25 - att 24
Rodada 8
Você morreu!
```

```
Aventureiro: vida 100 - att 20 - def 1
Monstro: vida 68 - att 23
Rodada 1
Aventureiro: vida 80 - att 20 - def 1
Monstro: vida 53 - att 23
Rodada 2
Aventureiro: vida 70 - att 20 - def 1
Monstro: vida 34 - att 23
Rodada 3
Aventureiro: vida 61 - att 20 - def 1
Monstro: vida 29 - att 23
Rodada 4
Aventureiro: vida 42 - att 20 - def 1
Monstro: vida 17 - att 23
Rodada 5
Aventureiro: vida 23 - att 20 - def 1
Monstro: vida 7 - att 23
Rodada 6
O monstro morreu!
```

## AC6

Acessar o convite para o site **Beecrowd** recebido no seu e-mail do Ibmec (matricula@alunos.ibmec.edu.br). Caso já tenha uma conta no Beecrowd com seu e-mail pessoal, me envie um e-mail (silva.victor@ibmec.edu.br) ou entre em contato pelo WhatsApp para que eu possa enviar um novo convite.

Na disciplina "Estruturas de Dados", realizar a lista com o nome "AC6". Suba o código no GitHub como normalmente e envie pelo https://estudante.ibmec.br o link para os exercícios no GitHub.
