# Reto_9

1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
   
1.1 Programa (Función Lambda) para hallar el promedio de 5 números
```python
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
```
1.2 Programa (Función Lambda) para calcular el peso de n animales (gallinas, gallos y pollitos)
```python
'''cantidad de carne de aves en kilos si se tienen N gallinas,
M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
'''
if __name__ == "__main__":
# nombramos las variables
 n: float= float(int(input("Cantidad de gallinas: ")))
 m: float= float(int(input("Cantidad de gallos: ")))
 k: float= float(int(input("Cantidad de pollitos: ")))
 #Utilizamos función lambda
 #Suponemos que una gallina pesa 6kg, un gallo 7kg y un pollito 1kg
masa=(lambda n,m,k:(n*6)+(m*7)+(k*1))(n,m,k)
print("El peso de ",n, "gallinas, ",m, "gallos y ",k, "pollitos es de ",masa, "kilos")
```
1.3 Programa (Función Lambda) para 
```python
#Calcular una función Racional
if __name__ == "__main__":
 #Nombramos las variables
 z = float(input("Digite un número: "))
 #Utilizamos la función lambda
 fx= (lambda z : z/(z**(1/3)-1))(z)
 #Mostrar resultado
 print("El resultado de su funcion F(x) es: ",fx)
```
2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

```python

```
3. Escriba una función recursiva para calcular la operación de la potencia.

```python
'''función recursiva para la potencia de un número
creamos una función'''
def potencia(num1,num2):
    '''Ordenamos al programa restricciones para seguir operando
    si el exponente es 0 o 1 el resultado es inmediato,
    sin embargo si es diferente de estos, se le debera restar 1'''
    if num2 ==0:
        return 1
    elif num1 == 0:
        return 0
    elif num2==1:
        return num1
    else:
        return num1 * potencia(num1, num2-1)
   
if __name__=="__main__":
    num1=float(input("Digite numero 1: "))
    num2=float(input("Digite numero 2: "))
    print("Su numero es: "+str(potencia(num1,num2)))
```
4. Utilice la siguiente plantilla de code para contar el tiempo:
```python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```
Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.

```python
#Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.
import time
def funcion_recursiva_fibonacci(Número = "")->float:
    if Número <= 1:
        return Número
    else:
        return funcion_recursiva_fibonacci(Número - 1) + funcion_recursiva_fibonacci(Número - 2)
def fibonacci_tiempo()->float:
    bandera_10 = False
    Número = 1
    while True:
        start_time = time.time() 
        funcion_recursiva_fibonacci(Número) 
        end_time = time.time() 
        timer = end_time - start_time
        Número += 1
        print(f"El tiempo entre el número {Número - 1} y el {Número} de la serie de Fibonacci es: {timer} ")
        # Si tarda más de 5 segundos la bandera se activa y se detiene el bucle while
        if timer >= 5 and bandera_10 == False:
            bandera_10 = True
            break
if __name__ == "__main__":
    print("inicio el programa")
    fibonacci_tiempo() 
```
[![Captura-de-pantalla-2024-04-22-092200.png](https://i.postimg.cc/MT9HThYg/Captura-de-pantalla-2024-04-22-092200.png)](https://postimg.cc/0MJPXXFC)

5. Crear cuenta en stackoverflow y adjuntar imagen en el repo

[![image.png](https://i.postimg.cc/6qkbCpNQ/image.png)](https://postimg.cc/JHQQLm0w)

6. Crear perfil en Linkedin

[![Captura-de-pantalla-2024-03-26-100033.png](https://i.postimg.cc/C1mzZRkj/Captura-de-pantalla-2024-03-26-100033.png)](https://postimg.cc/qh6kSMmR)
