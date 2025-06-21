# Importando a biblioteca math para operações matemáticas
import math

# introdução
print('"Fórmula de Bhaskara para o cálculo de raízes de polinômios de 2º grau"')
print('\n Uma equação de 2º grau tem a forma: ax² + bx +c = 0, em que o coeficiente "a" não pode ser nulo.')
print('Informe os coeficientes "a", "b" e "c" abaixo:')

# Imput e tratamento do coeficiente 'a' caso seja nulo, uma string ou outro tipo de dado inválido
while True:
    try:
        a = float(input('\n Digite o coeficiente "a": '))
        if a == 0:
            print('Coeficiente "a" precisa ser um número real e não-nulo.')
        else:
            break
    except ValueError:
        print('Coeficiente "a" precisa ser um número real e não-nulo.')
        a = float(input('Digite o coeficiente "a": '))

# Imput e tratamento dos coeficientes 'b' e 'c', garantindo que sejam números válidos
while True:
    try:
        b = float(input('\n Digite o coeficiente "b": '))
        break
    except ValueError:
        print('Coeficiente "b" precisa ser um número real.')

while True:
    try:
        c = float(input('\n Digite o coeficiente "c": '))
        break
    except ValueError:
        print('Coeficiente "c" precisa ser um número real.')

# Cálculo e exibição do discriminante (delta)
delta = b**2 - 4 * a * c
print(f'\n Discriminante (Δ) = {delta}')

# Cálculo das raízes
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'\n As raízes reais são:')
    print(f' x1 = {x1}')
    print(f' x2 = {x2}')
elif delta == 0:
    x = -b / (2 * a)
    print(f'\n A raiz real é:')
    print(f' x1 = x2 = {x}')
else:
    realPart = -b / (2 * a)
    imaginaryPart = math.sqrt(-delta) / (2 * a)
    print(f'\n As raízes complexas são:')
    print(f' x1 = {realPart} + {imaginaryPart}i')
    print(f' x2 = {realPart} - {imaginaryPart}i')

# Mensagem de conclusão
print('\n Cálculo concluído com sucesso!')
# Fim do programa
