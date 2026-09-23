#PUNTO 1
identificador = "COL-001"
nombre = "Moneda Antigua
precio = 1500.50
cantidad = 3
disponible = True
categorias_unicas = {"Arte", "Monedas"}


# Punto 2
entrada_nombre = input("Ingrese el nombre de la pieza: ")
entrada_precio = input("Ingrese el precio de la pieza: ")


# Punto 3
precio_numerico = float(entrada_precio)
cantidad_numerica = int("5")



# Punto 4
print(type(identificador))
print(type(precio_numerico))





#Punto 5
texto_sucio = "   figura coleccionable usada   "

# Quitar espacios en blanco a los lados (.strip())
texto_limpio = texto_sucio.strip()

# Convertir formatos de mayúsculas/minúsculas
en_mayusculas = texto_limpio.upper()
en_minusculas = texto_limpio.lower()
en_titulo = texto_limpio.title()

# Reemplazar palabras (.replace())
texto_modificado = texto_limpio.replace("usada", "certificada")

# Separar una cadena por comas
etiquetas = "retro,anime,edicion_limitada".split(",")

# Concatenación e Interpolación
concatenado = "Pieza: " + texto_limpio + " - Precio: " + str(precio)
interpolado = f"Pieza: {texto_limpio} - Precio: ${precio:.2f}"
