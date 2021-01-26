print('Escreva um programa que leia a quantidade de dias,horas,minutos e segundos do usuario.Calcule o total em segundos')
d= int(input('Entre em contato com a quantidade em dias'))
ds=(d*24*60*60)
print ('Resultado do valor de dias em segundos',ds)
#(na variavel h o usuario ira entrar com valor em horas e iremos transformar em segundos 
h= int(input('Entre com a quantidade de horas'))
hs=(h*60*60)
print('Tranformado valor de horas em segundos',hs)
#Valor de Minutos transformados em segundos
m=int(input('Entre com o valor em minutos'))
ms= (m*60)
print('Transformado o valor de minutos em segundos',ms)
seg=int(input('Entre com a quantidade em segundos'))
print('Valor em segundos')
totaldosvalores = (ds+hs+ms+seg)
print('Exibindo o total de todas as somas transformadas em segundos',totaldosvalores)        
       
       
       
       
