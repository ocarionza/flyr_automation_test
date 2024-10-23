from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.logger import get_logger

logger = get_logger()


def get_driver(browser_name):
    try:
        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            logger.info("Iniciando Chrome")
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        elif browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            logger.info("Iniciando Firefox")
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

        else:
            logger.error(f"Navegador '{browser_name}' no soportado")
            raise ValueError(f"Browser '{browser_name}' is not supported.")

    except Exception as e:
        logger.error(f"Error iniciando el navegador: {e}")
        raise
