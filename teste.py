from models.cliente import Cliente
from models.conta import Conta

marcus = Cliente('marcus', 'marcus@gmail.com', '60022115005', '10/11/2001')
banrisul = Conta(marcus)

#print(marcus)
print(banrisul)
