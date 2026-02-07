#  FacturaOCR - Extractor de Texto

Este proyecto es una herramienta sencilla y eficiente escrita en **Python** para realizar **OCR (Reconocimiento Óptico de Caracteres)** en imágenes de facturas o documentos. Utiliza el motor de Tesseract para transformar imágenes en texto editable de forma automatizada.

## Caracteristicas
- **Validacion de Archivos:** Comprueba la existencia del archivo antes de procesar.
- **Soporte de Idioma:** Configurado especificamente para detectar caracteres en español (`spa`).
- **Manejo de Errores:** Incluye bloques `try-except` para capturar fallos críticos durante el procesamiento.
- **Interfaz de Consola:** Facil de usar mediante argumentos de línea de comandos.

##  Requisitos Previos

Antes de ejecutar el script, asegurate de tener instalado lo siguiente:

1.  **Python 3.x**
2.  **Tesseract OCR Engine:** - Descargalo para Windows [aqui](https://github.com/UB-Mannheim/tesseract/wiki).
    - **Nota:** El script apunta por defecto a `C:\Program Files\Tesseract-OCR\tesseract.exe`.
3.  **Librerias de Python:**
    ```bash
    pip install pytesseract Pillow
    ```

##  Instalacion y Uso

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)
   cd nombre-del-repo

   ##  Estructura del Proyecto

El código sigue un diseño modular basado en **Programación Orientada a Objetos (POO)**. A continuación se detalla la arquitectura del script:

### 1. Capa de Configuración
En la parte superior, el script define la conexión con el motor externo:
* **Integración con Tesseract:** Se establece la ruta del ejecutable mediante `pytesseract.tesseract_cmd`. Es el puente necesario para que Python se comunique con el software de reconocimiento óptico.

### 2. Clase `FacturaOCR` (Lógica de Negocio)
Esta clase actúa como el motor principal del script. Su estructura es:

* **`__init__`**: Inicializa el sistema de registros (*logging*) para realizar un seguimiento de las operaciones.
* **`extraer_texto(ruta_imagen)`**: El método principal que ejecuta el flujo de trabajo:
    * **Validación de Entrada:** Comprueba la integridad de la ruta del archivo mediante la librería `os`.
    * **Carga de Imagen:** Utiliza `PIL` (Pillow) para cargar el objeto de imagen en memoria.
    * **Conversión:** Invoca al motor Tesseract con el parámetro `lang="spa"` para asegurar la detección de caracteres latinos (ñ, tildes).
    * **Sanitización:** Limpia el ruido del texto extraído con `.strip()`.



### 3. Orquestador de Ejecución (`__main__`)
El bloque final del código gestiona la interacción con el usuario desde la terminal:
1.  **Captura de Argumentos:** Lee la ruta de la imagen desde `sys.argv`.
2.  **Instanciación:** Crea un objeto único de la clase `FacturaOCR`.
3.  **Salida de Datos:** Imprime el resultado final formateado en la consola.

---

##  Flujo de Datos

```mermaid
graph TD
    A[Imagen en Disco] --> B{¿Existe el archivo?}
    B -- No --> C[Retornar Mensaje de Error]
    B -- Sí --> D[Cargar imagen con Pillow]
    D --> E[Procesar con PyTesseract]
    E --> F[Limpiar texto .strip]
    F --> G[Mostrar Resultado en Consola]