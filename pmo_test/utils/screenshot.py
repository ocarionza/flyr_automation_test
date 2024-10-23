import os
from utils.logger import get_logger

logger = get_logger()

def take_screenshot(driver, name):
    """Toma una captura de pantalla y la guarda en la carpeta 'reports'."""
    try:
        screenshot_path = os.path.join(os.getcwd(), "reports", f"{name}.png")
        driver.save_screenshot(screenshot_path)
        logger.info(f"Captura de pantalla guardada en: {screenshot_path}")
    except Exception as e:
        logger.error(f"Error al tomar la captura de pantalla: {e}")
        raise
