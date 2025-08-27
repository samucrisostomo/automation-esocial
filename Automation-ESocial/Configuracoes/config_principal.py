# -*- coding: utf-8 -*-
"""
Configuração Principal - Automation eSocial
==========================================

Este arquivo contém as configurações principais e comuns para todos os sistemas
de automação eSocial. As configurações específicas de cada projeto estão em
arquivos separados.

Autor: Sistema de Automação eSocial
Data: Dezembro 2024
Versão: 3.0
"""

import os
import sys
from pathlib import Path

# =============================================================================
# CONFIGURAÇÕES GLOBAIS DO SISTEMA
# =============================================================================

# Versão do sistema
VERSION = "3.0"
SYSTEM_NAME = "Automation eSocial"

# =============================================================================
# CONFIGURAÇÕES DE PASTAS
# =============================================================================

# Pasta base do usuário
USER_PROFILE = os.environ.get('USERPROFILE', os.path.expanduser('~'))

# Pasta base da automação
AUTOMATION_BASE = os.path.join(USER_PROFILE, "Desktop", "Automate-Esocial")

# Pastas específicas por projeto
COSAMPA_DESTINO = os.path.join(AUTOMATION_BASE, "Cosampa-Energia")
PARTNERSHIP_DESTINO = os.path.join(AUTOMATION_BASE, "PartnerShip-Engenharia")

# Pastas de logs
COSAMPA_LOGS = os.path.join(USER_PROFILE, "AppData", "Local", "CosampaLogs")
PARTNERSHIP_LOGS = os.path.join(
    USER_PROFILE, "AppData", "Local", "PartnerShipLogs")

# Pasta Chrome Debug
CHROME_DEBUG_BASE = os.path.join(
    USER_PROFILE, "AppData", "Local", "ChromeDebug")

# Pasta ChromeDriver
CHROMEDRIVER_BASE = os.path.join(
    USER_PROFILE, "AppData", "Local", "chromedriver")

# =============================================================================
# CONFIGURAÇÕES DO CHROME
# =============================================================================

# Porta de debug padrão
CHROME_DEBUG_PORT = 9222

# Argumentos padrão do Chrome
CHROME_ARGS_DEFAULT = [
    "--no-first-run",
    "--no-default-browser-check",
    "--disable-popup-blocking",
    "--disable-extensions",
    "--disable-plugins",
    "--disable-images",
    "--disable-javascript",
    "--disable-web-security",
    "--allow-running-insecure-content",
    "--disable-features=VizDisplayCompositor"
]

# =============================================================================
# CONFIGURAÇÕES DE TIMEOUT
# =============================================================================

# Timeouts padrão (em segundos)
TIMEOUT_PAGINA = 30
TIMEOUT_ELEMENTO = 10
TIMEOUT_NAVEGACAO = 60
TIMEOUT_DOWNLOAD = 120

# =============================================================================
# CONFIGURAÇÕES DE LOG
# =============================================================================

# Nível de log padrão
LOG_LEVEL = "INFO"

# Formato de log padrão
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Tamanho máximo do arquivo de log (MB)
LOG_MAX_SIZE = 10

# Número de arquivos de log para manter
LOG_BACKUP_COUNT = 5

# =============================================================================
# CONFIGURAÇÕES DE PLANILHAS
# =============================================================================

# Nomes padrão das planilhas
COSAMPA_PLANILHA = "CosampaEnergia.xlsx"
PARTNERSHIP_PLANILHA = "PartnerShip.xlsx"

# Caminhos completos das planilhas
COSAMPA_PLANILHA_PATH = os.path.join(AUTOMATION_BASE, COSAMPA_PLANILHA)
PARTNERSHIP_PLANILHA_PATH = os.path.join(AUTOMATION_BASE, PARTNERSHIP_PLANILHA)

# =============================================================================
# CONFIGURAÇÕES DE INTERFACE
# =============================================================================

# Cores padrão da interface
CORES = {
    "fundo": "#2b2b2b",
    "texto": "#ffffff",
    "botao": "#4CAF50",
    "erro": "#f44336",
    "sucesso": "#4CAF50",
    "aviso": "#ff9800",
    "info": "#2196F3"
}

# Dimensões padrão da janela
DIMENSOES = {
    "largura": 800,
    "altura": 600,
    "min_largura": 600,
    "min_altura": 400
}

# =============================================================================
# CONFIGURAÇÕES DE SEGURANÇA
# =============================================================================

# Modo de execução
MODO_EXECUCAO = "usuario"  # "usuario" ou "admin"

# Verificações de segurança
VERIFICACOES_SEGURANCA = {
    "verificar_python": True,
    "verificar_chrome": True,
    "verificar_chromedriver": True,
    "verificar_dependencias": True,
    "verificar_permissoes": True
}

# =============================================================================
# FUNÇÕES UTILITÁRIAS
# =============================================================================


def criar_pastas_necessarias():
    """
    Cria todas as pastas necessárias para o funcionamento do sistema.
    """
    pastas = [
        AUTOMATION_BASE,
        COSAMPA_DESTINO,
        PARTNERSHIP_DESTINO,
        COSAMPA_LOGS,
        PARTNERSHIP_LOGS,
        CHROME_DEBUG_BASE,
        CHROMEDRIVER_BASE
    ]

    for pasta in pastas:
        Path(pasta).mkdir(parents=True, exist_ok=True)
        print(f"✅ Pasta criada/verificada: {pasta}")


def verificar_configuracao():
    """
    Verifica se todas as configurações estão corretas.
    """
    print(f"🔍 Verificando configuração do {SYSTEM_NAME} v{VERSION}")
    print(f"📁 Pasta base: {AUTOMATION_BASE}")
    print(f"🏭 Cosampa: {COSAMPA_DESTINO}")
    print(f"🤝 PartnerShip: {PARTNERSHIP_DESTINO}")
    print(f"📝 Logs Cosampa: {COSAMPA_LOGS}")
    print(f"📝 Logs PartnerShip: {PARTNERSHIP_LOGS}")

    # Criar pastas se não existirem
    criar_pastas_necessarias()

    print("✅ Configuração verificada com sucesso!")


def obter_config_projeto(projeto):
    """
    Retorna as configurações específicas de um projeto.

    Args:
        projeto (str): Nome do projeto ('cosampa' ou 'partnership')

    Returns:
        dict: Configurações do projeto
    """
    if projeto.lower() == "cosampa":
        return {
            "destino": COSAMPA_DESTINO,
            "logs": COSAMPA_LOGS,
            "planilha": COSAMPA_PLANILHA_PATH,
            "nome": "Cosampa Energia"
        }
    elif projeto.lower() == "partnership":
        return {
            "destino": PARTNERSHIP_DESTINO,
            "logs": PARTNERSHIP_LOGS,
            "planilha": PARTNERSHIP_PLANILHA_PATH,
            "nome": "PartnerShip Engenharia"
        }
    else:
        raise ValueError(f"Projeto '{projeto}' não reconhecido")

# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================


if __name__ == "__main__":
    print("🚀 Sistema de Configuração - Automation eSocial")
    print("=" * 50)

    verificar_configuracao()

    print("\n📋 Resumo das Configurações:")
    print(f"   • Sistema: {SYSTEM_NAME} v{VERSION}")
    print(f"   • Modo: {MODO_EXECUCAO}")
    print(f"   • Timeout padrão: {TIMEOUT_PAGINA}s")
    print(f"   • Nível de log: {LOG_LEVEL}")

    print("\n🎯 Projetos Configurados:")
    for projeto in ["cosampa", "partnership"]:
        config = obter_config_projeto(projeto)
        print(f"   • {config['nome']}: {config['destino']}")

    print("\n✅ Configuração concluída!")
