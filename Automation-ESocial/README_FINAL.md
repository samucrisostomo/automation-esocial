# PartnerShip Automation - eSocial

## 📋 Descrição

Sistema automatizado para extração de dados do eSocial, desenvolvido para a PartnerShip Engenharia. O sistema automatiza o processo de geração de PDFs de colaboradores a partir de uma planilha Excel.

## ✨ Funcionalidades

- **Detecção Automática de Versões**: Detecta automaticamente a versão do Chrome instalada
- **Download Automático do ChromeDriver**: Baixa e instala a versão correta do ChromeDriver
- **Interface Gráfica Intuitiva**: Interface simples e fácil de usar
- **Automação Completa**: Processa planilhas Excel automaticamente
- **Sistema de Logs**: Registra todas as operações para facilitar a depuração
- **Tratamento de Erros Robusto**: Mensagens de erro claras e sugestões de solução

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Google Chrome instalado
- Conexão com a internet (para download automático do ChromeDriver)

### Passos de Instalação

1. **Clone ou baixe o projeto**

   ```bash
   git clone [URL_DO_REPOSITORIO]
   cd PythonTest
   ```

2. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o sistema**
   ```bash
   python partnership.py
   ```

## 📖 Como Usar

### 1. Preparação da Planilha

- Crie uma planilha Excel chamada `PartnerShip.xlsx`
- A primeira coluna deve conter os CPFs dos colaboradores
- A segunda coluna deve conter os nomes dos colaboradores
- Salve a planilha na pasta `Desktop/Automate-Esocial/`

### 2. Execução da Automação

1. **Selecionar Planilha**: Clique em "📁 Selecionar Planilha" para escolher sua planilha
2. **Verificar ChromeDriver**: Clique em "🔧 Verificar ChromeDriver" para garantir compatibilidade
3. **Abrir Chrome**: Clique em "🌐 Abrir Chrome eSocial" para iniciar o Chrome em modo debug
4. **Iniciar Automação**: Clique em "▶️ Iniciar Automação" para começar o processo
5. **Encerrar**: Use "⛔ Encerrar Automação" se precisar parar o processo

### 3. Processo Automático

O sistema irá:

- Conectar ao Chrome em modo debug
- Navegar pelo eSocial automaticamente
- Processar cada linha da planilha
- Gerar PDFs para cada colaborador
- Salvar os arquivos na pasta de destino

## 🔧 Solução de Problemas

### Erro de Compatibilidade do ChromeDriver

**Problema**: "This version of ChromeDriver only supports Chrome version X"

**Solução**:

1. Clique em "🔧 Verificar ChromeDriver"
2. O sistema baixará automaticamente a versão correta
3. Execute novamente a automação

### Chrome não abre em modo debug

**Problema**: Erro ao abrir Chrome

**Solução**:

1. Feche todas as instâncias do Chrome
2. Verifique se o Chrome está instalado corretamente
3. Tente executar manualmente o comando de debug

### Planilha não encontrada

**Problema**: "Planilha não encontrada"

**Solução**:

1. Verifique se a planilha existe no caminho correto
2. Use o botão "📁 Selecionar Planilha" para escolher manualmente
3. Certifique-se de que a planilha está no formato correto

## 📁 Estrutura de Arquivos

```
PythonTest/
├── partnership.py          # Arquivo principal da aplicação
├── config.py              # Configurações do sistema
├── logger.py              # Sistema de logging
├── requirements.txt       # Dependências Python
├── README_FINAL.md        # Este arquivo
└── Pacote_Instalacao/    # Pacote de instalação
```

## ⚙️ Configurações

### Arquivo config.py

O arquivo `config.py` contém todas as configurações do sistema:

- **Caminhos**: Pastas de destino e planilhas
- **Chrome**: Porta de debug e diretório de dados
- **ChromeDriver**: Diretório de instalação e URLs de download
- **Timeouts**: Configurações de tempo limite
- **Interface**: Cores e dimensões da janela

### Personalização

Para personalizar o sistema:

1. Edite o arquivo `config.py`
2. Modifique as variáveis conforme necessário
3. Reinicie a aplicação

## 📊 Logs e Depuração

### Sistema de Logs

O sistema gera logs detalhados em:

- `~/logs/partnership_automation.log`

### Níveis de Log

- **DEBUG**: Informações detalhadas para desenvolvedores
- **INFO**: Informações gerais sobre operações
- **WARNING**: Avisos sobre situações não críticas
- **ERROR**: Erros que impedem a execução

### Limpeza de Logs

Os logs antigos são automaticamente removidos após 30 dias.

## 🔒 Segurança

- O sistema não armazena senhas ou dados sensíveis
- Todas as operações são locais
- Conexões externas são apenas para download do ChromeDriver

## 🆘 Suporte

### Logs de Erro

Em caso de problemas:

1. Verifique os logs em `~/logs/partnership_automation.log`
2. Copie as mensagens de erro para análise
3. Verifique se o Chrome está atualizado

### Problemas Comuns

1. **Versão do Chrome**: Mantenha o Chrome sempre atualizado
2. **Firewall**: Permita conexões para download do ChromeDriver
3. **Permissões**: Execute como usuário normal (não como administrador)

## 📝 Changelog

### Versão 2.0

- ✅ Detecção automática de versões do Chrome
- ✅ Download automático do ChromeDriver
- ✅ Sistema de logging completo
- ✅ Configurações centralizadas
- ✅ Tratamento de erros robusto
- ✅ Interface melhorada

### Versão 1.0

- ✅ Automação básica do eSocial
- ✅ Interface gráfica simples
- ✅ Processamento de planilhas Excel

## 🤝 Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Abra um Pull Request

## 📄 Licença

Este projeto é de uso interno da PartnerShip Engenharia.

---

**Desenvolvido com ❤️ para automatizar processos e aumentar a produtividade**
