import math

print("=== Fórmula de Bhaskara para o cálculo de raízes de polinômios de 2º grau ===\n")
print("A equação do segundo grau tem a forma: ax² + bx + c = 0")
print("Informe os coeficientes abaixo:\n")

# Coletar os coeficientes da equação
# A entrada de 'a' deve ser verificada para garantir que não seja zero
while True:
    try:
        a = float(input("Digite o coeficiente a (não pode ser nulo): "))
        if a == 0:
            print("Coeficiente 'a' precisa ser um número real e não-nulo.")
        else:
            break
    except ValueError:
        print("Coeficiente 'a' precisa ser um número real e não-nulo.")

# Para os coeficientes 'b' e 'c', garantimos que são números válidos
while True:
    try:
        b = float(input("Digite o coeficiente b: "))
        break
    except ValueError:
        print("Coeficiente 'b' precisa ser um número real.")

while True:
    try:
        c = float(input("Digite o coeficiente c: "))
        break
    except ValueError:
        print("Coeficiente 'c' precisa ser um número real.")

# Calculando o discriminante (delta)
delta = b**2 - 4 * a * c
print(f"Discriminante (Δ) = {delta}")

# Calculando as raízes
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"As raízes reais são:")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
elif delta == 0:
    x = -b / (2 * a)
    print(f"A raiz real é:")
    print(f"x1 = x2 = {x}")
else:
    realPart = -b / (2 * a)
    imaginaryPart = math.sqrt(-delta) / (2 * a)
    print(f"As raízes complexas são:")
    print(f"x1 = {realPart} + {imaginaryPart}i")
    print(f"x2 = {realPart} - {imaginaryPart}i")
