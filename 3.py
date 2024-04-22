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
