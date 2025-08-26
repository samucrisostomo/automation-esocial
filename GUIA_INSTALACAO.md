# 🚀 GUIA DE INSTALAÇÃO - PartnerShip Automation

## 📋 **Visão Geral**

Este guia irá ajudá-lo a instalar o sistema **PartnerShip Automation** em seu computador. O sistema automatiza a extração de dados do eSocial, economizando tempo e reduzindo erros manuais.

## ⚠️ **Pré-requisitos**

### **Sistema Operacional**

- ✅ Windows 10 (versão 1903 ou superior)
- ✅ Windows 11
- ❌ Windows 7/8/8.1 (não suportados)

### **Requisitos de Hardware**

- 💾 **RAM**: Mínimo 4GB, recomendado 8GB
- 💿 **Espaço em disco**: Mínimo 500MB livres
- 🖥️ **Processador**: Intel/AMD dual-core ou superior

### **Software Necessário**

- 🐍 **Python**: Versão 3.8 ou superior
- 🌐 **Google Chrome**: Versão 100 ou superior
- 📡 **Conexão com internet**: Para download automático do ChromeDriver

## 🔧 **Opções de Instalação**

### **Opção 1: Instalação Automática (Recomendada)**

#### **Passo 1: Preparação**

1. Baixe todos os arquivos do pacote de instalação
2. Extraia o arquivo ZIP em uma pasta temporária
3. Feche todos os programas abertos

#### **Passo 2: Executar Instalador**

1. **Clique com o botão direito** no arquivo `INSTALAR.bat`
2. Selecione **"Executar como administrador"**
3. Aguarde a instalação automática

#### **Passo 3: Verificação**

- ✅ O instalador criará automaticamente:
  - Pasta de instalação em `%USERPROFILE%\PartnerShip-Automation`
  - Atalho na área de trabalho
  - Atalho no menu iniciar
  - Script de desinstalação

### **Opção 2: Instalação Manual**

#### **Passo 1: Instalar Python**

1. Acesse [python.org/downloads](https://www.python.org/downloads/)
2. Baixe a versão mais recente do Python 3.x
3. **IMPORTANTE**: Marque a opção "Add Python to PATH"
4. Execute o instalador como administrador

#### **Passo 2: Verificar Instalação**

1. Abra o **Prompt de Comando** (cmd)
2. Digite: `python --version`
3. Digite: `pip --version`
4. Ambos devem retornar versões válidas

#### **Passo 3: Instalar Dependências**

1. No prompt de comando, navegue até a pasta do projeto
2. Execute: `pip install -r requirements.txt`

#### **Passo 4: Configurar Sistema**

1. Crie a pasta: `%USERPROFILE%\PartnerShip-Automation`
2. Copie todos os arquivos `.py` para esta pasta
3. Crie atalhos manuais conforme necessário

## 🎯 **Primeira Execução**

### **1. Iniciar o Sistema**

- Clique duas vezes no atalho **"PartnerShip Automation"** na área de trabalho
- Ou execute: `python partnership.py` na pasta de instalação

### **2. Verificar ChromeDriver**

- Clique no botão **"🔧 Verificar ChromeDriver"**
- O sistema detectará automaticamente sua versão do Chrome
- Baixará e instalará o ChromeDriver correto

### **3. Configurar Planilha**

- Use o botão **"📁 Selecionar Planilha"** para escolher sua planilha Excel
- Formato esperado:
  - **Coluna A**: CPF dos colaboradores
  - **Coluna B**: Nome dos colaboradores
  - **Primeira linha**: Cabeçalhos (opcional)

### **4. Executar Automação**

- Clique em **"🌐 Abrir Chrome eSocial"** para iniciar o Chrome
- Clique em **"▶️ Iniciar Automação"** para começar o processo

## 🔍 **Solução de Problemas**

### **Problema: "Python não encontrado"**

**Solução:**

1. Reinstale o Python marcando "Add Python to PATH"
2. Reinicie o computador
3. Execute o instalador novamente

### **Problema: "pip não encontrado"**

**Solução:**

1. Abra o prompt de comando como administrador
2. Execute: `python -m ensurepip --upgrade`
3. Execute: `python -m pip install --upgrade pip`

### **Problema: "Erro ao instalar dependências"**

**Solução:**

1. Verifique se tem conexão com a internet
2. Execute: `pip install --upgrade setuptools wheel`
3. Tente instalar cada dependência individualmente

### **Problema: "ChromeDriver incompatível"**

**Solução:**

1. Atualize o Google Chrome para a versão mais recente
2. Clique em **"🔧 Verificar ChromeDriver"**
3. O sistema baixará automaticamente a versão correta

### **Problema: "Permissão negada"**

**Solução:**

1. Execute o instalador como administrador
2. Verifique se o antivírus não está bloqueando
3. Desative temporariamente o Windows Defender

## 📁 **Estrutura de Arquivos Após Instalação**

```
%USERPROFILE%\PartnerShip-Automation\
├── partnership.py          # Programa principal
├── config.py              # Configurações do sistema
├── logger.py              # Sistema de logs
├── requirements.txt       # Lista de dependências
├── README_FINAL.md        # Documentação
├── PartnerShip_Exemplo.xlsx # Planilha de exemplo
├── install_log.json       # Log da instalação
├── uninstall.bat          # Script de desinstalação
├── logs\                  # Pasta de logs
├── chromedriver\          # Pasta do ChromeDriver
└── temp\                  # Pasta temporária
```

## 🔗 **Atalhos Criados**

### **Área de Trabalho**

- `PartnerShip Automation.bat` - Inicia o sistema

### **Menu Iniciar**

- `PartnerShip Automation.bat` - Acesso rápido

## 🗑️ **Desinstalação**

### **Método 1: Script Automático**

1. Execute: `%USERPROFILE%\PartnerShip-Automation\uninstall.bat`
2. Confirme a desinstalação

### **Método 2: Manual**

1. Delete a pasta: `%USERPROFILE%\PartnerShip-Automation`
2. Delete o atalho da área de trabalho
3. Delete o atalho do menu iniciar

## 📞 **Suporte Técnico**

### **Em Caso de Problemas**

1. **Verifique os logs** em: `%USERPROFILE%\PartnerShip-Automation\logs\`
2. **Copie as mensagens de erro** para análise
3. **Verifique a versão do Chrome** instalada
4. **Teste a conexão com a internet**

### **Contatos**

- 📧 **Email**: suporte@partnership.com.br
- 🌐 **Website**: https://partnership.com.br
- 📱 **Suporte interno**: Entre em contato com o TI da empresa

## ✅ **Checklist de Instalação**

- [ ] Python 3.8+ instalado e no PATH
- [ ] pip funcionando corretamente
- [ ] Todas as dependências instaladas
- [ ] Sistema executando sem erros
- [ ] ChromeDriver compatível instalado
- [ ] Atalhos criados corretamente
- [ ] Planilha de exemplo funcionando
- [ ] Logs sendo gerados

## 🎉 **Parabéns!**

Se você chegou até aqui, o sistema **PartnerShip Automation** foi instalado com sucesso!

### **Próximos Passos:**

1. **Teste o sistema** com a planilha de exemplo
2. **Configure sua planilha** com dados reais
3. **Execute a automação** para verificar o funcionamento
4. **Entre em contato** se encontrar algum problema

---

**Desenvolvido com ❤️ para PartnerShip Engenharia**

_Versão 2.0 - Instalação Automatizada_
