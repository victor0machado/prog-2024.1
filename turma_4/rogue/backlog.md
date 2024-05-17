[X] transportar o mapa para a interface gráfica
[X] movimento do aventureiro
[X] visualizar na tela os atributos do aventureiro
[X] resumir o combate na tela

[X] skins (caractere e cor)
- Adicionar novas cores
- Criar lista de cores possíveis
- Criar lista de caracteres possíveis
- Criar métodos para mudar de cor e caractere
- Criar atalhos no teclado
- Refatorar método de renderização

[X] criar um boss no local do tesouro
- Criar uma classe que herda Monstro
- Definir novos atributos
- Quando a posição do aventureiro for igual à do tesouro, iniciar um combate com o boss

[X] criar monstros diferentes
- Criar subclasses de Monstro
- Criar a lista de monstros
- Na função `movimentar`, quando for definido que um monstro vai aparecer, escolher aleatoriamente entre os monstros

[X] montar sistema de níveis de dificuldades
- Criar uma variável `dificuldade` no módulo `mecanicas`
- Alterar as classes de monstros para receber o nível de dificuldade
- Alterar a definição dos atributos dos monstros conforme a dificuldade
- Alterar as chamadas dos monstros nos combates
- Associar a mudança de dificuldade a duas teclas do teclado

[X] sistema de níveis
- Criar um atributo xp para os monstros
- Criar atributos xp e nível para o aventureiro
- Criar métodos para o aventureiro ganhar xp e subir de nível
- Criar uma forma de progressão dos atributos do aventureiro (vida, força e defesa)
- Alterar a função de combate, para que o aventureiro ganhe xp quando derrotar o monstro
- Alterar a interface para mostrar o nível do aventureiro

[ ] criar um inputbox para pedir o nome


[ ] criar sistema de classes



[ ] criar sistema de itens
[ ] criar sistema de equipamentos
[ ] outros atributos
[ ] sistema de batalhas por turnos
[ ] habilidades diferentes
[ ] ataques especiais para monstros
[ ] sistema de drop
[ ] mecânica de elementos
[ ] expandir o mapa
[ ] sistema de andares
[ ] sistema de loja no jogo (drop de dinheiro e compra de itens)
[ ] criar um monstro especial que persegue o aventureiro
