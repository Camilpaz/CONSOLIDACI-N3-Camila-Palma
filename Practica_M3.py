#DESCRIPCIÓN
#Dada la siguiente lista de nombres:
#• Harry Houdini
#• Newton
#• David Blaine
#• Hawking
#• Messi
#• Teller
#• Einstein
#• Pele
#• Juanes
# Sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y Einstein son científicos.


# Separar los nombres en tres grupos: magos, científicos y otros

ls_magos = ["Harry Houdini", "David Blaine", "Teller"]
ls_cientificos = ["Newton", "Hawking", "Einstein"]
ls_otros = ["Messi", "Pele", "Juan"]

# Escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la frase ‘El gran‘ antes del nombre de cada mago.

def hacer_grandioso(ls_magos):
    return  print("el gran: ", ls_magos)
    
hacer_grandioso(ls_magos[0])
hacer_grandioso(ls_magos[1])
hacer_grandioso(ls_magos[2])

# Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de lalista.

personas = ls_magos + ls_cientificos + ls_otros

def imprimir_personas(personas):
    for x in personas:
        print("Nombre:", x)    

imprimir_personas(personas)

# Imprimir en pantalla la lista completa de nombres antes de ser modificados; luego imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.


print("Lista de nombres antes de ser modificados: ", personas)
print("Lista de magos grandiosos: ", ls_magos)
print("Lista de científicos: ", ls_cientificos)
print("Lista de otros: ", ls_otros)
