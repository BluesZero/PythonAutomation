# Importa las bibliotecas necesarias
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# Inicializa una sesión HTML con requests_html
s = HTMLSession()

# Define la URL de la página de Amazon a la que deseas acceder
url = 'https://www.amazon.com.mx/s?k=pokemon&__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=YXI14EYAM1OX&qid=1698731724&sprefix=pokemon+%2Caps%2C98&ref=sr_pg_1'

# Abre un archivo de texto para escribir los resultados
outputFile = open('resultados_amazon.txt', 'w', encoding='utf-8')

# Función para obtener el contenido HTML de una URL
def getData(url):
    r = s.get(url)
    r.html.render(sleep=1)  # Renderiza la página (espera 1 segundo para cargar JavaScript)
    soup = BeautifulSoup(r.html.html, 'html.parser')  # Parsea el HTML con BeautifulSoup
    return soup

# Función para obtener la URL de la siguiente página de resultados
def getNextPage(soup):
    # Esto buscará la sección de paginación en la página
    pages = soup.find('ul', {'class': 'a-pagination'})

    if pages is not None:  # Comprueba si se encontró la sección de paginación
        # Comprueba si hay una página siguiente ('a-last') o si estamos en la última página
        if not pages.find('li', {'class': 'a-disabled a-last'}):
            url = 'https://www.amazon.com.mx' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
            return url  # Devuelve la URL de la siguiente página

    return None  # No se encontró la sección de paginación o no hay más páginas, devuelve None

# Función para extraer y guardar los títulos, precios y enlaces de los productos en el archivo
def extractAndSaveResults(soup):
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    for product in products:
        title = product.find('h2').text
        price = product.find('span', {'class': 'a-price-whole'}).text
        link = 'https://www.amazon.com.mx' + product.find('a', {'class': 'a-link-normal'})['href']
        resultText = f"Título del producto: {title}\nPrecio: {price}\nEnlace al producto: {link}\n\n"
        outputFile.write(resultText)

# Bucle principal para recorrer todas las páginas de resultados
while True:
    data = getData(url)  # Obtiene el contenido HTML de la URL actual
    extractAndSaveResults(data)  # Extrae y guarda los resultados de la página actual
    url = getNextPage(data)  # Obtiene la URL de la siguiente página
    if not url:  # Si no hay más páginas, sal del bucle
        break

# Cierra el archivo de resultados
outputFile.close()
