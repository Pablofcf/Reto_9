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