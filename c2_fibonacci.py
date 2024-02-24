# # Factorial from number
# def factorial_number(number):
#     if number == 0:
#         return 1
#     return number*factorial_number(number-1)

# print(factorial_number(5))

# # fibonacci for loop
# def fibo_for(number):
#     fibo = [0,1]
    
#     for i  in range(2,number+1):
#         fibo.append(fibo[i-1]+fibo[i-2])
#     return fibo

# print(fibo_for(10))


#  * Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
#  * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
#  * 0, 1, 1, 2, 3, 5, 8, 13...

def fibo_number(n):
    if n <= 1:
        return n
    return fibo_number(n-1) + fibo_number(n-2)

# fix...  last number is none
def fibonacci(n: int):
    for i in range(n):
        print(fibo_number(i))  



