from  DesafioEngenharia import *

#Arquivo para demonstrar os casos de testes e resultados das funções

print('Testes das funções do desafio! \n')

#teste1
print('\n - Objetivo: Testa se  é possivel criar uma instância da class pilha')
pilha = Pilha()

#teste2
print('\n - Objetivo: Verificar com o get_pilha se o teste acima criou uma instância')
print('- Saída esperada = A pilha está vazia \n - Saída obtida =')
pilha.get_pilha()


#teste3
print('\n - Objetivo: Testa se é possivel empilhar um elemento do tipo inteiro')
print('- Saída esperada = O elemento 8 não é do tipo float \n - Saída obtida =')
pilha.empilhar(8)

#teste4
print('\n - Objetivo: Testa se é possivel empilhar um elemento do tipo float')
print('- Saída esperada = O elemento 3.4 foi inserido no topo  \n - Saída obtida =')
pilha.empilhar(3.4)

#teste5
print('\n - Objetivo: Testa se é possivel desempilhar')
print('- Saída esperada = Todos os elementos da pilha foram desempilhados \n - Saída obtida =')
pilha.desempilhar()

#teste6
print('\n - Objetivo: Testa se é possivel empilhar um elemento vazio')
print('- Saída esperada = O elemento '' não é do tipo float \n - Saída obtida =')
pilha.empilhar('')

#teste7
print('\n - Objetivo: Testa se é possivel empilhar uma lista vazia')
print('- Saída esperada = O elemento [] não é do tipo float \n - Saída obtida =')
pilha.empilhar([])

#teste8
print('\n - Objetivo: Testa se é possivel empilhar uma letra')
print('- Saída esperada = O elemento a não é do tipo float \n - Saída obtida =')
pilha.empilhar('a')

#teste9
print('\n - Objetivo: Testa se a desempilha o ultimo elemento')
print('- Saída esperada =  \n - Saída obtida =')
pilha.empilhar(5.3)
pilha.empilhar(3.9)
pilha.empilhar(0.7)
pilha.empilhar(1.4)
pilha.empilhar(9.0)
pilha.desempilhar()

#teste10
print('\n - Objetivo: Testar a função menor valor')
print('- Saída esperada = O elemento 0.3 é o menor valor da pilha \n - Saída obtida =')
pilha.menor_valor()

#teste10
print('\n - Objetivo: Testar a função topo')
print('- Saída esperada = O elemento 9.0 é o topo da pilha \n - Saída obtida =')
pilha.topo()

#teste11
print('\n - Objetivo: Testar a função vizualizar pilha')
print('- Saída esperada = [5.3 -> 3.9 -> 0.7 -> 1.4]  \n - Saída obtida =')
pilha.get_pilha()

#teste12
print('\n - Objetivo: Testar a função desempilhar')
print('- Saída esperada = A pilha está vazia  \n - Saída obtida =')
pilha.desempilhar()
pilha.desempilhar()
pilha.get_pilha()
pilha.desempilhar()
pilha.desempilhar()
pilha.get_pilha()

#teste13
print('\n - Objetivo: Testar a função menor valor')
print('- Saída esperada = A pilha está vazia \n - Saída obtida =')
pilha.menor_valor()

#teste14
print('\n - Objetivo: Testar a função topo')
print('- Saída esperada = A pilha está vazia \n - Saída obtida =')
pilha.topo()

#teste15
print('\n - Objetivo: Testar a função desempilhar')
print('- Saída esperada = A pilha já está vazia \n - Saída obtida =')
pilha.desempilhar()







