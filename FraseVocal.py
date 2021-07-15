'''
Escriba un programa que pida al usuario que introduzca una frase en la consola
y una vocal en minuscualas, y despues muestre por pontalla la misma frase pero
con la vocal introducida en mayusculas
'''

frase = input("Introduzca una frase: ")
vocal = str.lower(input("Introduzca una vocal en minuscula: "))
print(frase.replace(vocal,vocal.upper()))
#La vocel establecida se convierte en mayuscula en toda la frase
