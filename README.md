# 💰 IR Expert - Simulador de Imposto de Renda

Projeto desenvolvido para a disciplina de **Matemática Aplicada** - Curso de Análise e Desenvolvimento de Sistemas.

## 📋 Descrição

O **IR Expert** é uma aplicação web que calcula o Imposto de Renda para Pessoa Física (IRPF) e Pessoa Jurídica (IRPJ), com integração de APIs para consulta de CNPJ e cotação do dólar.

## ✨ Funcionalidades

### 👤 Pessoa Física (IRPF)
- Cálculo baseado em salário bruto mensal
- Dedução por dependentes
- Dedução de despesas médicas e educação
- Dedução de previdência

### 🏢 Pessoa Jurídica (IRPJ)
- **Lucro Presumido:** Para comércio (8%) e serviços (32%)
- **Lucro Real:** Cálculo direto sobre o lucro

### 🔗 Integrações
- Consulta de CNPJ via BrasilAPI
- Cotação USD/BRL via AwesomeAPI

## 🛠️ Tecnologias

- Python 3.11+
- Streamlit (interface web)
- Requests (APIs)
- Pandas, Plotly, FPDF

## 🚀 Como Executar

### 1. Baixar o projeto
```bash
git clone https://github.com/AsGhrK/Impostos_Colto.git
cd ir-expert
```
```bash
pip install -r requirements.txt
```
```bash
streamlit run app.py
```
```bash
http://localhost:8501
```
### 📁 Estrutura dos Arquivos

app.py - Interface principal do Streamlit
calculations.py - Funções de cálculo de impostos
services.py - Integração com APIs externas
requirements.txt - Lista de dependências

### 🧮 Como Usar
Para Pessoa Física:

Acesse a aba "Pessoa Física"
Preencha: salário, dependentes, despesas
Clique em "Calcular IRPF"

Para Pessoa Jurídica:

Acesse a aba "Pessoa Jurídica"
Escolha: Lucro Presumido ou Lucro Real
Preencha os dados solicitados
Clique em "Calcular IRPJ"

###👥 Autores

Davi Casari
Gustavo Bravin

###📄 Licença
MIT License
