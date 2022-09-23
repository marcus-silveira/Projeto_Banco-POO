from models.cliente import *

dados = {101: {'Nome': 'Marcus Vinicius Silveira ', 'E-mail': 'marcus@gmail.com', 'CPF': '600.221.150-05', 'Nascimento': '10/11/2001'}}
xx = dados[101]



list = []
for chave, valor in dados[101].items():
    list.append(valor)
#print(list)

cliente = Cliente(list[0], list[1], list[2], list[3])
print(cliente)
