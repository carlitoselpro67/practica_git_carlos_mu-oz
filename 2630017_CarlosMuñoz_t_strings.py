# =============================================================
# Portada
# =============================================================
# Nombre: Carlos Armando Muñoz Bustamante
# Matrícula: 2630017
# Grupo: IM-1-3

# =============================================================
# Resúmen Ejecutivo
# =============================================================
# Un string en Python son tipos de datos compuestos por secuencias
# de caracteres que representan texto. Son de tipo str y es inmutable.
# Esto quiere decir que no se pueden modificar directamente despues de crearlo
# Sus operaciones básicas son: concatenar textos (+), repetir (*),
# indicar el número de elementos de un objeto (len()), reemplazar texto (replace()),
# buscar texto (find()), etc.
# Es importante validar y normalizar el texto de entrada para evitar escribir
# espacios extra, mezclar mayúsculas y minúsculas, o caracteres especiales 
# que puedan afectar el procesamiento del texto.
# Este documento cubrirá seis problemas: formateador de nombres, 
# validador de correos, detector de palíndromos, estadísticas de palabras, 
# clasificador de contraseñas y formateador de etiquetas. 
# Cada uno incluye descripción, entradas,
# salidas, validaciones, tres casos de prueba y el código.

# =============================================================
# Principios y buenas prácticas
# =============================================================
# Los strings son inmutables: cualquier cambio genera una nueva cadena.
# Es buena práctica normalizar entrada con strip() y lower() antes de compararla.
# Evitar "números mágicos" en índices; documentar qué extrae cada slice.
# Usar métodos de string en lugar de reescribir lógica básica.
# Diseñar validaciones claras: primero que no esté vacío, luego el formato.
# Escribir código legible: nombres de variables claros y mensajes de error entendibles.

# =============================================================
# Problem 1: Full name formatter (name + initials)
# =============================================================
# Description:
# This program formats a person's full name using title case.
# It also extracts and displays the initials of each word in the name.
# Inputs:
# full_name (str): The full name of the person.
# Outputs:
# formatted_name (str): The full name in title case.
# initials (str): <X.X.X>  
# Validations:
# - The input must not be empty after using strip().
# - The name must contain at least two words (first and last name).
# - Inputs containing only spaces must be rejected.
# Test Cases:
# 1. Normal: Input: "carlos muñoz bustamante"
#   Expected Output: "Carlos Muñoz Bustamante", Initials: "C.M.B"
# 2. Border: Input: " CARLOS muñoz "
#   Expected Output: "Carlos Muñoz", Initials: "C.M."
# 3. Error: Input: "   "
#   Expected Output: Error message indicating that the input is invalid.

print("Problem 1: Full name formatter")
full_name = input("Enter your full name: ")

clean_name = " ".join(full_name.strip().split()) 
name_words = clean_name.split()

if clean_name == "" or len(name_words) < 2:
    print("Error: Please enter at least a first and last name.")

else:
    formatted_name = clean_name.title()
    initials = "" 

    for word in name_words:
        initials += word[0].upper() + "."

    print(f"Formatted Name: {formatted_name}")
    print(f"Initials: {initials}")


# =============================================================
# Problem 2: Simple email validator (structure + domain)
# =============================================================
# Description: 
# program that checks whether an email address follows basic formatting rules 
# - Checks whether an email address follows a basic format.
# - Verifies that the email contains a username, an @ symbol, and a domain.
# - Identifies email addresses that do not meet the required conditions.
# Inputs:
# email: A string entered by the user containing an email address.
# Outputs:
# valid email: if the email meets the basic validation rules, False otherwise.
# Invalid email: If the email does not meet the rules.
# Validations:
# -The email cannot be empty.
# -It must contain exactly one @ symbol.
# -It must contain text before and after the @.
# -The domain must contain a dot (.) followed by text.
# Test Cases: 
# 1. Normal: Input: "carlosmuñoz@gmail.com"
#   Expected Output: "Valid email"
# 2. Border: Input: "c@gmail.com"
#   Expected Output: "Valid email"
# 3. Error: Input: "carlosmuñoz@gmail" or "carlosmuñoz@@gmail.com"
#  Expected Output: "Invalid email"

print("\nProblem 2: Simple email validator")
email = input("Enter your email address: ").strip()

if email == "" or email.count("@") != 1: 
    print("Invalid email")
else:
    username, domain = email.split("@")
    if username == "" or "." not in domain: # comprueba que haya un punto en el dominio
        print("Invalid email")
    elif domain.startswith(".") or domain.endswith("."): # comprueba si el dominio empieza o termina con un punto
        print("Invalid email")
    else:
        print("Valid email")

# =============================================================
# Problem 3: Palindrome checker (ignoring spaces and case)
# =============================================================
# Description: Program that determines whether a word or phrase reads 
# the same forward and backward, ignoring spaces and uppercase or lowercase 
# differences.
# -Checks whether a word or phrase is a palindrome.
# -Ignores spaces and differences between uppercase and lowercase letters.
# -Compares the text with its reversed version.
# Inputs:
# text: A string entered by the user containing a word or phrase.
# Outputs:
# Palindrome: If the text read the same forward and backward.
# Not a palindrome: if the text is different when reversed.
# Validations:
# -The input cannot be empty.
# -Space must be ignored during comparison.
# -Uppercase and lowercase differences must be ignored
# Test Cases:
# 1. Normal: Input: "Anita lava la tina"
#   Expected Output: "Palindrome"
# 2. Border: Input: "A man a plan a canal Panama"
#   Expected Output: "Palindrome" 
# 3. Error: Input: "Hello world"
#   Expected Output: "Not a palindrome"

print("\nProblem 3: Palindrome checker")
text = input("Enter a word or phrase: ").strip()
clean_text = text.replace(" ", "").lower() # "anita lava la tina" a "anitalavalatina"

if clean_text == "":
    print("Error: empty input")
elif clean_text == clean_text[::-1]: # invierte el texto
    print("Palindrome")
else:
    print("Not a palindrome") 

# =============================================================
# Problem 4: Sentence word stats (lengths and first/last word)
# =============================================================
# Description: Program that analyzes a sentence and calculates
# basic information about its text.
# - Analyzes a sentence entered by the user.
# - Counts the total number of words and caracters in the sentence.
# - Displays basic statistics about the text.
# Inputs:
# sentence: A string entered by the user containing a sentence or text.
# Outputs:
# Word count: The total number of words in the sentence.
# Character count: The total number of characters in the sentence.
# Sentence count: The total number of sentences in the text.
# Validations:
# -The input cannot be empty.
# -Extra spaces should at the beginning and end be removed.
# Test Cases:
# 1. Normal: Input: "Hello world! This is a test."
#   Expected Output: Word count: 7, Character count: 31, Sentence count: 2
# 2. Border: Input: "   This is a test.   "
#   Expected Output: Word count: 4, Character count: 18, Sentence count: 1
# 3. Error: Input: "   "
#   Expected Output: Error message indicating that the input is invalid.

print("\nProblem 4: Sentence word stats")
sentence = input("Enter a sentence: ").strip()
if sentence == "":
    print("Error: empty input")
else:
    words = sentence.split()
    word_count = len(words)
    character_count = len(sentence)
    sentence_count = sentence.count(".") + sentence.count("!") + sentence.count("?") # cuenta los signos que norlmalmente terminan una oración.

    print(f"Word count: {word_count}")
    print(f"Character count: {character_count}")
    print(f"Sentence count: {sentence_count}")

# =============================================================
# Problem 5: Password strength classifier
# =============================================================
# Description: Program that evaluates the strength of a password based on
# certain criteria.
# - Evaluates its length and character variety.
# - Classifies the password as weak, medium, or strong.
# - Analyzes a password entered by the user.
# Inputs:
# password: A string entered by the user containing a password.
# Outputs:
# Weak: If the password is short and has little character variety.
# Medium: If the password meets some strength requirements 
# Strong: If the password meets most or all of the defined requierements.
# Validations:
# -The password cannot be empty.
# -Check the password length 
# -Check whether it contains uppercase letters.
# -Check whether it contains lowercase letters.
# -Check whether it contains numbers.
# -Check whether it contains special characters.
# Test Cases:
# 1. Normal: Input: "Pa$Sword1236-7#"
#   Expected Output: "Strong password"
# 2. Border: Input: "Password123"
#   Expected Output: "Medium password"
# 3. Error: Input: "pass"
#   Expected Output: "Weak password"

print("\nProblem 5: Password strength classifier")
password = input("Enter a password: ").strip()
if password == "":
    print("Error: empty password")
else:
    score = 0
    if len(password) >= 12:
        score += 1
    if any(char.isupper() for char in password): # char representa cada caracter de la contraseña 
        score += 1                               # isupper comprueba si el caracter es una mayúscula
    if any(char.islower() for char in password): # islower comprueba si el caracter es una minúscula
        score += 1
    if any(char.isdigit() for char in password): # isdigit verifica si el caracter es un dígito
        score += 1
    if any(not char.isalnum() for char in password): # isalnum verifica si el caracter es alfanumérico
        score += 1
    if score <= 2:
        print("Weak password")
    elif score <= 4:
        print("Medium password")
    else:
        print("Strong password")

# =============================================================
# Problem 6: Product label formatter (fixed-width text)
# =============================================================
# Description:program that formats a product name into a label 
# with a fixed length of 30 characters.
# - Receives a product name entered by the user.
# - Formats the product name into a label of exactly 30 characters.
# - Adds spaces when necessary to reach the required length.
# Inputs:
# product_name: A string entered by the user containing a product name.
# Outputs:
# formatted_label: The product name formatted to exactly 30 characters.
# Validations:
# -The product name cannot be empty.
# -Leading and trailing spaces should be removed.
# -If the product name is shorter than 30 characters, add spaces to reach 30.
# -If the product name is longer than 30 characters, truncate it to 30 characters.
# Test Cases:
# 1. Normal: "Wireless Mouse" -> Label with 30 characters.
# 2. Border: "A" -> Label with exactly 30 characters.
# 3. Error: "" -> Error: empty product name.

print("\nProblem 6: Product label formatter")
product_name = input("Enter a product name: ").strip()

if product_name == "":
    print("Error: empty product name")
else:
    label = product_name[:30].ljust(30) # esto es un slice que toma los primeros 30 caracteres como máximo.
    print(f"Formatted label: |{label}|")
    print(f"Label length: {len(label)}")

# =============================================================
# Conclusiones
# =============================================================
# En conclusión aprendí que trabajar con strings es importante para recibir,
# procesar, y mostrar datos correctamente. Los métodos como .join(), .lower(),
# .strip() y .split() nos permiten limpiar y organizar el texto según las 
# necesidades de nuestro programa. Normalizar el texto antes de compararlo
# sirve para evitar errores. Las validaciones son importantes porque impiden
# que se ingresen datos incorrectos. Aprendí que los strings son inmutables,
# o sea que no pueden ser modificados directamente, sino que se debe crear una 
# cadena nueva y los slices extraen partes específicas del texto indicando la
# posición inicial y final.

# =============================================================
# REFERENCIAS
# =============================================================

#Brugués, A. (s. f.). *Strings en Python*. Programa en Python. 
# https://www.programaenpython.com/fundamentos/strings-en-python/

#Python Software Foundation. (s. f.). *Tipos integrados*. Documentación de Python. 
# https://docs.python.org/es/3/builtins/stdtypes.html

#Mozilla. (s. f.). *`<input type="email">`*. MDN Web Docs. 
# https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email

#Python Software Foundation. (s. f.). *Built-in types*. Python documentation. 
# https://docs.python.org/3/builtins/stdtypes.html

#Python Software Foundation. (s. f.). *Input and output*. The Python Tutorial. 
# https://docs.python.org/3/tutorial/inputoutput.html
