Explicacion del proyecto:
Lector de facturas

1. Las Librerías (Los Ingredientes)
logging: Se usa para rastrear eventos. En lugar de solo usar print, esto permite generar mensajes estructurados que indican qué está pasando en el programa (informativos, errores, etc.).

pytesseract: Es la "voz" del código. Es una interfaz para Tesseract OCR (un motor de Google) que permite a Python "leer" imágenes.

PIL (Image): Proviene de la librería Pillow. Sirve para abrir y manipular los archivos de imagen (JPG, PNG, etc.) antes de pasárselos al lector.

2. La Clase FacturaOCR (El Cerebro)
El código utiliza Programación Orientada a Objetos para organizar la tarea.

El método __init__ (Configuración)
Cuando creas el objeto ocr = FacturaOCR(), pasan dos cosas:

Configura el Logger: Crea un sistema de anuncios interno que dice: "Hola, soy la clase FacturaOCR y te voy a informar qué estoy haciendo".

Ruta de Tesseract: Define dónde está instalado el motor Tesseract en tu computadora (C:/Program Files/...).

Nota importante: Aunque está definida en el código, falta una línea para que pytesseract realmente use esa ruta (debería ser pytesseract.pytesseract.tesseract_cmd = ...).

El método extraer_texto (La Acción)
Este es el corazón del script:

Image.open(ruta_imagen): Abre el archivo de la factura.

image_to_string: Aquí ocurre la magia. Toma la imagen y usa el parámetro lang="spa" para indicarle que busque caracteres y palabras en español (útil para detectar eñes o acentos).

Return: Devuelve todo el texto encontrado como una sola cadena de texto (str).

3. Bloque de Ejecución (if __name__ == "__main__":)
Este bloque solo corre si ejecutas el archivo directamente.

logging.basicConfig: Configura cómo se verán los mensajes de registro (con fecha, hora y nivel de importancia).

Instanciación: Crea una "máquina" de leer facturas (ocr = FacturaOCR()).

Procesamiento: Busca una imagen llamada factura.jpeg, extrae el texto y lo imprime en tu pantalla.

Aspectos importantes a considerar la importancia de un lector de facturas:

1. Automatización y Ahorro de Tiempo
La razón más obvia es la eficiencia. Digitar manualmente los datos de una factura (NIF, base imponible, IVA, fecha) toma minutos por cada documento.

Antes: Un empleado pasa horas pasando datos a un Excel.

Ahora: El código procesa cientos de facturas en segundos.

2. Reducción del Error Humano
Cuando una persona está cansada, es fácil que confunda un 8 con un B, o que mueva una coma decimal. En contabilidad, un error de un solo dígito puede causar problemas graves con el fisco o descuadres bancarios. El OCR, una vez calibrado, mantiene una precisión constante.

3. Digitalización y Buscabilidad
Si tienes mil facturas en papel o en fotos desordenadas, encontrar cuánto pagaste de electricidad en marzo de 2023 es una pesadilla. Al extraer el texto:

Puedes convertir la información en una base de datos.

Puedes hacer búsquedas por palabras clave (ej: buscar "Endesa" o "Mantenimiento").

4. Escalabilidad del Negocio
Si tu empresa recibe 10 facturas al mes, puedes hacerlo a mano. Si recibe 1,000, necesitas un sistema como este. Este proyecto es la base para crear un sistema de gestión empresarial (ERP) o una app de finanzas personales que categoriza gastos automáticamente.

¿Cómo encaja el flujo de este proyecto?
Captura: Tomas la foto

Procesamiento: El motor "entiende" los caracteres (lo que hace pytesseract).

Salida: Obtienes texto digital listo para ser analizado o guardado.