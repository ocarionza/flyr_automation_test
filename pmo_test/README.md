# Selenium POM Project

Este es un proyecto de pruebas automatizadas utilizando Selenium y el patrón Page Object Model (POM). Soporta pruebas en Chrome y Firefox.

## Requisitos

- Python 3.x
- Selenium
- WebDriver Manager
- Pytest
- Allure instalado en el proyecto (https://allurereport.org/docs/install-for-windows/#install-from-an-archive)
- Ffmpeg instalado en el equipo (https://phoenixnap.com/kb/ffmpeg-windows)

## Instalación

1. Clona el repositorio.
2. Instala las dependencias:
3. Instalar el paquete de Allure y añadirlo al PATH en las variables de entorno
4. Instalar el Ffmpeg y añadirlo al PATH en las variables de entorno

```bash
pip install -r requirements.txt
```

```bash
pytest .\tests\test_one_way.py --browser=chrome -m=oneway --alluredir=allure-results
```

```bash
pytest .\tests\test_one_way.py --browser=chrome -m=oneway --alluredir=allure-results
```