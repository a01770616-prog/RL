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

def generar_datos():
    dias = [1, 2, 3, 4, 5]
    ventas = [100, 150, 200, 250, 300]
    return list(dias, ventas)

def resumen_analitica():
    dias,ventas = generar_datos()
    total = sum(ventas)
    promedio = total / len(ventas)

    return {
        "dias": dias,
        "ventas": ventas,
        "total": total,
        "promedio": promedio
    }

datos = resumen_analitica()
print("Total de ventas:", datos["total"])
print("Promedio de ventas:", datos["promedio"])
