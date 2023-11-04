import random
from datetime import datetime

def listaCart(linhas):
  x = len(linhas)
  M = [[]]*x
  for i in range(x):
      M[i] = linhas[i].rstrip().split(',')    
  return M

def selecionaCart(lista):
  x = len(lista)
  M = [[]]*4
  samples = random.sample(range(x), 4)
  for i in range(len(M)):        
      M[i] = lista[samples[i]]  
  return M

def sorteio():
  return random.sample(range(1,50), 49)

def main():    
  print('----------------- BINGOLITE -----------------')  
  arquivo = open('cartelas.txt', 'r')
  vencedores = open('vencedores.txt', 'a')
         
  linhas = arquivo.readlines()
  lista_cart = listaCart(linhas)        
  cartelas = selecionaCart(lista_cart)

  resposta = ''
  atual_cart, indice_sorteado = 0, 0
  sorteado = sorteio()
  sorteados = []
  vencedora = -1
  controle = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
  lista_vitoria = [1,1,1,1,1]
  loop = True
  
  while loop:
    print(f'Número Sorteado: {sorteado[indice_sorteado]}')
    print()
    for i in range(4):
      tamanho = len(cartelas[i])
      if i == atual_cart:
        print(f'#Cartela {i+1}# -- ', end=' ')
      else:
        print(f'Cartela {i+1} -- ', end=' ')       
          
      for j in range(tamanho):
        if int(cartelas[i][j]) == sorteado[indice_sorteado]:
          sorteados.append(cartelas[i][j])
          controle[i][j] = 1
            
      for k in range(tamanho):
        desigual = ''
        for l in range(len(sorteados)):
          if cartelas[i][k] == sorteados[l] and cartelas[i][k] != desigual:
            print(f'#{cartelas[i][k]}#', end=' ')
            desigual = cartelas[i][k]              
        if cartelas[i][k] != desigual:
          print(f'{cartelas[i][k]}', end=' ')
            
      print('\n')        
            
      if controle[i] == lista_vitoria:
        vencedora = i         
          
    indice_sorteado += 1

    if vencedora != -1:
      if vencedora == atual_cart:
        print('-> PARABÉNS, VOCÊ VENCEU!!!')
        nome = input('-> Digite seu nome para constar no rol de vencedores:')
        
        data_e_hora = datetime.now()
        data = data_e_hora.strftime('%d/%m/%Y')
        horario = data_e_hora.strftime('%H:%M')
        
        venc = f'Nome: {nome}, Data: {data} e Horário: {horario} \n'
        vencedores.write(venc)
        loop = False
      else:
        print('-> Outra cartela foi completada!')
        print('-> Mais sorte da próxima vez!')  
        loop = False
    else:
      resposta = input('Selecione outra cartela ou pressione ENTER para sortear: ')
      print()
      if resposta != '':
        atual_cart = int(resposta) - 1
  arquivo.close()
  vencedores.close()
main()
