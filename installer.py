#!/usr/bin/env python3
"""
Instalador Automatizado para PartnerShip Automation
Versão 2.0 - Instalação Completa e Automatizada
"""

import os
import sys
import subprocess
import shutil
import zipfile
import requests
import json
from pathlib import Path
import platform


class PartnerShipInstaller:
    def __init__(self):
        self.install_dir = Path.home() / "PartnerShip-Automation"
        self.python_version = "3.8"
        self.required_packages = [
            "numpy>=1.21.0",
            "pandas>=1.5.0",
            "pyautogui>=0.9.54",
            "pygetwindow>=0.0.9",
            "selenium>=4.10.0",
            "openpyxl>=3.1.0",
            "xlrd>=2.0.1",
            "requests>=2.25.0"
        ]

    def print_banner(self):
        """Exibe o banner de instalação"""
        print("=" * 60)
        print("🚀 PARTNERSHIP AUTOMATION - INSTALADOR AUTOMATIZADO")
        print("=" * 60)
        print(f"📁 Diretório de instalação: {self.install_dir}")
        print(f"🐍 Python necessário: {self.python_version}+")
        print(f"💻 Sistema: {platform.system()} {platform.release()}")
        print("=" * 60)
        print()

    def check_python_version(self):
        """Verifica se a versão do Python é compatível"""
        print("🔍 Verificando versão do Python...")

        version = sys.version_info
        if version.major < 3 or (version.major == 3 and version.minor < 8):
            print(
                f"❌ Python {version.major}.{version.minor} não é compatível!")
            print(f"   Necessário: Python {self.python_version}+")
            return False

        print(
            f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatível!")
        return True

    def check_pip(self):
        """Verifica se o pip está disponível"""
        print("🔍 Verificando pip...")

        try:
            subprocess.run([sys.executable, "-m", "pip", "--version"],
                           check=True, capture_output=True)
            print("✅ pip disponível!")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ pip não encontrado!")
            return False

    def create_installation_directory(self):
        """Cria o diretório de instalação"""
        print("📁 Criando diretório de instalação...")

        try:
            self.install_dir.mkdir(parents=True, exist_ok=True)
            print(f"✅ Diretório criado: {self.install_dir}")
            return True
        except Exception as e:
            print(f"❌ Erro ao criar diretório: {e}")
            return False

    def copy_source_files(self):
        """Copia os arquivos fonte para o diretório de instalação"""
        print("📋 Copiando arquivos fonte...")

        source_files = [
            "partnership.py",
            "config.py",
            "logger.py",
            "requirements.txt",
            "README_FINAL.md"
        ]

        copied_count = 0
        for file_name in source_files:
            if os.path.exists(file_name):
                try:
                    shutil.copy2(file_name, self.install_dir / file_name)
                    print(f"   ✅ {file_name}")
                    copied_count += 1
                except Exception as e:
                    print(f"   ❌ {file_name}: {e}")
            else:
                print(f"   ⚠️ {file_name} não encontrado")

        print(f"✅ {copied_count}/{len(source_files)} arquivos copiados!")
        return copied_count > 0

    def install_dependencies(self):
        """Instala as dependências Python"""
        print("📦 Instalando dependências...")

        try:
            # Atualiza o pip primeiro
            print("   🔄 Atualizando pip...")
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
                           check=True, capture_output=True)

            # Instala as dependências
            for package in self.required_packages:
                print(f"   📥 Instalando {package}...")
                subprocess.run([sys.executable, "-m", "pip", "install", package],
                               check=True, capture_output=True)
                print(f"      ✅ {package}")

            print("✅ Todas as dependências instaladas!")
            return True

        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao instalar dependências: {e}")
            return False

    def create_desktop_shortcut(self):
        """Cria atalho na área de trabalho"""
        print("🔗 Criando atalho na área de trabalho...")

        try:
            desktop = Path.home() / "Desktop"
            shortcut_path = desktop / "PartnerShip Automation.lnk"

            # Cria um arquivo .bat como alternativa
            bat_path = desktop / "PartnerShip Automation.bat"
            with open(bat_path, 'w', encoding='utf-8') as f:
                f.write(f'@echo off\n')
                f.write(f'cd /d "{self.install_dir}"\n')
                f.write(f'python partnership.py\n')
                f.write(f'pause\n')

            print(f"✅ Atalho criado: {bat_path}")
            return True

        except Exception as e:
            print(f"❌ Erro ao criar atalho: {e}")
            return False

    def create_start_menu_shortcut(self):
        """Cria atalho no menu iniciar"""
        print("🔗 Criando atalho no menu iniciar...")

        try:
            start_menu = Path.home() / "AppData" / "Roaming" / "Microsoft" / \
                "Windows" / "Start Menu" / "Programs"
            start_menu.mkdir(parents=True, exist_ok=True)

            shortcut_path = start_menu / "PartnerShip Automation.bat"
            with open(shortcut_path, 'w', encoding='utf-8') as f:
                f.write(f'@echo off\n')
                f.write(f'cd /d "{self.install_dir}"\n')
                f.write(f'python partnership.py\n')

            print(f"✅ Atalho no menu iniciar criado!")
            return True

        except Exception as e:
            print(f"❌ Erro ao criar atalho no menu iniciar: {e}")
            return False

    def create_config_folders(self):
        """Cria pastas de configuração necessárias"""
        print("📁 Criando pastas de configuração...")

        folders = [
            self.install_dir / "logs",
            self.install_dir / "chromedriver",
            self.install_dir / "temp",
            Path.home() / "Desktop" / "Automate-Esocial"
        ]

        created_count = 0
        for folder in folders:
            try:
                folder.mkdir(parents=True, exist_ok=True)
                print(f"   ✅ {folder}")
                created_count += 1
            except Exception as e:
                print(f"   ❌ {folder}: {e}")

        print(f"✅ {created_count}/{len(folders)} pastas criadas!")
        return created_count > 0

    def create_sample_excel(self):
        """Cria planilha de exemplo"""
        print("📊 Criando planilha de exemplo...")

        try:
            import pandas as pd

            # Dados de exemplo
            sample_data = {
                'CPF': ['12345678901', '98765432100', '11122233344'],
                'Nome': ['João Silva', 'Maria Santos', 'Pedro Oliveira'],
                'Cargo': ['Engenheiro', 'Técnico', 'Auxiliar']
            }

            df = pd.DataFrame(sample_data)
            excel_path = self.install_dir / "PartnerShip_Exemplo.xlsx"
            df.to_excel(excel_path, index=False)

            print(f"✅ Planilha de exemplo criada: {excel_path}")
            return True

        except Exception as e:
            print(f"❌ Erro ao criar planilha de exemplo: {e}")
            return False

    def create_uninstaller(self):
        """Cria script de desinstalação"""
        print("🗑️ Criando script de desinstalação...")

        try:
            uninstall_path = self.install_dir / "uninstall.bat"
            with open(uninstall_path, 'w', encoding='utf-8') as f:
                f.write('@echo off\n')
                f.write('echo Desinstalando PartnerShip Automation...\n')
                f.write('echo.\n')
                f.write('echo Removendo arquivos...\n')
                f.write(f'rmdir /s /q "{self.install_dir}"\n')
                f.write('echo.\n')
                f.write('echo Removendo atalhos...\n')
                f.write(
                    f'del "%USERPROFILE%\\Desktop\\PartnerShip Automation.bat"\n')
                f.write(
                    f'del "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\PartnerShip Automation.bat"\n')
                f.write('echo.\n')
                f.write('echo Desinstalação concluída!\n')
                f.write('pause\n')

            print(f"✅ Script de desinstalação criado!")
            return True

        except Exception as e:
            print(f"❌ Erro ao criar script de desinstalação: {e}")
            return False

    def create_install_log(self):
        """Cria log da instalação"""
        print("📝 Criando log da instalação...")

        try:
            import datetime

            log_data = {
                'install_date': datetime.datetime.now().isoformat(),
                'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
                'platform': platform.platform(),
                'install_dir': str(self.install_dir),
                'dependencies': self.required_packages
            }

            log_path = self.install_dir / "install_log.json"
            with open(log_path, 'w', encoding='utf-8') as f:
                json.dump(log_data, f, indent=2, ensure_ascii=False)

            print(f"✅ Log da instalação criado!")
            return True

        except Exception as e:
            print(f"❌ Erro ao criar log da instalação: {e}")
            return False

    def run_tests(self):
        """Executa testes básicos"""
        print("🧪 Executando testes básicos...")

        try:
            # Testa importação dos módulos
            test_imports = [
                "import pandas",
                "import selenium",
                "import pyautogui",
                "import tkinter"
            ]

            for import_test in test_imports:
                try:
                    exec(import_test)
                    print(f"   ✅ {import_test}")
                except Exception as e:
                    print(f"   ❌ {import_test}: {e}")

            print("✅ Testes básicos concluídos!")
            return True

        except Exception as e:
            print(f"❌ Erro nos testes: {e}")
            return False

    def install(self):
        """Executa a instalação completa"""
        print("🚀 Iniciando instalação...")
        print()

        steps = [
            ("Verificação do Python", self.check_python_version),
            ("Verificação do pip", self.check_pip),
            ("Criação do diretório", self.create_installation_directory),
            ("Cópia dos arquivos", self.copy_source_files),
            ("Instalação das dependências", self.install_dependencies),
            ("Criação das pastas", self.create_config_folders),
            ("Criação da planilha exemplo", self.create_sample_excel),
            ("Criação dos atalhos", self.create_desktop_shortcut),
            ("Criação do menu iniciar", self.create_start_menu_shortcut),
            ("Criação do desinstalador", self.create_uninstaller),
            ("Criação do log", self.create_install_log),
            ("Execução dos testes", self.run_tests)
        ]

        successful_steps = 0
        total_steps = len(steps)

        for step_name, step_func in steps:
            print(f"📋 {step_name}...")
            if step_func():
                successful_steps += 1
            print()

        # Resumo da instalação
        print("=" * 60)
        print("📊 RESUMO DA INSTALAÇÃO")
        print("=" * 60)
        print(f"✅ Passos bem-sucedidos: {successful_steps}/{total_steps}")
        print(f"📁 Diretório de instalação: {self.install_dir}")
        print(f"🔗 Atalho na área de trabalho: PartnerShip Automation.bat")
        print()

        if successful_steps == total_steps:
            print("🎉 INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
            print()
            print("📖 PRÓXIMOS PASSOS:")
            print(
                "1. Clique duas vezes no atalho 'PartnerShip Automation' na área de trabalho")
            print("2. O sistema detectará automaticamente a versão do Chrome")
            print("3. Baixará o ChromeDriver correto automaticamente")
            print("4. Execute a automação normalmente")
            print()
            print("📞 Em caso de problemas, verifique os logs em:")
            print(f"   {self.install_dir}/logs/")
        else:
            print("⚠️ INSTALAÇÃO PARCIALMENTE CONCLUÍDA")
            print("   Alguns passos falharam. Verifique os erros acima.")

        print("=" * 60)

        return successful_steps == total_steps


def main():
    """Função principal"""
    try:
        installer = PartnerShipInstaller()
        installer.print_banner()

        # Confirmação do usuário
        response = input(
            "Deseja continuar com a instalação? (s/N): ").strip().lower()
        if response not in ['s', 'sim', 'y', 'yes']:
            print("❌ Instalação cancelada pelo usuário.")
            return

        # Executa a instalação
        success = installer.install()

        if success:
            input("\nPressione Enter para sair...")
        else:
            input("\nPressione Enter para sair (verifique os erros acima)...")

    except KeyboardInterrupt:
        print("\n\n❌ Instalação interrompida pelo usuário.")
    except Exception as e:
        print(f"\n\n❌ Erro inesperado: {e}")
        input("\nPressione Enter para sair...")


if __name__ == "__main__":
    main()
