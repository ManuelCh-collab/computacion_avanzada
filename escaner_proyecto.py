import logging
import pytesseract
from PIL import Image

class FacturaOCR:
    def __init__(self):
        self.logger = logging.getLogger(f"[{self.__class__.__name__}]")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
        self.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

    def extraer_texto(self, ruta_imagen: str) -> str:
        """Extrae texto de una imagen de factura utilizando OCR.

        Args:
            ruta_imagen (str): Ruta de la imagen de factura.

        Returns:
            str: Texto extraído de la imagen.
        """
        img = Image.open(ruta_imagen)
        texto = pytesseract.image_to_string(img, lang="spa")  # 'spa' para español
        return texto

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ocr = FacturaOCR()
    ruta_imagen = "factura.jpeg"  # Cambia esto por la ruta de tu imagen
    texto_extraido = ocr.extraer_texto(ruta_imagen)
    print("Texto extraído de la factura:")
    print(texto_extraido)
