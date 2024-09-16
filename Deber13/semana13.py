# Definición de la función que calcula el promedio de temperaturas para cada ciudad
print("UEA\nPatrick Luna\nDeber semana 13 temperaturas" )

def calcular_promedio_ciudad(temperaturas, ciudades):
    promedios_ciudades = {}

    # Iteramos sobre cada ciudad usando el índice y los datos de temperaturas
    for ciudad_es, ciudad in enumerate(temperaturas):
        total_temp = 0
        num_dias = 0

        # Dentro de cada ciudad, iteramos sobre las semanas
        for semana in ciudad:
            # Sumamos las temperaturas de cada día en la semana
            total_temp += sum([dia["temp"] for dia in semana])
            # Contamos el número de días en esa semana
            num_dias += len(semana)

        # Calculamos el promedio de la ciudad
        promedio = total_temp / num_dias
        # Almacenamos el promedio en un diccionario con el nombre de la ciudad
        promedios_ciudades[ciudades[ciudad_es]] = promedio

    # Retornamos el diccionario con los promedios por ciudad
    return promedios_ciudades

# Datos de ejemplo, reutilizando la estructura anterior
temperaturas = [
    # Ciudad 1 - Quito
    [
        [{"dia": "Lunes", "temp": 19}, {"dia": "Martes", "temp": 19}, {"dia": "Miércoles", "temp": 20},
         {"dia": "Jueves", "temp": 18}, {"dia": "Viernes", "temp": 23}, {"dia": "Sábado", "temp": 22},
         {"dia": "Domingo", "temp": 19}],
        [{"dia": "Lunes", "temp": 20}, {"dia": "Martes", "temp": 22}, {"dia": "Miércoles", "temp": 19},
         {"dia": "Jueves", "temp": 19}, {"dia": "Viernes", "temp": 20}, {"dia": "Sábado", "temp": 18},
         {"dia": "Domingo", "temp": 19}],
        [{"dia": "Lunes", "temp": 23}, {"dia": "Martes", "temp": 24}, {"dia": "Miércoles", "temp": 23},
         {"dia": "Jueves", "temp": 23}, {"dia": "Viernes", "temp": 22}, {"dia": "Sábado", "temp": 20},
         {"dia": "Domingo", "temp": 14}],
        [{"dia": "Lunes", "temp": 13}, {"dia": "Martes", "temp": 18}, {"dia": "Miércoles", "temp": 18},
         {"dia": "Jueves", "temp": 22}, {"dia": "Viernes", "temp": 23}, {"dia": "Sábado", "temp": 23},
         {"dia": "Domingo", "temp": 21}]
    ],
    # Ciudad 2 - Sevilla
    [
        [{"dia": "Lunes", "temp": 35}, {"dia": "Martes", "temp": 35}, {"dia": "Miércoles", "temp": 35},
         {"dia": "Jueves", "temp": 36}, {"dia": "Viernes", "temp": 35}, {"dia": "Sábado", "temp": 34},
         {"dia": "Domingo", "temp": 36}],
        [{"dia": "Lunes", "temp": 34}, {"dia": "Martes", "temp": 34}, {"dia": "Miércoles", "temp": 32},
         {"dia": "Jueves", "temp": 32}, {"dia": "Viernes", "temp": 32}, {"dia": "Sábado", "temp": 31},
         {"dia": "Domingo", "temp": 35}],
        [{"dia": "Lunes", "temp": 36}, {"dia": "Martes", "temp": 32}, {"dia": "Miércoles", "temp": 30},
         {"dia": "Jueves", "temp": 30}, {"dia": "Viernes", "temp": 28}, {"dia": "Sábado", "temp": 27},
         {"dia": "Domingo", "temp": 27}],
        [{"dia": "Lunes", "temp": 28}, {"dia": "Martes", "temp": 29}, {"dia": "Miércoles", "temp": 30},
         {"dia": "Jueves", "temp": 28}, {"dia": "Viernes", "temp": 33}, {"dia": "Sábado", "temp": 35},
         {"dia": "Domingo", "temp": 36}]
    ],
    # Ciudad 3 - New York
    [
        [{"dia": "Lunes", "temp": 25}, {"dia": "Martes", "temp": 26}, {"dia": "Miércoles", "temp": 27},
         {"dia": "Jueves", "temp": 29}, {"dia": "Viernes", "temp": 24}, {"dia": "Sábado", "temp": 25},
         {"dia": "Domingo", "temp": 26}],
        [{"dia": "Lunes", "temp": 27}, {"dia": "Martes", "temp": 26}, {"dia": "Miércoles", "temp": 27},
         {"dia": "Jueves", "temp": 26}, {"dia": "Viernes", "temp": 26}, {"dia": "Sábado", "temp": 25},
         {"dia": "Domingo", "temp": 26}],
        [{"dia": "Lunes", "temp": 28}, {"dia": "Martes", "temp": 23}, {"dia": "Miércoles", "temp": 24},
         {"dia": "Jueves", "temp": 22}, {"dia": "Viernes", "temp": 19}, {"dia": "Sábado", "temp": 26},
         {"dia": "Domingo", "temp": 22}],
        [{"dia": "Lunes", "temp": 24}, {"dia": "Martes", "temp": 27}, {"dia": "Miércoles", "temp": 24},
         {"dia": "Jueves", "temp": 22}, {"dia": "Viernes", "temp": 21}, {"dia": "Sábado", "temp": 28},
         {"dia": "Domingo", "temp": 32}]
    ]
]

# Nombres de las ciudades
ciudades = ["Quito", "Sevilla", "New York"]

# Llamamos a la función para obtener el promedio
promedios = calcular_promedio_ciudad(temperaturas, ciudades)
# Mostramos los resultados
for ciudad, promedio in promedios.items():
        # Mostramos el nombre de la ciudad,
        print(f"\nEn la ciudad de {ciudad}\nEl promedio de temperatura es {promedio:.2f}°C")
    # Imprimir línea separadora entre ciudades
        print("-" * 50)