#No desafio vamos trabalhar com pilhas que são estruturas
#de dados do tipo LIFO(last-in first-out), onde o último
#elemento a ser inserido é o primeiro a ser removido.
class Pilha:
    
    def __init__(self):
    #Instanciação da classe Pilha que cria um objeto vazio
        self.elementos = []

    def empilhar(self, elemento):
    #Função que recebe o elemento e adiciona no topo da pilha
        if type(elemento)== float: 
            self.elementos += [elemento]
            print('O elemento '+str(elemento)+' foi inserido no topo')
        else:
            print('O elemento '+str(elemento)+' não é do tipo float')

    def desempilhar(self):
    #Função que retira o ultimo elemento da pilha
        if self.elementos == []:
            print('A pilha já está vazia.')
        elif len(self.elementos) < 2:
            self.elementos = self.elementos[:-1]
            print('Todos os elementos da pilha foram desempilhados')
        else:
            x = self.elementos[-1]
            self.elementos = self.elementos[:-1]
            print('O elemento '+ str(x)+' foi desempilhado')

    def topo(self):
    #Função que confere o elemento que está no topo e o retorna
        if self.elementos == []:
            print('A pilha está vazia')
        else:
            resultado = self.elementos[-1]
            print('O elemento '+ str(resultado)+' está no topo da pilha.')
        
    def menor_valor(self):
    #Função que compara todos os valores entre si, os coloca em ordem crescente
    #e retorna o primeiro valor da lista ordenada.
        if self.elementos == []:
            print('A pilha está vazia')
        else: 
            lista = self.elementos
            menor = lista[0]
            for i in lista:
                if i < menor: #Compara todos os valores da pilha
                    menor = i
            print('O elemento '+str(menor)+' é o menor valor da pilha.')
        
    def get_pilha(self):
    #Função que mostra o estado da pilha
        if self.elementos == []:
            print('A pilha está vazia')
        else:
            self.elementos = self.elementos[:] #Cópia da lista
            a = str(self.elementos) #Transforma em string
            b = str.replace(a, ',', ' ->') #Troca o separador
            print(b)


def main():
#Função para executar o código diretamente
    print('\n Escolha uma opção\n')
    print('(1) Empilhar \n')
    print('(2) Desempilhar \n')
    print('(3) Topo \n')
    print('(4) Menor Valor \n')
    print('(5) Visualizar pilha \n')
    print('(6) Sair \n')
    
    while True:
        try:
            opcao = int(input('- Digite sua opção: '))
            if opcao >= 1 and opcao <=6:
                break
            if opcao >=7:
                print("O valor inserido não é uma opção válida. Tente novamente...")
                
        except Exception:
            print("O valor inserido não é uma opção válida. Tente novamente...")
                
    pilha = Pilha()
    while opcao != 7:
        if opcao == 1:
            while True:
                try:
                    print('Digite o valor para adicionar: ')
                    elemento = float(input())
                    break
                except ValueError:
                    print("O valor inserido não é um float válido. Tente novamente...")

            pilha.empilhar(elemento)

        if opcao == 2:
            pilha.desempilhar()

        if opcao == 3:
            pilha.topo()
            

        if opcao == 4:
            pilha.menor_valor()
            

        if opcao == 5:
            pilha.get_pilha()

        if opcao == 6:
             break
        
        while True:
            try:
                opcao = int(input('- Digite sua opção: '))
                if opcao >= 1 and opcao <=6:
                    break
                if opcao >=7:
                    print("O valor inserido não é uma opção válida. Tente novamente...")
                
            except Exception:
                print("O valor inserido não é uma opção válida. Tente novamente...")
        

if __name__ == '__main__':
    main()
                    
            

   
