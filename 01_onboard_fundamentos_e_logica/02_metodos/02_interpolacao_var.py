'''
  % 
  f strings - f""
'''

nome = "Thiago"
idade = 28
profissao = "Programador"
linguagem = 'Python'

#interpolacao com porcentagem %
print("Olá, me chamo %s. Tenho %d anos de idade. Trabalho como %s" %(nome, idade, profissao))

#interpolacao com format {}
print("Olá, me chamo {}. Tenho {} anos de idade. Trabalho como {}".format(nome, idade, profissao))

#interpolacao com f-string
print(f"Olá, me chamo {nome}. Tenho {idade} anos de idade. Trabalho como {profissao}")

PI = 3.14159

print(f'Valor de PI: {PI:.2f}')
print(f'Valor de PI: {PI:10.2f}')