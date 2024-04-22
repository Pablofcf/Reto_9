# Programa, calculo de promedio
if __name__=="__main__":
 # Declaramos las 5 variables
 a : float = float(input("Piense en un numero y digitelo: \n "))
 b : float = float(input("Digite un numero completo y seguido del dia, mes y año de su nacimiento\nejemplo, dia 19 mes 10 año 2005, numero resultante 19102005: \n "))
 c : float = float(input("Digite su edad sumando el año en el que estamos: \n "))
 d : float = float(input("Digite un numero re random: \n "))
 e : float = float(input("Preguntele a su amigo un numero mayor a 500 y escribalo: \n "))
 #Utilizamos la función Lambda
promedio = (lambda a,b,c,d,e:(a+b+c+d+e)/5)(a,b,c,d,e)
# Mostrar resultado funcion Anonima
print("El promedio de los números digitados es: ",promedio)
