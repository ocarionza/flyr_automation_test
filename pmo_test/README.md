# Selenium POM Project

Este es un proyecto de pruebas automatizadas utilizando Selenium y el patrón Page Object Model (POM). Soporta pruebas en Chrome y Firefox.

## Requisitos

- Python 3.x
- Selenium
- WebDriver Manager
- Pytest
- Allure instalado en el proyecto (https://allurereport.org/docs/install-for-windows/#install-from-an-archive)
- Ffmpeg instalado en el equipo windows (https://phoenixnap.com/kb/ffmpeg-windows)
- Ffmpeg MAC (https://phoenixnap.com/kb/ffmpeg-mac)
- Ffmpeg linux (https://phoenixnap.com/kb/install-ffmpeg-ubuntu)

## Instalación

1. Clona el repositorio.
2. Instala las dependencias:
3. Instalar el paquete de Allure y añadirlo al PATH en las variables de entorno
4. Instalar el Ffmpeg y añadirlo al PATH en las variables de entorno
5. Se debe modificar el conmando ffmpeg de grabacion en el archivo () de acuerdo a su sistema operativo

```bash
pip install -r requirements.txt
```

Ejecucion prueba one-way (Se seleccionan servicios aleatorios y asientos aleatorios)

```bash
pytest .\tests\test_one_way.py --browser=chrome -m=oneway --alluredir=allure-results
```

Ejecucion prueba de cambio de idioma

```bash
pytest .\tests\test_language_selector.py --browser=chrome -m=oneway --alluredir=allure-results
```

Ejecucion prueba de cambio de POS

```bash
pytest .\tests\test_pos_selector.py --browser=chrome -m=oneway --alluredir=allure-results
```
