import pytest
import allure
import subprocess
import os
import shutil
from datetime import datetime
from config.browser_config import get_driver
from utils.logger import get_logger

logger = get_logger()

# Path donde se guardarán los videos
VIDEO_DIR = "videos/"

@pytest.fixture(scope="session", autouse=True)
def clear_allure_reports():
    report_dir = "allure_reports/"
    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)  # Borra el directorio de reportes de Allure
        print(f"Reportes de Allure en {report_dir} eliminados.")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para capturar pantalla en los tests fallidos y generar el reporte de Allure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        try:
            # Tomar captura de pantalla cuando el test falla
            driver = item.funcargs['driver']
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Fallo al tomar captura de pantalla: {e}")

@pytest.fixture(scope="function")
def start_recording(request):
    """Fixture para grabar el video de la ejecución del test."""
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    video_name = f"{test_name}_{timestamp}.mp4"
    video_path = os.path.join(VIDEO_DIR, video_name)

    # Crea la carpeta de videos si no existe
    if not os.path.exists(VIDEO_DIR):
        os.makedirs(VIDEO_DIR)

    # Comando para grabar el escritorio con ffmpeg
    command = f"ffmpeg -y -f gdigrab -framerate 30 -i desktop -c:v libx264 -r 30 -pix_fmt yuv420p {video_path}"
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)

    yield  # Ejecuta el test

    # Detener la grabación de forma segura
    process.stdin.write(b'q')  # Envía el comando 'q' para finalizar
    process.stdin.flush()  # Asegúrate de que se envíe el comando
    process.wait()  # Espera a que el proceso termine

    # Adjuntar el video al reporte de Allure
    allure.attach.file(video_path, name="video", attachment_type=allure.attachment_type.MP4)

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    driver = get_driver(browser)

    yield driver

    driver.quit()
    logger.info(f"Finalizando el navegador {browser}")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests with.")