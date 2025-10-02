print("Hola a todos, este es un repositorio local y se desplegara en Github")

print("Este archivo se estará modificando")

for i in range(10):
    print(int)

def suma(a, b):
    return a + b
print(suma(5, 3))


def suma(a, b, c):
    print(a + b + c)
    suma()

import matplotlib.pyplot as plt

def graficar_ventas(dias,ventas):
    plt.figure(figsize=(10,5))
    plt.plot(dias, ventas,marker='o', linestyle='-',color='blue')
    plt.title('Gráfica de Ventas diarias')
    plt.xlabel('Días')
    plt.ylabel('Ventas')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main_frontend():
    dias = [1, 2, 3, 4, 5, 6, 7]
    ventas = [150, 200, 250, 300, 350, 400, 450]
    graficar_ventas(dias, ventas)   

main_frontend()