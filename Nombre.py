'''
Escriba un programa que pregunte el nombre del usuario en la consola y después
de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
donde <NOMBRE> es el nombre del usuario en mayusculas y <n> es el numero de
letras que tiene el nombre.
'''

nombre = str.upper(input("Ingrese su nombre: "))
n = len(nombre)
print(f"Su nombre es {nombre} y tiene {n} letras.")
