"""
Arquivo de configuração para o sistema PartnerShip Automation e Cosampa Energia
"""

import os

# Configurações do sistema - PartnerShip
PASTA_DESTINO = fr"C:\Users\{os.getlogin()}\Desktop\Automate-Esocial\PartnerShip-Engenharia"
PLANILHA_PADRAO = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "Automate-Esocial",
    "PartnerShip.xlsx"
)

# Configurações do sistema - Cosampa Energia
PASTA_DESTINO_COSAMPA = fr"C:\Users\{os.getlogin()}\Desktop\Automate-Esocial\Cosampa-Energia"
PLANILHA_PADRAO_COSAMPA = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "Automate-Esocial",
    "CosampaEnergia.xlsx"
)

# Configurações do Chrome
CHROME_DEBUG_PORT = 9222
CHROME_USER_DATA_DIR = os.path.join(
    os.path.expanduser("~"), "AppData", "Local", "ChromeDebug")

# Configurações do ChromeDriver
CHROMEDRIVER_DIR = os.path.join(os.path.expanduser("~"), "chromedriver")
CHROMEDRIVER_EXE = os.path.join(CHROMEDRIVER_DIR, "chromedriver.exe")

# URLs do ChromeDriver
CHROMEDRIVER_API_BASE = "https://chromedriver.storage.googleapis.com"
CHROMEDRIVER_DOWNLOAD_BASE = "https://chromedriver.storage.googleapis.com"

# Configurações de timeout
TIMEOUT_PADRAO = 30
TIMEOUT_IMPLICITO = 10
TIMEOUT_DOWNLOAD = 60

# Configurações do PyAutoGUI
PYAUTOGUI_PAUSE = 0.5
PYAUTOGUI_FAILSAFE = True

# Configurações da interface
JANELA_LARGURA = 400
JANELA_ALTURA = 450
JANELA_TITULO = "PartnerShip Automation - eSocial"
JANELA_SUBTITULO = "Automação eSocial"

# Cores da interface
COR_VERDE = "#4CAF50"
COR_AZUL = "#2196F3"
COR_LARANJA = "#FF9800"
COR_VERMELHO = "#F44336"
COR_TITULO = "#2E86AB"
COR_SUBTITULO = "#666666"
