import re  # Importar el módulo de expresiones regulares

s = 'calculateWeight.py'  # Source

def toCamelCase(word):
  parts = word.split('_')
  # Iniciar camelCaseWord con la primera parte en minúsculas
  camelCaseWord = parts[0].lower()
  # Iterar sobre las partes restantes para construir camelCaseWord
  for part in parts[1:]:
      camelCaseWord += part.capitalize()
  return camelCaseWord

def replaceWithCamelCase(match):
    word = match.group(0)  # La palabra completa que coincide con el patrón
    return toCamelCase(word)

with open(s, 'r') as file:
    content = file.read()

# Patrón para identificar palabras con guiones bajos
pattern = r'\b\w+(_\w+)+\b'

# Reemplazar todas las coincidencias del patrón en el contenido con su versión camelCase
formattedContent = re.sub(pattern, replaceWithCamelCase, content)

# Ahora 'formatted_content' contiene el texto con las palabras en camelCase, manteniendo el formato original
print(formattedContent)

# Abre un archivo llamado 'Readme.txt' en modo escritura ('w')
with open(s, 'w') as f:
    # Escribe el contenido JSON en el archivo
    f.write(formattedContent)