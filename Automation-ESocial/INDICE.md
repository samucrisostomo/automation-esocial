# 📚 ÍNDICE - Automation eSocial

## 🚀 **Navegação Rápida**

### **📁 Estrutura Principal**

```
Automation-ESocial/
├── 📖 README.md                    # Documentação principal
├── 📋 INDICE.md                    # Este arquivo
├── 📦 requirements.txt             # Dependências Python
│
├── 🏭 Cosampa-Energia/            # Sistema Cosampa
├── 🤝 PartnerShip-Engenharia/     # Sistema PartnerShip
├── 🔧 Scripts/                     # Scripts de instalação
├── ⚙️  Configuracoes/             # Arquivos de configuração
├── 📊 Exemplos/                    # Planilhas de exemplo
└── 📚 Documentacao/                # Documentação completa
```

---

## 🏭 **COSAMPA ENERGIA**

### **📁 Pasta: `Cosampa-Energia/`**

- **`cosampaenergia.py`** - Sistema principal de automação
- **`config.py`** - Configurações específicas do Cosampa
- **`logger.py`** - Sistema de logs do Cosampa
- **`requirements.txt`** - Dependências do projeto
- **`Cosampa Energia Automation.exe`** - Executável standalone

### **🔧 Scripts Relacionados**

- **`Scripts/INSTALAR_COSAMPA.bat`** - Instalador automático
- **`Scripts/VERIFICAR_COSAMPA.bat`** - Verificador específico

### **📊 Exemplo**

- **`Exemplos/CosampaEnergia_Exemplo.xlsx`** - Planilha modelo

---

## 🤝 **PARTNERSHIP ENGENHARIA**

### **📁 Pasta: `PartnerShip-Engenharia/`**

- **`partnership.py`** - Sistema principal de automação
- **`config.py`** - Configurações específicas do PartnerShip
- **`logger.py`** - Sistema de logs do PartnerShip
- **`requirements.txt`** - Dependências do projeto
- **`PartnerShip-Automation.exe`** - Executável standalone

### **🔧 Scripts Relacionados**

- **`Scripts/INSTALAR.bat`** - Instalador automático

### **📊 Exemplo**

- **`Exemplos/PartnerShip_Exemplo.xlsx`** - Planilha modelo

---

## 🔧 **SCRIPTS DE INSTALAÇÃO**

### **📁 Pasta: `Scripts/`**

- **`INSTALAR_COSAMPA.bat`** - Instalação do Cosampa
- **`INSTALAR.bat`** - Instalação do PartnerShip
- **`VERIFICAR_COSAMPA.bat`** - Verificação do Cosampa
- **`VERIFICAR_SISTEMA.bat`** - Verificação completa do sistema

---

## ⚙️ **CONFIGURAÇÕES**

### **📁 Pasta: `Configuracoes/`**

- **`config_principal.py`** - Configurações globais do sistema
- **`config_cosampa.py`** - Configurações específicas do Cosampa
- **`config_partnership.py`** - Configurações específicas do PartnerShip
- **`logger_cosampa.py`** - Logger específico do Cosampa
- **`logger_partnership.py`** - Logger específico do PartnerShip

---

## 📊 **EXEMPLOS**

### **📁 Pasta: `Exemplos/`**

- **`CosampaEnergia_Exemplo.xlsx`** - Planilha modelo para Cosampa
- **`PartnerShip_Exemplo.xlsx`** - Planilha modelo para PartnerShip

---

## 📚 **DOCUMENTAÇÃO**

### **📁 Pasta: `Documentacao/`**

- **`GUIA_COMPLETO_USO.md`** - Manual completo de uso
- **`GUIA_INSTALACAO.md`** - Guia de instalação detalhado
- **`COMO_USAR.txt`** - Guia rápido de uso
- **`RESUMO_COSAMPA_CRIADO.md`** - Resumo técnico do Cosampa

---

## 🚀 **COMO COMEÇAR**

### **1. Primeira Execução**

```bash
# Verificar todo o sistema
cd Scripts
VERIFICAR_SISTEMA.bat
```

### **2. Instalação**

```bash
# Para Cosampa Energia
cd Scripts
INSTALAR_COSAMPA.bat

# Para PartnerShip
cd Scripts
INSTALAR.bat
```

### **3. Uso**

```bash
# Executar Cosampa
cd Cosampa-Energia
python cosampaenergia.py

# Executar PartnerShip
cd PartnerShip-Engenharia
python partnership.py
```

---

## 🔍 **VERIFICAÇÕES**

### **Sistema Completo**

- **`Scripts/VERIFICAR_SISTEMA.bat`** - Verifica todo o sistema

### **Cosampa Específico**

- **`Scripts/VERIFICAR_COSAMPA.bat`** - Verifica apenas o Cosampa

### **Configuração Principal**

```bash
cd Configuracoes
python config_principal.py
```

---

## 📁 **ESTRUTURA DE PASTAS CRIADAS**

### **Desktop do Usuário**

```
%USERPROFILE%\Desktop\Automate-Esocial\
├── Cosampa-Energia\          # PDFs gerados pelo Cosampa
└── PartnerShip-Engenharia\   # PDFs gerados pelo PartnerShip
```

### **AppData Local**

```
%USERPROFILE%\AppData\Local\
├── CosampaLogs\              # Logs do Cosampa
├── PartnerShipLogs\          # Logs do PartnerShip
├── chromedriver\             # ChromeDriver
└── ChromeDebug\              # Dados de debug do Chrome
```

---

## 🎯 **CASOS DE USO**

### **Desenvolvedor**

1. **Configuração**: `python Configuracoes/config_principal.py`
2. **Desenvolvimento**: Edite arquivos `.py` nas pastas específicas
3. **Teste**: Use scripts de verificação

### **Usuário Final**

1. **Instalação**: Execute scripts `.bat` da pasta Scripts
2. **Uso**: Execute arquivos `.exe` ou use atalhos criados
3. **Suporte**: Consulte documentação na pasta Documentacao

### **Administrador**

1. **Verificação**: Execute `VERIFICAR_SISTEMA.bat`
2. **Manutenção**: Monitore logs em AppData\Local
3. **Atualizações**: Use scripts de instalação

---

## 🔒 **SEGURANÇA**

### **✅ Características**

- **Zero Administrador**: Funciona sem privilégios elevados
- **Sandbox do Usuário**: Todas as operações são locais
- **Logs Completos**: Rastreamento de todas as ações
- **Configuração Local**: Nenhuma modificação do sistema

### **📝 Auditoria**

- Logs em: `AppData\Local\*Logs\`
- Configurações em: `Configuracoes\`
- Scripts em: `Scripts\`

---

## 🆘 **SUPORTE**

### **Problemas Comuns**

1. **Python não encontrado**: Execute `VERIFICAR_SISTEMA.bat`
2. **ChromeDriver incompatível**: Sistema baixa automaticamente
3. **Permissões negadas**: Execute instaladores novamente

### **Logs de Erro**

- **Cosampa**: `%USERPROFILE%\AppData\Local\CosampaLogs\`
- **PartnerShip**: `%USERPROFILE%\AppData\Local\PartnerShipLogs\`

### **Documentação**

- **Guia Completo**: `Documentacao/GUIA_COMPLETO_USO.md`
- **Instalação**: `Documentacao/GUIA_INSTALACAO.md`
- **Uso Rápido**: `Documentacao/COMO_USAR.txt`

---

## 📈 **VERSÕES**

### **Versão Atual: 3.0**

- ✅ Estrutura reorganizada
- ✅ Configurações centralizadas
- ✅ Scripts padronizados
- ✅ Documentação completa
- ✅ Verificação automática

### **Compatibilidade**

- **Sistema**: Windows 10/11
- **Python**: 3.8+
- **Chrome**: Qualquer versão
- **Permissões**: Usuário normal

---

**🎯 Use este índice para navegar rapidamente pela estrutura do sistema!**

_Última atualização: Dezembro 2024_
