# Reto_9

1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
1) Programa (Función Lambda) para hallar el promedio de 5 números
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
2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

```python

```
3. Escriba una función recursiva para calcular la operación de la potencia.

```python

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

```
5. Crear cuenta en stackoverflow y adjuntar imagen en el repo

[![image.png](https://i.postimg.cc/6qkbCpNQ/image.png)](https://postimg.cc/JHQQLm0w)

6. Crear perfil en Linkedin

[![Captura-de-pantalla-2024-03-26-100033.png](https://i.postimg.cc/C1mzZRkj/Captura-de-pantalla-2024-03-26-100033.png)](https://postimg.cc/qh6kSMmR)
