'''
Escribir un programa que pida al usuario su peso en kg y estatura en metros, calcule el
índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase “Tu
índice de masa corporal es <imc>” donde <imc> es el índice calculado redondeado con
dos decimales.
Dato
Imc = peso/(estatura)^2
'''

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su estatura en metros: "))
IMC = peso/(altura**2)
print(f"Tu indice de masa corporal (IMC) es: {round(IMC,2)}")
