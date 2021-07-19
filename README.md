<h1 align="center"> Desafio Engenharia </h1>

### <p align="justify"> O desafio proposto foi o desenvolvimento de uma pilha de floats nas seguintes linguagens: Python 3+, Node.js (JavaScript) ou ANSI C. A linguaguem escolhida foi Python na versão 3.9.5 por uma questão de maior famialiridade. Pilhas são estruturas de dados, do tipo LIFO(last in first out), onde o último elemento a ser inserido é o primeiro a ser removido, permitindo acesso somente ao último item de dados.  </p> 

### <p align="justify"> Ao iniciar a programação optei por utilizar classe, porque proporcionam uma forma de organizar dados e funcionalidades juntos, e listas, porque irei manipular o topo da estrutura (o final da lista). Nas funções não utilizei as funções prontas do python para poder mostrar o conceito de cada uma e a minha linha de raciocínio.    </p> 


Tabela de conteúdos
=================
<!--ts-->
   * [Métodos da Classe](#funções-utilizadas)
       * [Instanciação](#instanciação)
       * [Empilhar](#empilhar)
       * [Desempilhar](#desempilhar)
       * [Topo](#topo)
       * [Menor Valor](#menor-valor)
       * [Visualizar Pilha](#visualizar-a-pilha)   
   * [Instalação](#instalação)
      * [Pré Requisitos](#pré-requisitos)
      * [Local files](#local-files) 
   * [Como usar](#como-usar)
   * [Testes](#testes)
   * [Conclusão](#conclusão)
<!--te-->


### Modelo de uma Estrutura de dados do tipo Pilha. 

<a href="https://imgur.com/SlYK5Be"><img src="https://i.imgur.com/SlYK5Be.png" title="source: imgur.com" /></a>

Estrutura de Dados do tipo pilha é usada para armazenamento de dados com um tipo de estrutura onde os dados ficam empilhados de modo no qual podemos somente acrescentar ou retirar informações do topo dessa pilha.

### Funções Utilizadas
<h1 align=""> </h1>
Algumas operações básica de estrutura de dados de pilha, seriam:

### Instanciação
<p align="justify"> A operação de instanciação (“invocar” um objeto classe) cria um objeto vazio. Quando define um método init(), o processo de instanciação automaticamente invoca __init() sobre a instância recém criada. </p> 

### Empilhar
Empilhamento nessa estrutura de dados é adicionar um dado ao topo da pilha, ou seja, dessa forma você adiciona dados em forma sequênciais sem afetar o restante da pilha. Não é possível empilhar ou adicionar dados ao meio ou inicio da pilha, essa ação só pode ser feita no topo.

![image](https://user-images.githubusercontent.com/80843917/126227902-b2f265f1-a4c9-499e-9de2-989f9f2a8ac6.png)


### Desempilhar
O desempilhar nessa estrutura de dados é a retirada do dado do topo da pilha, com isso você retira o último dado da estrutura sem afetar o restante da pilha. Não é possível retirar dados que não sejam do topo.

![image](https://user-images.githubusercontent.com/80843917/126228184-03723a95-8007-45bb-b055-c64980fbf40c.png)

### Topo
Mostrar o Topo da estrutra de dados, ou seja, nessa função tem como objetivo ver o último valor/dado que foi empilhado, assim como ver o próximo a ser desempilhado/retirado.

![image](https://user-images.githubusercontent.com/80843917/126228272-e1f386c0-abbb-4d4d-94c1-c54e38a31cbd.png)


### Menor Valor
Nessa casso, com valores float, tem como função ver o dado de menor valor Float da pilha de dado.

![image](https://user-images.githubusercontent.com/80843917/126228330-e061ec71-54d5-4ed1-8b1c-f970538d2762.png)


### Visualizar a Pilha

Visualiza todo os valores correspondentes as suas posições na pilha de dados. Ou seja, nele podemos ter o panorâma geral da estrura da pilha e seus respectivos valores.

![image](https://user-images.githubusercontent.com/80843917/126228362-566843ad-96dd-4c05-9e8e-c09cfe53dc2d.png)


### Como Usar 
<h1 align=""> </h1>

Para uma melhor interação com o usuário, foi utilizado uma função Main. Com isso o usuário teria opções em número para escolher quais procedimentos iria querer realizar com a pilha de FLOAT.

Função Main Interagindo com o Usuário:

![image](https://user-images.githubusercontent.com/80843917/126230995-e19a363c-2a60-4a45-9129-6cea03fe42e8.png)

Com isso dentro das opções escolhidas você irá realizar uma tarefa na pilha, caso escolha a função empilhar, logo após você entrará com o número FLOAT desejado para o armazenamento do dado na PILHA.

Exemplo 1:

![image](https://user-images.githubusercontent.com/80843917/126231200-0c97d519-00ec-4be3-99c0-4db21b1c2cef.png)





### Instalação
<h1 align=""> </h1>

### Pré Requisitos

Antes de começar, você vai precisar ter instalado em sua máquina a seguinte ferramenta:
[Python](https://www.python.org/).
Além disto é bom ter um ambiente integrado de desenvolvimento e à aprendizagem do Python para trabalhar com o código como [IDLE](https://www.python.org/).

### Local Files 
Apesar do Python ser um dos componentes padrões de vários sistemas operacionais, como do Linux, AmigaOS 4, FreeBSD, NetBSD, OpenBSD e OS X, é preciso ter a ferramenta e pode ser encontrada no site oficial.

[Python(Windows/MacOS/Linux/Outras Plataformas)](https://www.python.org/).

- Alguns terminais onde pode-se ter um ambiente integrado para programar/desenvolver linguaguem Python no Windows.

[IDLE (Windows/MacOS/Linux/Outras Plataformas)](https://www.python.org/).

[Pycharm (Windows/MacOS/Linux)](https://www.jetbrains.com/pt-br/pycharm/download/)

### Testes
<h1 align=""> </h1>

Alguns teste foram feitos para por em prova o empilhamento de dados do tipo Float e possíveis entradas do usuários.
Nessa entradas foram levada em contas, entradas corretas, ou seja do tipo FLOAT e entradas do quais o empilhamento não deve ser feito, como entradas de valores inteiros, de string, de dados vazios, entre outros tipo de entradas.

![image](https://user-images.githubusercontent.com/80843917/126229299-89b1eafd-1f29-4719-9abc-5df450044c3c.png)

![image](https://user-images.githubusercontent.com/80843917/126232054-e57b8287-7a8e-40e6-8ce6-b3ecca1fee0e.png)

### Conclusão
<h1 align=""> </h1>
No Desafio Engenharia prospoto, nossa estruturação de dados, armazenava elementos com valor FLOAT, com isso criamos pilhas com esses valores.

Alguns erros foram sanados durante o processo, caso o usuário entrasse com valores diferentes de FLOAT como por exemplo:

* Usuário entrar com valores Inteiros(int)
* Usuário entrar com Strings (str)
* Usuário entrar com  Listas Vazias ([])
* Usuário entrar com valores nulos ('')
* Usuário entrar com String de Floats

Esses erros foram contornados com condicionais e Tratamento de Erro e Exceções..
Com isso ffoi chegada a estruturação de dados do tipo PILHA, com entrada em valores FLOAT.

De modo geral pilhas são usualmente utilizadas por muitos programadores para estruturação de dados.
Dessa forma alguns exemplos de sistema onde usa essa estrura são:
* Funções recursivas em compiladores;
* Mecanismo de desfazer/refazer dos editores de texto;
* Navegação entre páginas Web;
