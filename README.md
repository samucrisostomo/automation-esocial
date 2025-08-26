# �� Automation eSocial - Sistema de Automação Corporativa

## �� Descrição

Sistema completo de automação para processos do eSocial, desenvolvido para funcionar **SEM privilégios de administrador** em ambientes corporativos. Inclui automações para Cosampa Energia e PartnerShip Engenharia.

## ✨ Funcionalidades Principais

- **�� Zero Administrador**: Funciona em qualquer ambiente corporativo
- **�� Automação Completa**: Processamento automático de planilhas Excel
- **�� Geração de PDFs**: Criação automática de documentos do eSocial
- **�� Chrome Inteligente**: Detecção automática de versões e ChromeDriver
- **📝 Logs Completos**: Rastreamento de todas as operações
- **⚙️ Configurável**: Sistema flexível e personalizável

## 🏗️ Projetos Incluídos

### 🏭 Cosampa Energia Automation

- **Arquivo**: `Automation-ESocial/Cosampa/cosampaenergia.py`
- **Instalador**: `Automation-ESocial/Cosampa/INSTALAR_COSAMPA.bat`
- **Executável**: `Automation-ESocial/Cosampa/Cosampa Energia Automation.exe`

### 🤝 PartnerShip Automation

- **Arquivo**: `Automation-ESocial/Partnership/partnership.py`
- **Instalador**: `Automation-ESocial/Partnership/INSTALAR.bat`
- **Executável**: `Automation-ESocial/Partnership/PartnerShip-Automation.exe`

## 🚀 Instalação Rápida

### Pré-requisitos

- Python 3.8 ou superior
- Google Chrome instalado
- Conexão com internet

### Instalação Automática

1. **Clone o repositório**

   ```bash
   git clone https://github.com/SEU_USUARIO/automation-esocial.git
   cd automation-esocial
   ```

2. **Execute o instalador desejado**

   ```bash
   # Para Cosampa Energia
   cd Automation-ESocial/Cosampa
   INSTALAR_COSAMPA.bat

   # Para PartnerShip
   cd Automation-ESocial/Partnership
   INSTALAR.bat
   ```

## 📖 Como Usar

### 1. Preparar Planilha

- Crie uma planilha Excel com CPFs (coluna A) e nomes (coluna B)
- Salve na pasta `Desktop/Automate-Esocial/`

### 2. Executar Automação

- **Opção A**: Duplo clique no atalho da área de trabalho
- **Opção B**: Execute o arquivo `.exe` gerado
- **Opção C**: Execute via Python: `python cosampaenergia.py`

### 3. Processo Automático

1. Sistema detecta versão do Chrome
2. Baixa ChromeDriver compatível automaticamente
3. Abre Chrome em modo debug
4. Processa planilha e gera PDFs
5. Salva na pasta de destino configurada

## 🔧 Solução de Problemas

### Erro de Permissão

```bash
❌ Erro: Access Denied
```

**Solução**: Execute o instalador novamente

### ChromeDriver não baixa

```bash
❌ Erro: ChromeDriver download failed
```

**Solução**: Verifique conexão com internet e execute o verificador

### Pasta não encontrada

```bash
❌ Erro: Directory not found
```

**Solução**: Execute o instalador para criar pastas necessárias

## 📁 Estrutura do Projeto

```
automation-esocial/
├── Automation-ESocial/
│   ├── Cosampa/
│   │   ├── cosampaenergia.py
│   │   ├── config.py
│   │   ├── logger.py
│   │   ├── requirements.txt
│   │   ├── INSTALAR_COSAMPA.bat
│   │   ├── VERIFICAR_COSAMPA.bat
│   │   ├── Cosampa Energia Automation.exe
│   │   └── Executavel_Cosampa_Otimizado/
│   ├── Partnership/
│   │   ├── partnership.py
│   │   ├── config.py
│   │   ├── logger.py
│   │   ├── requirements.txt
│   │   ├── INSTALAR.bat
│   │   └── PartnerShip-Automation.exe
│   └── Documentacao/
├── README.md
├── .gitignore
├── LICENSE
└── requirements.txt
```

## 🔒 Segurança Corporativa

### ✅ O que o sistema FAZ:

- Cria pastas apenas no perfil do usuário
- Instala dependências localmente (`--user`)
- Usa apenas recursos do usuário
- Opera dentro do sandbox do usuário
- Mantém logs locais para auditoria

### ❌ O que o sistema NÃO faz:

- Não modifica arquivos do sistema
- Não instala programas globalmente
- Não requer privilégios de administrador
- Não acessa registros do Windows
- Não modifica variáveis de ambiente globais

## 📊 Logs e Monitoramento

### Localização dos Logs

```
%USERPROFILE%\AppData\Local\CosampaLogs\
%USERPROFILE%\AppData\Local\PartnerShipLogs\
```

### Conteúdo dos Logs

- Todas as operações do sistema
- Detecção de versões do Chrome
- Download e instalação do ChromeDriver
- Processamento da planilha
- Geração de PDFs
- Erros e avisos

## 🆘 Suporte

### Verificação de Sistema

```bash
# Para Cosampa
VERIFICAR_COSAMPA.bat

# Para PartnerShip
python partnership.py --verify
```

### Informações para Suporte

- Versão do Python: `python --version`
- Versão do Chrome: `chrome://version/`
- Logs do sistema: Pasta AppData\Local
- Arquivo de configuração: `.env`

## 🤝 Contribuição

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Abra um Pull Request

## 📄 Licença

Este projeto é de uso interno das empresas parceiras.

---

**🚀 Desenvolvido para automatizar processos e aumentar a produtividade em ambientes corporativos!**
