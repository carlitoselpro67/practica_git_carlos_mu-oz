# =============================================================
# Portada
# =============================================================
# Nombre: Carlos Armando Muñoz Bustamante
# Matrícula: 2630017
# Grupo: IM-1-3

# =============================================================
# Resúmen Ejecutivo
# =============================================================
# Los enteros representan números completos, incluyendo el cero,
# los números positivos y los números negativos.
# Los números flotantes representan números que pueden tener
# una parte entera y una parte decimal.
# Un booleano es un tipo de dato que puede tener dos valores:
# True o False. Se obtiene mediante comparaciones usando operadores
# como >, <, == y !=. Validar rangos garantiza que los datos
# se mantengan dentro de los límites permitidos. Evitar la división
# entre cero es importante porque provoca un ZeroDivisionError,
# que puede interrumpir la ejecución del programa.
# Este documento abarcará: la descripción de cada problema, el diseño de entradas y salidas,
#  las validaciones aplicadas y el uso de enteros, 
# números flotantes y booleanos para tomar decisiones.

# =============================================================
# Principios y buenas prácticas
# =============================================================
# Usar tipos apropiados: int para contadores y float para valores decimales.
# Evitar repetir expresiones complejas almacenando resultados intermedios en variables.
# Validar los datos antes de realizar operaciones, como comprobar que las horas
# y los salarios no sean negativos.
# Usar nombres de variables descriptivos y mensajes claros para el usuario.
# Documentar claramente qué significan True y False en cada contexto.

# =============================================================
# Problem 1: Temperature converter and range flag
# =============================================================
# Description:
# Convierte una temperatura de Celsius a Fahrenheit y determina mediante un booleano 
# (True o False) si la temperatura está dentro del rango establecido.
# Inputs:
# - temp_c (float; temperatura en °C).
# - "Fahrenheit:" <temp_f>
# - "Kelvin:" <temp_k>
# - "High temperature:" true|false
# Outputs:
# Temperatura en Fahrenheit, temperatura en Kelvin y un indicador
# booleano que señala si la temperatura es alta.

# Validations:
# Comprobar que las entradas sean numéricas.
# Verificar que la temperatura esté dentro del rango permitido.
# Comprobar que la temperatura mínima no sea mayor que la máxima.
# Test cases:
# Test Cases:
# 1. Normal: Input: 25
#   Expected Output: Fahrenheit: 77.0, Kelvin: 298.15, High temperature: false
# 2. Border: Input: 30
#   Expected Output: Fahrenheit: 86.0, Kelvin: 303.15, High temperature: true
# 3. Error: Input: "hola"
#   Expected Output: Error: invalid input

print("Problem 1: Temperature converter and range flag")
temp_c_text = input("Enter temperature in Celsius: ")

try:  # try intenta ejecutar una operación que podría fallar
    temp_c = float(temp_c_text)

    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15

    if temp_k < 0:
        print("Error invalid temperature")
    else:
        is_high_temperature = temp_c >= 30.0

        print(f"Fahrenheit: {temp_f}")
        print(f"Kelvin: {temp_k}")
        print(f"High temperature: {str(is_high_temperature).lower()}")

except ValueError: # Marcará error si el resultado no es un número
    print("Error: invalid input")


# =============================================================
# Problem 2: Work hours and overtime payment
# =============================================================
# Description:
# Calcula el salario total de un trabajador 
# según las horas trabajadas y su pago por hora.
# Inputs:
# - Hours_worked (float): total de horas trabajadas.
# - Hourly_rate (float): pago normal por hora.
# Outputs:
# -Regular pay: pago por las primeras 40 horas o menos.
# -Overtime pay: pago por las horas extra.
# -Total pay: suma de ambos pagos.
# Validations:
# Comprobar que las entradas sean números.
# Verificar que las horas trabajadas no sean negativas.
# Verificar que el pago por hora no sea negativo.
# Test case:
# 1. Normal: Input: Hours: 45, Rate: 100
#   Expected Output: Regular pay: 4000.0, Overtime pay: 750.0, Total pay: 4750.0
# 2. Border: Input: Hours: 40, Rate: 100
#   Expected Output: Regular pay: 4000.0, Overtime pay: 0.0, Total pay: 4000.0
# 3. Error: Input: Hours: "hello", Rate: 100
#   Expected Output: Error: invalid input

print("Problem 2: Work Hours and Overtime Payment")

hours_text = input("Enter hours worked: ")
rate_text = input("Enter hourly rate: ")

try:
    hours = float(hours_text)
    rate = float(rate_text)

    if hours < 0 or rate < 0:
        print("Error: values cannot be negative")
    else:
        regular_hours = min(hours, 40) # toma el valor menor entre las horas trabajadas y 40.
        overtime_hours = max(hours - 40, 0) # toma el valor mayor entre las horas que exceden 40 y cero.

        regular_pay = regular_hours * rate
        overtime_pay = overtime_hours * rate * 1.5
        total_pay = regular_pay + overtime_pay

        print(f"Regular pay: {regular_pay}")
        print(f"Overtime pay: {overtime_pay}")
        print(f"Total pay: {total_pay}")

except ValueError:
    print("Error: invalid input")

# =============================================================
# Problem 3: Discount eligibility with booleans
# =============================================================
# Description:
# Determina si un cliente califica para un descuento 
# según si es miembro y cuánto dinero ha gastado.
# Inputs: 
# - is_member (boolean): indica si el cliente es miembro.
# - total_spent (float): cantidad total gastada.
# Outputs:
# - Discount eligible: True o False.
# Validations:
# Comprobar que el gasto sea un número.
# Verificar que el gasto no sea negativo.
# Comprobar que la membresía sea válida (True o False).
# Test case:
# 1. Normal: Input: Age: 30, Purchase: 1500
#   Expected Output: Senior customer: false, Large purchase: true, Gets discount: true
# 2. Border: Input: Age: 60, Purchase: 500
#   Expected Output: Senior customer: true, Large purchase: false, Gets discount: true
# 3. Error: Input: Age: "hello", Purchase: 500
#   Expected Output: Error: invalid input

print("Problem 3: Discount eligibility with booleans")
age_text = input("Enter your age: ")
purchase_text = input("Enter purchase amount: ")

try: 
    age = int(age_text)
    purchase = float(purchase_text)

    if age < 0 or purchase < 0:
        print("Error: value cannot be negative")
    else: 
        is_senior = age >= 60
        is_large_purchase = purchase >= 1000
        gets_discount = is_senior or is_large_purchase

        print(f"Senior coustomer: {str(is_senior).lower()}")
        print(f"Large purchase: {str(is_large_purchase).lower()}")
        print(f"Gets discount: {str(gets_discount).lower()}")

except ValueError:
    print("Error: invalid input")

# =============================================================
# Problem 4: Basic statistics of three integers
# =============================================================
# Description:
# Lee tres números enteros y calcula 
# su suma, promedio, valor mínimo y valor máximo.
# Inputs: 
# - num1 (int): primer número.
# - num2 (int): segundo número.
# - num3 (int): tercer número.
# Outputs:
# - sum: suma de los tres números.
# - average: promedio de los tres números.
# - minimum: número menor.
# - maximum: número mayor.
# Validations: 
# Comprobar que las tres entradas sean números enteros.
# Permitir números positivos, negativos y cero.
# Mostrar un error si alguna entrada no es un entero válido.
# Test cases:
# 1. Normal: Input: 4, 8, 12
#   Expected Output: Sum: 24, Average: 8.0, Smallest: 4, Largest: 12, Difference: 8
# 2. Border: Input: 5, 5, 5
#   Expected Output: Sum: 15, Average: 5.0, Smallest: 5, Largest: 5, Difference: 0
# 3. Error: Input: "hello", 5, 8
#   Expected Output: Error: invalid input

print("Problem 4: Basic statistics of three integers")
num_1_text = input("Enter the first integer: ")
num_2_text = input("Enter the second integer: ")
num_3_text = input("Enter the third integer: ")
num_4_text = input("Enter the fourth integer: ")

try:
    num1 = int(num_1_text)
    num2 = int(num_2_text)
    num3 = int(num_3_text)
    num4 = int(num_4_text)

    total = num1 + num2 + num3 + num4
    average = total / 4
    smallest = min(num1, num2, num3, num4) # min() busca el número más pequeño
    largest = max(num1, num2, num3, num4) # max() busca el número más grande
    difference = abs(largest - smallest) # abs() elimina el signo negativo

    print(f"Sum: {total}")
    print(f"Average: {round(average, 2)}") # round() redondea
    print(f"Smallest: {smallest}")
    print(f"Largest: {largest}")
    print(f"Diference: {difference}")

except ValueError:
    print("Error: invalid input")

# =============================================================
# Problem 5: Loan eligibility (income and debt ratio)
# =============================================================
# Description:
# Calcula la proporción entre las deudas mensuales y los ingresos mensuales
# para determinar si una persona cumple con los criterios establecidos para 
# obtener un préstamo.
# Inputs: 
# - monthly_income (float): ingresos mensuales.
# - monthly_debt (float): pagos mensuales de deudas.
# Outputs:
# - Debt ratio: porcentaje de deuda respecto a los ingresos.
# - Loan eligible: True o False, según los criterios definidos.
# Validations:
# Comprobar que los ingresos y las deudas sean números.
# Verificar que los ingresos sean mayores que cero para evitar división entre cero.
# Verificar que las deudas no sean negativas.
# Test cases:
# 1. Normal: Input: Income: 20000, Debt: 5000
#   Expected Output: Debt ratio: 25.0%, Sufficient income: true, Acceptable debt: true, Loan eligible: true
# 2. Border: Input: Income: 10000, Debt: 3500
#   Expected Output: Debt ratio: 35.0%, Sufficient income: true, Acceptable debt: true, Loan eligible: true
# 3. Error: Input: Income: "hello", Debt: 2000
#   Expected Output: Error: invalid input

print("Problem 5: Loan Eligibility")

income_text = input("Enter monthly income: ")
debt_text = input("Enter monthly debt payments: ")

try: 
    income = float(income_text)
    debt = float(debt_text)

    if income <= 0 or debt <= 0:
        print("Error: income must be positive and debt cannot be negative")
    else: 
        debt_ratio = debt / income
        is_income_sufficient = income >= 10000
        is_debt_aceptable = debt_ratio <= 0.35
        loan_eligible = is_income_sufficient and is_debt_aceptable # las condiciones deben ser verdaderas para que el resultado sea "True"

        print(f"Debt ratio: {round(debt_ratio * 100, 2)}%")
        print(f"Sufficient income: {str(is_income_sufficient).lower()}")
        print(f"Acceptable debt: {str(is_debt_aceptable).lower()}")
        print(f"Loan eligible: {str(loan_eligible).lower()}")

except ValueError:
    print("Error: invalid input")

# =============================================================
# Problem 6: Body Mass Index (BMI) and category flag
# =============================================================
# Description:
# Calcula el IMC usando el peso y la estatura de una persona, y asigna una categoría: 
# bajo peso, peso saludable, sobrepeso u obesidad.
# Inputs: 
# - weight (float): peso en kilogramos.
# - height (float): estatura en metros.
# Outputs:
# - BMI: valor calculado del IMC.
# - Category: categoría correspondiente.
# - is_healthy_weight: booleano que indica si el IMC está entre 18.5 y 25.
# Validations:
# Comprobar que las entradas sean números.
# Verificar que el peso sea mayor que cero.
# Verificar que la estatura sea mayor que cero para evitar dividir entre cero.
# Test cases:
# 1. Normal: Input: Weight: 70, Height: 1.75
#   Expected Output: BMI: 22.86, Underweight: false, Normal weight: true, Overweight: false
# 2. Border: Input: Weight: 80, Height: 2.0
#   Expected Output: BMI: 20.0, Underweight: false, Normal weight: true, Overweight: false
# 3. Error: Input: Weight: "hello", Height: 1.75
#   Expected Output: Error: invalid input

print("Problem 6: BMI and category flag")
weight_text = input("Enter weight in Kg: ")
height_text = input("Enter height in Mts.: ")

try: 
    weight = float(weight_text)
    height = float(height_text)

    if weight < 0 or height < 0:
        print("Error: weight and height must be positive")
    else:
        bmi = weight / (height ** 2) # ** 2 eleva la altura la cuadrado
        is_underweight = bmi < 18.5
        is_normalweigth = 18.5 <= bmi < 25
        is_overweight = bmi > 25

        print(f"BMI: {round(bmi, 2)}")

except ValueError:
    print("Error: invalid input")

# =============================================================
# Conclusiones 
# =============================================================
# En conclusión los int y floats se usan juntos para hacer cálculos con números
# enteros y decimales. Las comparaciones permiten obtener True o False dependiendo
# de los valores. Con el if podemos tomar decisiones según se cumplan o no ciertas
# condiciones.
# Es importante validar los rangos para así comprobar que los datos sean correctos.
# También hay que evitar dividir entre cero porque puede causar errores en el programa.
# Supe que and, or y not sirven para combinar condiciones de diferentes maneras.
# Estas condiciones ayudan a que el programa tome decisiones según los datos puestos.

# =============================================================
# Referencias
# ============================================================
# Python Built-in Functions
# https://docs.python.org/3/library/functions.html

# Python Expressions
# https://docs.python.org/3.13/reference/expressions.html

# Python Built-in Types
# https://docs.python.org/3/library/stdtypes.html

# Python Errors and Exceptions
# https://docs.python.org/3/tutorial/errors.html

# Numeric Types: int, float, complex and bool
# https://elpythonista.com/tipos-numericos-int-float-complex-bool

# U.S. Department of Labor: Overtime
# https://www.dol.gov/general/topic/workhours/overtime

# Consumer Financial Protection Bureau: Debt-to-Income Ratio
# https://www.consumerfinance.gov/ask-cfpb/what-is-a-debt-to-income-ratio-en-1791/

# Centers for Disease Control and Prevention: Adult BMI Categories
# https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html

# Centers for Disease Control and Prevention: Calculating BMI
# https://www.cdc.gov/growth-chart-training/hcp/using-bmi/calculating-bmi.html
