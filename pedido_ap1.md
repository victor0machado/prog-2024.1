# Pedido da AP1

Recomendo utilizar o modelo do projeto [disponível aqui](https://github.com/victor0machado/prog-2024.1/blob/main/modelos/ap1/ap1.py). Mesmo que não use o modelo, veja a documentação de cada função para entender os detalhes das mecânicas e do desenrolar do jogo.

## Descrição do projeto

O seu time deve desenvolver um jogo **Caça ao Tesouro**, por linha de comando. Neste jogo, o jogador controla um aventureiro (representado pelo caractere `@`) que está em busca de um tesouro (representado pelo caractere `X`) localizado em um mapa 10 x 10. Enquanto percorre o mapa atrás do tesouro, o aventureiro pode se deparar com diversos monstros!

### Comandos

O jogador possui os seguintes comandos possíveis, todos controlados pelo teclado:

- Teclas `W`, `A`, `S` e `D`: indicam a movimentação do aventureiro pelo mapa (respectivamente cima, esquerda, baixo e direita);
- Tecla `T`: Exibe os atributos do aventureiro;
- Tecla `Q`: Sai do jogo.

### Elementos principais

O aventureiro é um dicionário em Python, que possui os seguintes dados:

- Nome: informado pelo jogador assim que o jogo começa;
- Força: um inteiro aleatório entre 10 e 18;
- Defesa: um inteiro aleatório entre 10 e 18;
- Vida: um inteiro inicializado aleatoriamente entre 100 e 120;
- Posição: uma lista com dois elementos, inicializado como `[0, 0]`;

Além disso, o aventureiro possui algumas ações possíveis:

- Atacar: retorna um inteiro igual à força mais um valor aleatório entre 1 e 6;
- Defender: recebe como parâmetro um valor de dano, e reduz desse valor a defesa do aventureiro. O valor final é reduzido da vida atual do aventureiro (se for positivo);
- Mover: muda as coordenadas do aventureiro, na direção indicada (se possível);
- Está vivo: retorna um booleano informando se o aventureiro está vivo.

O jogo também deve ter pode gerar monstros, que são armazenados em dicionários e que possuem os seguintes dados:

- Força: um inteiro aleatório entre 5 e 25
- Vida: um inteiro aleatório entre 10 e 100

Além disso, o monstro possui algumas ações possíveis:

- Atacar: retorna um inteiro igual à força;
- Defender: recebe como parâmetro um valor de dano. O valor recebido é reduzido da vida atual do monstro;
- Está vivo: retorna um booleano informando se o mosntro está vivo.

Por fim, o jogo ainda possui um dicionário para o tesouro, que tem um único atributo `posicao`, que corresponde a uma lista com dois inteiros.

### Mecânica

O jogo se passa em um mapa de dimensão 10 x 10. O aventureiro sempre começa na posição `[0, 0]`, e o tesouro em uma posição aleatória no mapa (exceto a posição `[0, 0]`). O aventureiro é representado pelo caractere `@`, e o tesouro pelo caractere `X`.

Em cada rodada, o aventureiro pode fazer uma de quatro ações:

- Mover-se: utilizando as teclas `W`, `A`, `S` e `D`, o aventureiro se move pelo mapa (ver efeito disso a seguir);
- Ver atributos: verifica força, defesa e vida do aventureiro;
- Sair do jogo: utilizando a tecla `Q`, o jogador foge e o jogo encerra.

#### Movimentando

Ao movimentar o aventureiro, o jogo deve recalcular a sua coordenada baseado na direção que ele se moveu. O aventureiro não pode se mover para as extremidades do mapa (sua posição não pode ser inferior a 0 e nem superior a 9).

Caso o aventureiro realmente se mova, um de dois efeitos podem ocorrer:

- Nada (60%): simplesmente nada acontece, e o aventureiro anda para a nova posição;
- Monstro! (40%): um novo monstro surge para lutar contra o aventureiro! Veja a seção abaixo.

No final do efeito selecionado, se o aventureiro estiver vivo, o mapa é redesenhado com o aventureiro na nova posição.

#### Combate

O combate se dá nas seguintes ações:

- Fase do aventureiro: ataca, armazenando o dano;
- Fase do monstro: defende, atualizando a vida dele;
- Fase do monstro: ataca, armazenando o dano;
- Fase do aventureiro: defende, atualizando a vida dele.

O combate encerra assim que um dos dois, aventureiro ou monstro, chega a uma vida menor que zero.

#### Encerramento

O jogo acaba quando (a) o aventureiro morre, ou (b) o aventureiro chega no tesouro.

## Exemplo de execução do jogo

O trecho abaixo é uma extração de como foi executado o jogo:

```
Deseja buscar um tesouro? Primeiro, informe seu nome: Victor
Saudações, Victor! Boa sorte!
@ . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: d
. @ . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: s
. . . . . . . . . .
. @ . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: s
Um novo monstro apareceu!
Victor causa 15 de dano! Vida do monstro: 29
Monstro causa 12 de dano! Vida de Victor: 118
Victor causa 13 de dano! Vida do monstro: 16
Monstro causa 12 de dano! Vida de Victor: 117
Victor causa 14 de dano! Vida do monstro: 2
Monstro causa 12 de dano! Vida de Victor: 116
Victor causa 17 de dano! Vida do monstro: -15
Monstro foi derrotado!
. . . . . . . . . .
. . . . . . . . . .
. @ . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: d
. . . . . . . . . .
. . . . . . . . . .
. . @ . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: d
Um novo monstro apareceu!
Victor causa 15 de dano! Vida do monstro: 72
Monstro causa 21 de dano! Vida de Victor: 106
Victor causa 17 de dano! Vida do monstro: 55
Monstro causa 21 de dano! Vida de Victor: 96
Victor causa 13 de dano! Vida do monstro: 42
Monstro causa 21 de dano! Vida de Victor: 86
Victor causa 17 de dano! Vida do monstro: 25
Monstro causa 21 de dano! Vida de Victor: 76
Victor causa 16 de dano! Vida do monstro: 9
Monstro causa 21 de dano! Vida de Victor: 66
Victor causa 18 de dano! Vida do monstro: -9
Monstro foi derrotado!
. . . . . . . . . .
. . . . . . . . . .
. . . @ . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: d
. . . . . . . . . .
. . . . . . . . . .
. . . . @ . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: d
. . . . . . . . . .
. . . . . . . . . .
. . . . . @ . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: d
. . . . . . . . . .
. . . . . . . . . .
. . . . . . @ . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: d
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . @ . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: d
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . @ .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: s
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . @ .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: s
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . @ .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: s
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . @ .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: s
Um novo monstro apareceu!
Victor causa 17 de dano! Vida do monstro: 47
Monstro causa 7 de dano! Vida de Victor: 66
Victor causa 14 de dano! Vida do monstro: 33
Monstro causa 7 de dano! Vida de Victor: 66
Victor causa 15 de dano! Vida do monstro: 18
Monstro causa 7 de dano! Vida de Victor: 66
Victor causa 17 de dano! Vida do monstro: 1
Monstro causa 7 de dano! Vida de Victor: 66
Victor causa 13 de dano! Vida do monstro: -12
Monstro foi derrotado!
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . @ .
. . . . . . . . . .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: s
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . @ .
. . . . . . . . X .
. . . . . . . . . .
Insira o seu comando: s
Um novo monstro apareceu!
Victor causa 18 de dano! Vida do monstro: 25
Monstro causa 19 de dano! Vida de Victor: 58
Victor causa 17 de dano! Vida do monstro: 8
Monstro causa 19 de dano! Vida de Victor: 50
Victor causa 18 de dano! Vida do monstro: -10
Monstro foi derrotado!
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . @ .
. . . . . . . . . .
Parabéns, Victor! Você encontrou o tesouro!
```

## Avaliação

Os projetos serão avaliados de acordo com os seguintes critérios:

* Qualidade do código (30%): código de acordo com os padrões de escrita, algoritmos bem estruturados e arquitetura bem organizada;
* Testes realizados pelo professor não apresentam falhas (70%).

## Informações gerais:

* Prazo: entrega até 23/04/2023 (impreterivelmente);
* Grupos de no mínimo 3 e no máximo 5 pessoas;
* Método de entrega: via Sala de Aula Virtual (estudante.ibmec.br). Formato de entrega:
  * Criar um repositório no GitHub exclusivo para a AP1, torná-lo **privado** e adicionar o professor (@victor0machado) como colaborador. Subir no estudante o link para o repositório;
  * Um único aluno de cada grupo cria o repositório;
  * Um único aluno envia o link do projeto pela Sala de Aula Virtual.
