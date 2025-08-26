# Script PowerShell para build do PartnerShip Automation
# Executar: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Depois: .\build.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    Build PartnerShip Automation" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar Python
Write-Host "[1/5] Verificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERRO: Python não encontrado" -ForegroundColor Red
    Read-Host "Pressione Enter para sair"
    exit 1
}

# Instalar/Atualizar PyInstaller
Write-Host ""
Write-Host "[2/5] Instalando/Atualizando PyInstaller..." -ForegroundColor Yellow
try {
    pip install --upgrade pyinstaller
    Write-Host "PyInstaller instalado/atualizado com sucesso" -ForegroundColor Green
} catch {
    Write-Host "ERRO: Falha ao instalar PyInstaller" -ForegroundColor Red
    Read-Host "Pressione Enter para sair"
    exit 1
}

# Instalar dependências
Write-Host ""
Write-Host "[3/5] Instalando dependências..." -ForegroundColor Yellow
try {
    pip install -r requirements.txt
    Write-Host "Dependências instaladas com sucesso" -ForegroundColor Green
} catch {
    Write-Host "ERRO: Falha ao instalar dependências" -ForegroundColor Red
    Read-Host "Pressione Enter para sair"
    exit 1
}

# Limpar builds anteriores
Write-Host ""
Write-Host "[4/5] Limpando builds anteriores..." -ForegroundColor Yellow
if (Test-Path "build") { Remove-Item -Recurse -Force "build" }
if (Test-Path "dist") { Remove-Item -Recurse -Force "dist" }
if (Test-Path "__pycache__") { Remove-Item -Recurse -Force "__pycache__" }
if (Test-Path "*.spec") { Remove-Item "*.spec" }
Write-Host "Limpeza concluída" -ForegroundColor Green

# Compilar executável
Write-Host ""
Write-Host "[5/5] Compilando executável..." -ForegroundColor Yellow
try {
    $pyinstallerArgs = @(
        "--clean",
        "--onefile",
        "--windowed",
        "--name", "PartnerShip-Automation",
        "--add-data", "PartnerShip.xlsx;.",
        "--add-data", "config.py;.",
        "--add-data", "logger.py;.",
        "--hidden-import", "pandas",
        "--hidden-import", "numpy",
        "--hidden-import", "pyautogui",
        "--hidden-import", "pygetwindow",
        "--hidden-import", "selenium",
        "--hidden-import", "selenium.webdriver",
        "--hidden-import", "selenium.webdriver.chrome.options",
        "--hidden-import", "selenium.webdriver.common.by",
        "--hidden-import", "selenium.webdriver.support.ui",
        "--hidden-import", "selenium.webdriver.support",
        "--hidden-import", "selenium.webdriver.support.expected_conditions",
        "--hidden-import", "selenium.common.exceptions",
        "--hidden-import", "openpyxl",
        "--hidden-import", "xlrd",
        "--hidden-import", "tkinter",
        "--hidden-import", "tkinter.messagebox",
        "--hidden-import", "tkinter.filedialog",
        "partnership.py"
    )
    
    pyinstaller @pyinstallerArgs
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Compilação concluída com sucesso!" -ForegroundColor Green
    } else {
        throw "Falha na compilação"
    }
} catch {
    Write-Host "ERRO: Falha na compilação" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Read-Host "Pressione Enter para sair"
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    Build concluído com sucesso!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Executável criado em: dist\PartnerShip-Automation.exe" -ForegroundColor Green
Write-Host ""
Write-Host "Características do executável:" -ForegroundColor Yellow
Write-Host "- Não requer privilégios de administrador" -ForegroundColor White
Write-Host "- Arquivo único (portable)" -ForegroundColor White
Write-Host "- Interface gráfica (sem console)" -ForegroundColor White
Write-Host "- Inclui todas as dependências" -ForegroundColor White
Write-Host "- Tamanho otimizado" -ForegroundColor White
Write-Host ""

# Verificar se o arquivo foi criado
if (Test-Path "dist\PartnerShip-Automation.exe") {
    $fileSize = (Get-Item "dist\PartnerShip-Automation.exe").Length / 1MB
    Write-Host "Tamanho do executável: $([math]::Round($fileSize, 2)) MB" -ForegroundColor Green
} else {
    Write-Host "AVISO: Executável não encontrado em dist\" -ForegroundColor Yellow
}

Read-Host "Pressione Enter para sair" 