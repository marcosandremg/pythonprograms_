"""
1 -

x = int(input())
print(x)

2 -

x = float(input())
print(x)

3-
print("Digite três inteiros")
int_1 = int(input())
int_2 = int(input())
int_3 = int(input())
y = int_1+int_2+int_3
print(f'A soma deles é {y}')

4-
x = float(input())
print(pow(x, 2))

5 -
x = float(input())
print(x/5)

6-
c = float(input())
f = (c*(9.0/5.0)) + 32
print(f'A temperatura é {f}°F')

7-
f = float(input())
c = (5.0*(f-32.0))/9
print(f'A temperatura é {c}°C')

8-
k = float(input())
c = k-273.15
print(f'A temperatura é {c}°C')

9-
k = float(input())
c = k-273.15
print(f'A temperatura é {c}°C')

10-
k = float(input())
m = k/3.6
print(f'A velocidade é {m} m/s')
11-
m = float(input())
k = m*3.6
print(f'A velocidade é {k} km/h')

Pulando para o 28, tendo em vista que todos os outros exercícos são semelhantes a esses acima.

28-

x = int(input())
y = int(input())
z = int(input())
print((pow(x, 2)) + (pow(y, 2)) + (pow(z, 2)))

29-
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
print((n1+n2+n3+n4)/4)

30-
print('Qual é o seu valor em reais?')
x = float(input())
print('Qual é a cotação do dólar?')
y = float(input())
print(f'O valor em dólar é: {x/y}$')

31-
x = int(input())
print(f'Antecessor {x - 1} sucessor {x+1}')

32-
x = int(input())
print(((3*x)+1) + ((2*x)-1))

33-
x = int(input())
print(f'A área do quadrado é: {x*x}m²')

34-
r = float(input())
print(f'A área da circunferência é: {3.141592*r*r}m²')

35-

a = float(input())
b = float(input())
print(f'A hipotenusa é: {pow((a*a)+(b*b), 1/2)}')
#ou
print(f'A hipotenusa é: {pow(((pow(a, 2))+(pow(b, 2))), 1/2)}')

36-
h = float(input())
r = float(input())
print(f'O volume do Cilindro é: {3.141592*r*r*h}m³')
#ou
print(f'O volume do Cilindro é: {3.141592*(pow(r, 2))*h}m³')

37-
h = float(input())
print(f'O valor é: R${h}')
print(f'Com o desconto: R${h-((12/100)*h)}')

38-
h = float(input())
print(f'O novo salário é R${h+((25/100)*h)}')

39-
t = 780000.0
p = t*0.46
s = t*0.32
print(f'O primeiro irá receber: {p}')
print(f'O segundo irá receber: {s}')
print(f'O terceiro irá receber: {t-p-s}')

40-
print('Quantos dia de trabalho o encanador teve?')
d = int(input())
v = 30.00*d
print(f'Então ele irá receber R${v - (0.08*v)}')
print(f'Valor sem IR R${v}')

41-
x = float(input('Qual o valor da hora de trabalho?'))
h = int(input('Quantas horas de trabalho por dia?'))
pg = x*h

print(f'O valor a ser pago é R${pg + (0.1*pg)}')

42-
sb = float(input('Qual é o salário base?'))
print(f'O valor do salário base: R${sb} \nO valor da gratificação é: R${0.05*sb}\nO Valor do Imposto de Renda é: '
      f'R${0.07*sb}\nO Valor que deverá ser recebido é: R$ {sb-(0.02*sb)}')

43 -

t = float(input('Qual o valor total da venda?'))
v_com_des = -(0.1*t)+t
com_a_vista = 0.05*t
com_par = 0.05*v_com_des
print(f'O valor total: R${t}\nO valor com 10% de desconto: R${v_com_des}\nValor da parcela(Compra dividida em 3x:'
      f'R${v_com_des/3}\nComissão da vendedora caso a venda seja a vista: R${com_a_vista}\nComissão da vendedora'
      f'caso a venda seja parcelada: R${com_par}')

44 -
h_deg = float(input('Qual é altura do Degrau?'))
h_usu = float(input('Qual altura que o usuário deseja alcançar?'))
print(f'O usuário deverá subir no mínimo: {h_usu/h_deg} degraus')

45-
x = input('Digite uma letra MAIÚSCULA     ')
print(f'{x.lower()}')
Mas não é isso que ele quer.
Método correto:
x = (input('Digite uma letra MAIÚSCULA     '))
print(chr(ord(x) + 32))

46-
x = input('Digite um número de 3 digítos e vamos inverter ele\n'
          '')
print(x[::-1])

47-
x = input('Digite um número de 4 digitos\n'
          '')
print(f'{x[0]}\n{x[1]}\n{x[2]}\n{x[3]}')

48-
x = int(input('Digite os valores em segundos  '))
print(f'São {int(x/3600)}h {int((x%3600)/60)}min {int((x%3600)%60)}seg')

49-


50-
id = int(input('Digite sua Idade  '))
ano = int(input('Digite o ano que estamos  '))
print(f'Você nasceu em {ano - id}')

51-
x, y = input('Digite as coordenadas ex: x y\n').split()
print(f'A distãncia das coordenadas até a origem é: {pow((pow((float(x)), 2) + pow((float(y)), 2)), 1/2)}')

52 -
jog1 = float(input('Quanto o jogador 1 apostou?'))
jog2 = float(input('Quanto o jogador 2 apostou?'))
jog3 = float(input('Quanto o jogador 3 apostou?'))
prem = float(input('Qual o valor do Premio?'))
print(f'O Jogador 1 irá ganhar: R${(jog1/(jog1+jog2+jog3))*prem}\n'
      f'O Jogador 2 irá ganhar: R${(jog2/(jog1+jog2+jog3))*prem}\n'
      f'O Jogador 3 irá ganhar: R${(jog3/(jog1+jog2+jog3))*prem}\n')

53-
c = float(input('Digite o Comprimento '))
l = float(input('Digie a largura '))
p = float(input('Digie o preço do metro da tela '))
print(f'Você irá gastar:R${(c+c+l+l)*p} para cercar todo o terreno com a tela')

"""