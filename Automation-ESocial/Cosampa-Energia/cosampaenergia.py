import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import pandas as pd
import pyautogui
import pygetwindow as gw
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException
import config
import logger

# Importa configurações do arquivo config.py
PASTA_DESTINO = config.PASTA_DESTINO_COSAMPA
PLANILHA = config.PLANILHA_PADRAO_COSAMPA
executando = False
driver = None

# Configurações do PyAutoGUI para maior confiabilidade
pyautogui.FAILSAFE = config.PYAUTOGUI_FAILSAFE
pyautogui.PAUSE = config.PYAUTOGUI_PAUSE


def atualizar_status(msg):
    status_var.set(msg)
    janela.update_idletasks()


def selecionar_planilha():
    global PLANILHA
    arquivo = filedialog.askopenfilename(
        title="Selecionar planilha CosampaEnergia.xlsx",
        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
    )
    if arquivo:
        PLANILHA = arquivo
        atualizar_status(f"Planilha selecionada: {os.path.basename(PLANILHA)}")
    else:
        atualizar_status("Nenhuma planilha selecionada")


def ativar_janela_esocial():
    try:
        janelas = [j for j in gw.getAllWindows(
        ) if "esocial" in j.title.lower()]
        if not janelas:
            atualizar_status("⚠️ Janela do eSocial não encontrada.")
            return False
        janela = janelas[0]
        if not janela.isActive:
            janela.activate()
            time.sleep(0.5)
            for _ in range(3):
                if janela.isActive:
                    atualizar_status("Janela do eSocial ativada com sucesso.")
                    return True
                time.sleep(0.5)
                janela.activate()
            atualizar_status("⚠️ Falha ao ativar a janela do eSocial.")
            return False
        else:
            atualizar_status("Janela do eSocial já está ativa.")
            return True
    except Exception as e:
        atualizar_status(f"Erro ao ativar janela do eSocial: {str(e)}")
        return False


def iniciar_chrome_debug():
    try:
        atualizar_status("Iniciando Chrome em modo debug...")
        pyautogui.hotkey('win', 'r')
        time.sleep(1)
        user_data_dir = config.CHROME_USER_DATA_DIR
        comando = f'chrome.exe --remote-debugging-port={config.CHROME_DEBUG_PORT} --user-data-dir="{user_data_dir}" --no-first-run --no-default-browser-check'
        pyautogui.write(comando, interval=0.05)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.write(
            'https://login.esocial.gov.br/login.aspx', interval=0.05)
        pyautogui.press('enter')
        atualizar_status("Chrome iniciado e eSocial aberto.")
    except Exception as e:
        atualizar_status(f"Erro ao iniciar Chrome: {str(e)}")


def automacao():
    global executando, driver
    executando = True

    if not os.path.exists(PLANILHA):
        messagebox.showerror("Erro", f"Planilha não encontrada em: {PLANILHA}")
        executando = False
        return

    try:
        df = pd.read_excel(PLANILHA)
        if df.empty:
            messagebox.showerror("Erro", "A planilha está vazia")
            executando = False
            return
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler a planilha: {str(e)}")
        executando = False
        return

    os.makedirs(PASTA_DESTINO, exist_ok=True)

    # Usa o ChromeDriver configurado no config.py
    chromedriver_path = config.CHROMEDRIVER_EXE
    if not os.path.exists(chromedriver_path):
        messagebox.showerror(
            "Erro", "ChromeDriver não encontrado. Verifique a configuração.")
        executando = False
        return

    chrome_options = Options()
    chrome_options.debugger_address = "localhost:9222"
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")

    try:
        # Cria o serviço com o caminho do ChromeDriver
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(config.TIMEOUT_IMPLICITO)
        atualizar_status("Conectado ao Chrome com sucesso")
    except SessionNotCreatedException as e:
        messagebox.showerror(
            "Erro de Sessão",
            f"Erro ao criar sessão do Chrome: {str(e)}\n\n"
            f"Verifique se o Chrome está aberto em modo debug e se o ChromeDriver está configurado corretamente."
        )
        executando = False
        return
    except WebDriverException as e:
        messagebox.showerror(
            "Erro", f"Erro ao conectar ao Chrome. Certifique-se de que o Chrome está aberto em modo debug.\n\nErro: {str(e)}")
        executando = False
        return
    except Exception as e:
        messagebox.showerror(
            "Erro", f"Erro inesperado ao conectar ao Chrome: {str(e)}")
        executando = False
        return

    # Aguarda o menuEmpregado ficar disponível
    wait = WebDriverWait(driver, config.TIMEOUT_PADRAO)
    try:
        wait.until(EC.presence_of_element_located((By.ID, "menuEmpregado")))
        atualizar_status("menuEmpregado identificado. Iniciando automação...")
    except Exception as e:
        atualizar_status("❌ menuEmpregado não identificado. Abortando.")
        driver.quit()
        executando = False
        return

    driver.execute_script("arguments[0].click();", wait.until(
        EC.element_to_be_clickable((By.ID, "menuEmpregado"))))
    time.sleep(2)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[contains(text(), 'Gestão de Empregado')]"))).click()
    time.sleep(3)

    for i in range(len(df)):
        if not executando:
            break
        cpf = str(df.iloc[i, 0])
        if pd.isna(cpf) or cpf.strip() == "":
            atualizar_status("Linha vazia encontrada. Finalizando...")
            break
        nome_colaborador = str(df.iloc[i, 1])
        atualizar_status(f"Processando: {nome_colaborador}")
        filtro_input = wait.until(
            EC.presence_of_element_located((By.ID, "filtro")))
        filtro_input.clear()
        filtro_input.send_keys(cpf)
        try:
            wait.until(EC.element_to_be_clickable((By.ID, "ui-id-3"))).click()
        except:
            continue
        try:
            btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@class, 'dados-cadastrais') and contains(text(), 'Dados Cadastrais')]")))
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(4)
        except:
            continue
        if not ativar_janela_esocial():
            atualizar_status("Prosseguindo sem ativação da janela...")
            continue
        pyautogui.hotkey('ctrl', 'p')
        time.sleep(5)
        nome_pdf = f"{nome_colaborador}.pdf"
        if i == 0:
            pyautogui.press('tab', presses=5, interval=0.4)
            pyautogui.press('down')
            time.sleep(0.5)
            pyautogui.press('enter')
            pyautogui.press('tab', presses=3, interval=0.4)
            pyautogui.press('down')
            time.sleep(0.5)
            pyautogui.press('enter')
            pyautogui.press('tab', presses=3, interval=0.4)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.write(nome_pdf, interval=0.1)
            pyautogui.press('tab', presses=6, interval=0.4)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.write(PASTA_DESTINO, interval=0.05)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
        else:
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.write(nome_pdf, interval=0.1)
            time.sleep(1)
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
        atualizar_status(f"PDF salvo: {nome_pdf}")
        time.sleep(2)

    # Fechar driver e limpar recursos
    try:
        if driver:
            driver.quit()
    except Exception as e:
        print(f"Erro ao fechar driver: {e}")

    executando = False
    atualizar_status("✅ Automação concluída.")
    messagebox.showinfo("Finalizado", "Automação finalizada com sucesso.")


def iniciar():
    global executando
    if not executando:
        thread = threading.Thread(target=automacao)
        thread.start()
    else:
        messagebox.showwarning(
            "Executando", "A automação já está em execução.")


def iniciar_chrome():
    thread = threading.Thread(target=iniciar_chrome_debug)
    thread.start()


def parar():
    global executando
    if executando:
        executando = False
        atualizar_status("🛑 Encerrando automação...")
        messagebox.showinfo("Parar", "A automação será encerrada.")
    else:
        messagebox.showinfo("Status", "Nenhuma automação está rodando.")


janela = tk.Tk()
janela.title("Cosampa Energia Automation - eSocial")
janela.geometry(f"{config.JANELA_LARGURA}x{config.JANELA_ALTURA}")
janela.resizable(False, False)

# Configurar ícone da janela (se disponível)
try:
    janela.iconbitmap("icon.ico")
except:
    pass

# Título principal
titulo_frame = tk.Frame(janela)
titulo_frame.pack(pady=10)
tk.Label(titulo_frame, text="Cosampa Energia Automation - eSocial",
         font=("Arial", 14, "bold"), fg=config.COR_TITULO).pack()
tk.Label(titulo_frame, text="Automação eSocial",
         font=("Arial", 10), fg=config.COR_SUBTITULO).pack()

# Frame para botões principais
botoes_frame = tk.Frame(janela)
botoes_frame.pack(pady=10)

tk.Button(botoes_frame, text="📁 Selecionar Planilha", width=25,
          command=selecionar_planilha, bg=config.COR_VERDE, fg="white",
          font=("Arial", 10, "bold")).pack(pady=3)

tk.Button(botoes_frame, text="🌐 Abrir Chrome eSocial", width=25,
          command=iniciar_chrome, bg=config.COR_AZUL, fg="white",
          font=("Arial", 10, "bold")).pack(pady=3)


tk.Button(botoes_frame, text="▶️ Iniciar Automação", width=25,
          command=iniciar, bg=config.COR_VERDE, fg="white",
          font=("Arial", 10, "bold")).pack(pady=3)

tk.Button(botoes_frame, text="⛔ Encerrar Automação", width=25,
          command=parar, bg=config.COR_VERMELHO, fg="white",
          font=("Arial", 10, "bold")).pack(pady=3)

# Status
status_frame = tk.Frame(janela)
status_frame.pack(pady=10, fill="x", padx=20)

status_var = tk.StringVar()
status_var.set("Aguardando início...")
tk.Label(status_frame, textvariable=status_var, fg=config.COR_TITULO,
         wraplength=350, font=("Arial", 10), justify="center").pack()

# Informações da planilha
info_var = tk.StringVar()
info_var.set(f"Planilha: {os.path.basename(PLANILHA)}")
tk.Label(status_frame, textvariable=info_var, fg=config.COR_SUBTITULO,
         font=("Arial", 9)).pack(pady=5)

janela.mainloop()
