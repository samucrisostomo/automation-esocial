# 🚀 Automation eSocial - Sistema de Automação Corporativa

## 📋 **Descrição**

Sistema completo de automação para processos do eSocial, desenvolvido para funcionar **SEM privilégios de administrador** em ambientes corporativos. Inclui automações para Cosampa Energia e PartnerShip Engenharia.

## ✨ **Funcionalidades Principais**

- **🔒 Zero Administrador**: Funciona em qualquer ambiente corporativo
- **🤖 Automação Completa**: Processamento automático de planilhas Excel
- **📄 Geração de PDFs**: Criação automática de documentos do eSocial
- **🌐 Chrome Inteligente**: Detecção automática de versões e ChromeDriver
- **📝 Logs Completos**: Rastreamento de todas as operações
- **⚙️ Configurável**: Sistema flexível e personalizável

## 🏗️ **Projetos Incluídos**

### 🏭 **Cosampa Energia Automation**

- **Arquivo**: `Cosampa-Energia/cosampaenergia.py`
- **Instalador**: `Scripts/INSTALAR_COSAMPA.bat`
- **Executável**: `Cosampa-Energia/Cosampa Energia Automation.exe`

### 🤝 **PartnerShip Automation**

- **Arquivo**: `PartnerShip-Engenharia/partnership.py`
- **Instalador**: `Scripts/INSTALAR.bat`
- **Executável**: `PartnerShip-Engenharia/PartnerShip-Automation.exe`

## 📁 **Estrutura do Projeto**

```
Automation-ESocial/
├── 📁 Cosampa-Energia/           # Sistema Cosampa Energia
│   ├── cosampaenergia.py         # Arquivo principal
│   ├── config.py                 # Configurações
│   ├── logger.py                 # Sistema de logs
│   ├── requirements.txt          # Dependências
│   └── Cosampa Energia Automation.exe
│
├── 📁 PartnerShip-Engenharia/    # Sistema PartnerShip
│   ├── partnership.py            # Arquivo principal
│   ├── config.py                 # Configurações
│   ├── logger.py                 # Sistema de logs
│   ├── requirements.txt          # Dependências
│   └── PartnerShip-Automation.exe
│
├── 📁 Scripts/                   # Scripts de instalação
│   ├── INSTALAR_COSAMPA.bat     # Instalador Cosampa
│   ├── VERIFICAR_COSAMPA.bat    # Verificador Cosampa
│   └── INSTALAR.bat             # Instalador PartnerShip
│
├── 📁 Configuracoes/             # Arquivos de configuração
│   ├── config_cosampa.py        # Config Cosampa
│   ├── config_partnership.py    # Config PartnerShip
│   ├── logger_cosampa.py        # Logger Cosampa
│   └── logger_partnership.py    # Logger PartnerShip
│
├── 📁 Exemplos/                  # Planilhas de exemplo
│   ├── CosampaEnergia_Exemplo.xlsx
│   └── PartnerShip_Exemplo.xlsx
│
├── 📁 Documentacao/              # Documentação completa
│   ├── GUIA_COMPLETO_USO.md     # Guia principal
│   ├── GUIA_INSTALACAO.md       # Instalação
│   ├── COMO_USAR.txt            # Uso rápido
│   └── README_FINAL.md          # Documentação original
│
├── requirements.txt               # Dependências principais
└── README.md                     # Este arquivo
```

## 🚀 **Instalação Rápida**

### **Pré-requisitos**

- Python 3.8 ou superior
- Google Chrome instalado
- Conexão com internet

### **Instalação Automática**

1. **Clone o repositório**

   ```bash
   git clone https://github.com/SEU_USUARIO/automation-esocial.git
   cd automation-esocial
   ```

2. **Execute o instalador desejado**

   ```bash
   # Para Cosampa Energia
   cd Scripts
   INSTALAR_COSAMPA.bat

   # Para PartnerShip
   cd Scripts
   INSTALAR.bat
   ```

## 📖 **Como Usar**

### **1. Preparar Planilha**

- Crie uma planilha Excel com CPFs (coluna A) e nomes (coluna B)
- Salve na pasta `Desktop/Automate-Esocial/`

### **2. Executar Automação**

- **Opção A**: Duplo clique no atalho da área de trabalho
- **Opção B**: Execute o arquivo `.exe` gerado
- **Opção C**: Execute via Python: `python cosampaenergia.py`

### **3. Processo Automático**

1. Sistema detecta versão do Chrome
2. Baixa ChromeDriver compatível automaticamente
3. Abre Chrome em modo debug
4. Processa planilha e gera PDFs
5. Salva na pasta de destino configurada

## 🔧 **Solução de Problemas**

### **Verificação de Sistema**

```bash
# Para Cosampa
cd Scripts
VERIFICAR_COSAMPA.bat

# Para PartnerShip
cd PartnerShip-Engenharia
python partnership.py --verify
```

### **Logs do Sistema**

```
%USERPROFILE%\AppData\Local\CosampaLogs\
%USERPROFILE%\AppData\Local\PartnerShipLogs\
```

## 🔒 **Segurança Corporativa**

### **✅ O que o sistema FAZ:**

- Cria pastas apenas no perfil do usuário
- Instala dependências localmente (`--user`)
- Usa apenas recursos do usuário
- Opera dentro do sandbox do usuário
- Mantém logs locais para auditoria

### **❌ O que o sistema NÃO faz:**

- Não modifica arquivos do sistema
- Não instala programas globalmente
- Não requer privilégios de administrador
- Não acessa registros do Windows

## 📚 **Documentação**

- **📖 GUIA_COMPLETO_USO.md**: Manual completo de uso
- **🔧 GUIA_INSTALACAO.md**: Instalação detalhada
- **⚡ COMO_USAR.txt**: Guia rápido de uso
- **📋 README_FINAL.md**: Documentação original

## 🆘 **Suporte**

### **Em Caso de Problemas:**

1. Execute o verificador do sistema
2. Verifique os logs em AppData\Local
3. Consulte a documentação completa
4. Entre em contato com o suporte técnico

## 🤝 **Contribuição**

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Abra um Pull Request

## 📄 **Licença**

Este projeto é de uso interno das empresas parceiras.

---

**🚀 Desenvolvido para automatizar processos e aumentar a produtividade em ambientes corporativos!**

_Versão 3.0 - Estrutura Reorganizada_
_Última atualização: Dezembro 2024_
