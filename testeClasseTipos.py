from datafile import filename

from classes.tipos import Tipos

# Tipos.read(filename + 'YouTube.db')

# obj = Tipos.from_string("222;Word")

# print("objeto sem estar gravado ",obj)

# Tipos.insert(getattr(obj,Tipos.att[0]))

# obj = Tipos.from_string("333;Excel")
# Tipos.insert(getattr(obj,Tipos.att[0]))


# print("\nLista dos onjetos gravados " ,Tipos.lst)


# # alterar
# obj = Tipos.first()
# print ("\nPrimeiro objeto gravado ",obj)
# obj.name = "fimes terror"
# Tipos.update(getattr(obj, Tipos.att[0]))

Tipos.read(filename + 'YouTube.db')

print("\nobjectos gravados")    
for code in Tipos.lst:
    print(Tipos.obj[code])