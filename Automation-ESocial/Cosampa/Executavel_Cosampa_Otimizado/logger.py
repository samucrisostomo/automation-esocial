"""
Sistema de logging para o Cosampa Energia Automation
Otimizado para execução sem privilégios de administrador
"""

import logging
import os
from datetime import datetime
import config


def configurar_logger(nome_arquivo=None):
    """Configura e retorna um logger configurado"""
    
    if nome_arquivo is None:
        nome_arquivo = config.LOG_FILE

    # Usa pasta de logs configurada no config.py
    log_dir = config.LOG_DIR
    os.makedirs(log_dir, exist_ok=True)

    log_path = os.path.join(log_dir, nome_arquivo)

    # Configura o logger
    logger = logging.getLogger('CosampaEnergiaAutomation')
    logger.setLevel(logging.DEBUG)

    # Evita duplicação de handlers
    if not logger.handlers:
        # Handler para arquivo
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        # Handler para console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formato das mensagens
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


def log_info(mensagem):
    """Registra uma mensagem de informação"""
    logger = configurar_logger()
    logger.info(mensagem)


def log_error(mensagem, erro=None):
    """Registra uma mensagem de erro"""
    logger = configurar_logger()
    if erro:
        logger.error(f"{mensagem}: {str(erro)}", exc_info=True)
    else:
        logger.error(mensagem)


def log_warning(mensagem):
    """Registra uma mensagem de aviso"""
    logger = configurar_logger()
    logger.warning(mensagem)


def log_debug(mensagem):
    """Registra uma mensagem de debug"""
    logger = configurar_logger()
    logger.debug(mensagem)


def limpar_logs_antigos(dias=30):
    """Remove logs mais antigos que o número de dias especificado"""
    try:
        log_dir = config.LOG_DIR
        if not os.path.exists(log_dir):
            return

        data_limite = datetime.now().timestamp() - (dias * 24 * 60 * 60)

        for arquivo in os.listdir(log_dir):
            if arquivo.endswith('.log'):
                arquivo_path = os.path.join(log_dir, arquivo)
                if os.path.getmtime(arquivo_path) < data_limite:
                    os.remove(arquivo_path)
                    log_info(f"Log antigo removido: {arquivo}")

    except Exception as e:
        log_error("Erro ao limpar logs antigos", e)
