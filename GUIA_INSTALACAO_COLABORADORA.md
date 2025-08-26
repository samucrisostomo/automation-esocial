# 📋 Guia de Instalação - PartnerShip Automation

## 🎯 **Informações do Executável**

- **Arquivo**: `PartnerShip-Automation.exe`
- **Tamanho**: ~42 MB
- **Tipo**: Executável único (portable)
- **Privilégios**: Não requer administrador
- **Sistema**: Windows 10/11

## 🚀 **Como Instalar e Usar**

### **Passo 1: Preparação**

1. **Crie uma pasta** no Desktop chamada `Automate-Esocial`
2. **Copie o executável** `PartnerShip-Automation.exe` para esta pasta
3. **Crie uma planilha** chamada `PartnerShip.xlsx` na mesma pasta com:
   - **Coluna A**: CPF dos colaboradores
   - **Coluna B**: Nome dos colaboradores

### **Passo 2: Primeira Execução**

1. **Clique duas vezes** no `PartnerShip-Automation.exe`
2. **Aguarde** a interface abrir (pode demorar alguns segundos)
3. **Se aparecer aviso do Windows Defender**:
   - Clique em "Mais informações"
   - Clique em "Executar mesmo assim"

### **Passo 3: Configuração Inicial**

1. **Clique em "📁 Selecionar Planilha"** e escolha sua planilha
2. **Clique em "🌐 Abrir Chrome eSocial"** para iniciar o Chrome
3. **Faça login** no eSocial normalmente
4. **Aguarde** a página carregar completamente

### **Passo 4: Executar Automação**

1. **Clique em "▶️ Iniciar Automação"**
2. **Aguarde** o processamento de cada colaborador
3. **Os PDFs serão salvos** em: `Desktop\Automate-Esocial\PartnerShip-Engenharia\`

## ⚠️ **Possíveis Restrições Corporativas**

### **Se o executável não abrir:**

- **Contate o TI** para liberar a execução
- **Solicite exceção** no antivírus corporativo
- **Verifique políticas** de execução de aplicações

### **Se o Chrome não iniciar:**

- **Verifique se o Chrome está instalado**
- **Contate o TI** para liberar execução com flags especiais
- **Solicite liberação** da porta 9222

### **Se não conseguir acessar o eSocial:**

- **Verifique VPN** (se necessário)
- **Teste acesso manual** ao eSocial
- **Contate o TI** para liberar o domínio

## 🔧 **Solução de Problemas**

### **Erro: "Executável não encontrado"**

```
Solução: Verifique se o arquivo está na pasta correta
```

### **Erro: "Chrome não pode ser iniciado"**

```
Solução:
1. Feche todas as instâncias do Chrome
2. Reinicie o executável
3. Se persistir, reinicie o computador
```

### **Erro: "Planilha não encontrada"**

```
Solução:
1. Verifique se a planilha está na pasta correta
2. Use o botão "📁 Selecionar Planilha"
3. Verifique se o arquivo é .xlsx
```

### **Erro: "menuEmpregado não identificado"**

```
Solução:
1. Certifique-se de estar logado no eSocial
2. Aguarde a página carregar completamente
3. Verifique se está na página correta
```

## 📁 **Estrutura de Pastas Recomendada**

```
Desktop/
└── Automate-Esocial/
    ├── PartnerShip-Automation.exe
    ├── PartnerShip.xlsx
    └── PartnerShip-Engenharia/  (criada automaticamente)
        ├── Nome1.pdf
        ├── Nome2.pdf
        └── ...
```

## 🛡️ **Checklist de Segurança**

### **Antes de usar:**

- [ ] Executável em pasta segura
- [ ] Planilha com dados corretos
- [ ] Chrome instalado e funcionando
- [ ] Acesso ao eSocial testado

### **Durante o uso:**

- [ ] Não interromper a automação
- [ ] Manter janela do eSocial visível
- [ ] Não usar mouse/teclado durante execução
- [ ] Verificar PDFs gerados

## 📞 **Suporte**

### **Se encontrar problemas:**

1. **Anote a mensagem de erro** exata
2. **Tire print da tela** se possível
3. **Contate o desenvolvedor** com as informações

### **Informações úteis para o TI:**

- **Porta utilizada**: 9222 (localhost)
- **Domínio**: login.esocial.gov.br
- **Flags Chrome**: --remote-debugging-port=9222
- **Permissões**: Controle de janelas (PyAutoGUI)

## ✅ **Vantagens do Executável**

- ✅ **Não precisa de Python** instalado
- ✅ **Não requer privilégios** de administrador
- ✅ **Arquivo único** (portable)
- ✅ **Interface gráfica** amigável
- ✅ **Inclui todas as dependências**
- ✅ **Funciona offline** (após primeira execução)

## 🎉 **Pronto para Usar!**

O executável está otimizado para funcionar na maioria dos ambientes corporativos sem necessidade de privilégios especiais. Em caso de restrições, contate o TI com as informações fornecidas acima.
