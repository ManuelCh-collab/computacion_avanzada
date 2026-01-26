import logging
import pytesseract
from PIL import Image
import sys
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class FacturaOCR:
    def __init__(self):
        self.logger = logging.getLogger(f"[{self.__class__.__name__}]")
        
    def extraer_texto(self, ruta_imagen: str) -> str:
        """Extrae texto de una imagen validando que el archivo exista."""
        if not os.path.exists(ruta_imagen):
            return f"Error: El archivo '{ruta_imagen}' no existe."
            
        try:
            img = Image.open(ruta_imagen)
            
            texto = pytesseract.image_to_string(img, lang="spa")
            return texto.strip() 
        except Exception as e:
            return f"Error crítico al procesar la imagen: {e}"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
    if len(sys.argv) < 2:
        print("\n[!] Uso correcto: python escaner_proyecto.py nombre_de_la_imagen.jpg")
        print("[?] Ejemplo: python escaner_proyecto.py factura1.jpg\n")
    else:
        ruta_imagen = sys.argv[1] 
        ocr = FacturaOCR()
        
        print(f"--- Iniciando OCR para: {ruta_imagen} ---")
        texto_extraido = ocr.extraer_texto(ruta_imagen)
        
        print("\nRESULTADO:\n")
        print(texto_extraido)
        print("\n" + "="*40)