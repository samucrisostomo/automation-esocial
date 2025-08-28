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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === CONFIGURAÇÕES GERAIS ===
PASTA_DESTINO = fr"C:\Users\{os.getlogin()}\Desktop\Automate-Esocial\Cosampa-Energia"
# Caminho absoluto para a planilha local
PLANILHA = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "Automate-Esocial",
    "CosampaEnergia.xlsx"
)
executando = False  # Flag de controle para saber se a automação está rodando

# === FUNÇÃO PARA ATUALIZAR O STATUS NA INTERFACE ===


def atualizar_status(msg):
    status_var.set(msg)  # Atualiza a variável de texto do Label
    janela.update_idletasks()  # Garante que a interface seja atualizada em tempo real


# === FUNÇÃO PARA SELECIONAR PLANILHA ===
def selecionar_planilha():
    global PLANILHA
    arquivo = filedialog.askopenfilename(
        title="Selecionar planilha CosampaEnergia.xlsx",
        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
    )
    if arquivo:
        PLANILHA = arquivo
        atualizar_status(f"Planilha selecionada: {os.path.basename(PLANILHA)}")
        # Atualiza também a informação da planilha na interface
        info_var.set(f"Planilha: {os.path.basename(PLANILHA)}")
    else:
        atualizar_status("Nenhuma planilha selecionada")

# === FUNÇÃO PARA ATIVAR A JANELA DO ESOCIAL ===


def ativar_janela_esocial():
    try:
        # Busca janelas com "eSocial" no título (case-insensitive)
        janelas = [j for j in gw.getAllWindows(
        ) if "esocial" in j.title.lower()]
        if not janelas:
            atualizar_status("⚠️ Janela do eSocial não encontrada.")
            return False

        # Tenta ativar a primeira janela correspondente
        janela = janelas[0]
        if not janela.isActive:
            janela.activate()
            time.sleep(0.5)  # Reduz o tempo de espera inicial
            # Verifica se a janela foi realmente ativada
            for _ in range(3):  # Tenta até 3 vezes
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


# === FUNÇÃO PARA INICIAR O CHROME EM MODO DEBUG ===
def iniciar_chrome_debug():
    try:
        atualizar_status("Iniciando Chrome em modo debug...")
        pyautogui.hotkey('win', 'r')
        time.sleep(1)
        # Usar pasta do usuário em vez de C:\selenium (que precisa de admin)
        user_data_dir = os.path.join(
            os.path.expanduser("~"), "AppData", "Local", "ChromeDebug")
        comando = f'chrome.exe --remote-debugging-port=9222 --user-data-dir="{user_data_dir}" --no-first-run --no-default-browser-check'
        pyautogui.write(comando, interval=0.05)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.write(
            'https://login.esocial.gov.br/login.aspx', interval=0.05)
        pyautogui.press('enter')
        atualizar_status("Chrome iniciado e eSocial aberto.")
    except Exception as e:
        atualizar_status(f"Erro ao iniciar Chrome: {str(e)}")

# === FUNÇÃO PRINCIPAL DE AUTOMAÇÃO ===


def automacao():
    global executando
    executando = True  # Inicia a execução

    # Verifica se o arquivo da planilha existe
    if not os.path.exists(PLANILHA):
        messagebox.showerror("Erro", f"Planilha não encontrada em: {PLANILHA}")
        executando = False
        return

    # Lê a planilha Excel e cria pasta de destino se necessário
    try:
        df = pd.read_excel(PLANILHA)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler a planilha: {str(e)}")
        executando = False
        return

    os.makedirs(PASTA_DESTINO, exist_ok=True)

    # Conecta ao navegador Chrome já aberto com modo de depuração
    chrome_options = Options()
    chrome_options.debugger_address = "localhost:9222"
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao Chrome: {str(e)}")
        executando = False
        return

    # Verifica se a aba atual é o eSocial
    if "eSocial" not in driver.title:
        messagebox.showerror("Erro", "A aba aberta não é o eSocial.")
        driver.quit()
        return

    # Navega para o menu "Gestão de Empregado"
    wait = WebDriverWait(driver, 15)
    driver.execute_script("arguments[0].click();", wait.until(
        EC.element_to_be_clickable((By.ID, "menuEmpregado"))))
    time.sleep(2)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[contains(text(), 'Gestão de Empregado')]"))).click()
    time.sleep(3)

    # === LOOP PARA CADA COLABORADOR NA PLANILHA ===
    for i in range(len(df)):
        if not executando:
            break  # Se clicar em "Parar", encerra loop imediatamente

        cpf = str(df.iloc[i, 0])  # Coluna de CPF
        if pd.isna(cpf) or cpf.strip() == "":
            atualizar_status("Linha vazia encontrada. Finalizando...")
            break

        nome_colaborador = str(df.iloc[i, 1])  # Coluna de Nome
        atualizar_status(f"Processando: {nome_colaborador}")

        # Preenche o campo de filtro com o CPF
        filtro_input = wait.until(
            EC.presence_of_element_located((By.ID, "filtro")))
        filtro_input.clear()
        filtro_input.send_keys(cpf)

        # Clica na sugestão do CPF
        try:
            wait.until(EC.element_to_be_clickable((By.ID, "ui-id-3"))).click()
        except:
            continue  # Se não encontrar sugestão, passa para o próximo

        # Clica em "Dados Cadastrais"
        try:
            btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@class, 'dados-cadastrais') and contains(text(), 'Dados Cadastrais')]")))
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(4)
        except:
            continue  # Se não encontrar botão, passa para o próximo

        # Ativa a janela do eSocial
        if not ativar_janela_esocial():
            atualizar_status("Prosseguindo sem ativação da janela...")
            continue  # Pula para o próximo se não conseguir ativar

        # Inicia a tela de impressão
        pyautogui.hotkey('ctrl', 'p')
        time.sleep(5)
        nome_pdf = f"{nome_colaborador}.pdf"

        # === PRIMEIRA VEZ: configurações iniciais ===
        if i == 0:
            # Altera o destino para "Salvar como PDF"
            pyautogui.press('tab', presses=5, interval=0.4)
            pyautogui.press('down')
            time.sleep(0.5)
            pyautogui.press('enter')

            # Altera layout para paisagem
            pyautogui.press('tab', presses=3, interval=0.4)
            pyautogui.press('down')
            time.sleep(0.5)
            pyautogui.press('enter')

            # Clica em "Imprimir"
            pyautogui.press('tab', presses=3, interval=0.4)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(3)

            # Nomeia o arquivo PDF
            pyautogui.write(nome_pdf, interval=0.1)
            pyautogui.press('tab', presses=6, interval=0.4)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.write(PASTA_DESTINO, interval=0.05)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('enter')  # Confirmar salvar
            pyautogui.press('enter')  # Substituir, se necessário
            pyautogui.press('enter')  # Substituir, se necessário
            pyautogui.press('enter')  # Substituir, se necessário

        # === DEMAIS ITERAÇÕES ===
        else:
            pyautogui.press('enter')  # Imprimir direto
            time.sleep(3)
            pyautogui.write(nome_pdf, interval=0.1)
            time.sleep(1)
            pyautogui.press('enter')  # Confirmar salvar
            pyautogui.press('enter')  # Substituir
            pyautogui.press('enter')
            pyautogui.press('enter')

        atualizar_status(f"PDF salvo: {nome_pdf}")
        time.sleep(2)

    # Finaliza automação
    driver.quit()
    executando = False
    atualizar_status("✅ Automação concluída.")
    messagebox.showinfo("Finalizado", "Automação finalizada com sucesso.")

# === FUNÇÃO PARA INICIAR A AUTOMAÇÃO (em nova thread) ===


def iniciar():
    global executando
    if not executando:
        thread = threading.Thread(target=automacao)
        thread.start()
    else:
        messagebox.showwarning(
            "Executando", "A automação já está em execução.")


# === FUNÇÃO PARA INICIAR O CHROME ===
def iniciar_chrome():
    thread = threading.Thread(target=iniciar_chrome_debug)
    thread.start()

# === FUNÇÃO PARA PARAR A AUTOMAÇÃO ===


def parar():
    global executando
    if executando:
        executando = False
        atualizar_status("🛑 Encerrando automação...")
        messagebox.showinfo("Parar", "A automação será encerrada.")
    else:
        messagebox.showinfo("Status", "Nenhuma automação está rodando.")


# === INTERFACE GRÁFICA COM TKINTER ===
janela = tk.Tk()
janela.title("Automação eSocial - Cosampa Energia")
janela.geometry("380x350")
janela.resizable(False, False)

# Título
tk.Label(janela, text="Esocial - Cosampa Energia",
         font=("Arial", 12, "bold")).pack(pady=10)

# Botões
tk.Button(janela, text="📁 Selecionar Planilha", width=25, command=selecionar_planilha,
          bg="green", fg="white").pack(pady=5)

tk.Button(janela, text="🌐 Abrir Chrome eSocial", width=25, command=iniciar_chrome,
          bg="blue", fg="white").pack(pady=5)

tk.Button(janela, text="▶️ Iniciar Automação", width=25, command=iniciar,
          bg="green", fg="white").pack(pady=5)

tk.Button(janela, text="⛔ Encerrar Automação", width=25, command=parar,
          bg="red", fg="white").pack(pady=5)

# Label dinâmico de status
status_var = tk.StringVar()
status_var.set("Aguardando início...")
tk.Label(janela, textvariable=status_var, fg="blue", wraplength=320,
         font=("Arial", 10)).pack(pady=10)

# Informações da planilha
info_var = tk.StringVar()
info_var.set(f"Planilha: {os.path.basename(PLANILHA)}")
tk.Label(janela, textvariable=info_var, fg="gray",
         font=("Arial", 9)).pack(pady=5)

# Inicia o loop da interface
janela.mainloop()
