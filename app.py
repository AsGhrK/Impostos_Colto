
import streamlit as st
from calculations import (
    calcular_irpf,
    calcular_irpj_lucro_presumido,
    calcular_irpj_lucro_real,
)
from services import consultar_cnpj, consultar_cambio


st.set_page_config(page_title="IR Expert", page_icon="💰", layout="wide")

st.title("💰 IR Expert - Simulador de Imposto de Renda (PF e PJ)")

tab1, tab2 = st.tabs(["👤 Pessoa Física", "🏢 Pessoa Jurídica"])

with tab1:
    st.header("Cálculo de IRPF")
    salario = st.number_input("Salário Bruto Mensal (R$)", min_value=0.0)
    dependentes = st.number_input("Número de Dependentes", min_value=0, step=1)
    despesas_med = st.number_input("Despesas Médicas (R$)", min_value=0.0)
    despesas_edu = st.number_input("Despesas com Educação (R$)", min_value=0.0)
    previdencia = st.number_input("Previdência Oficial (R$)", min_value=0.0)

    if st.button("Calcular IRPF"):
        irpf = calcular_irpf(salario, dependentes, despesas_med, despesas_edu, previdencia)
        st.success(f"💸 Imposto de Renda Pessoa Física: R$ {irpf}")

with tab2:
    st.header("Cálculo de IRPJ")

    cnpj = st.text_input("Digite o CNPJ da empresa")
    if cnpj:
        dados = consultar_cnpj(cnpj)
        if dados:
            st.subheader("🔍 Dados da Empresa:")
            st.json(dados)
        else:
            st.warning("CNPJ não encontrado.")

    tipo = st.selectbox("Tipo de regime", ["Lucro Presumido", "Lucro Real"])

    if tipo == "Lucro Presumido":
        faturamento = st.number_input("Faturamento Mensal (R$)", min_value=0.0)
        atividade = st.selectbox("Atividade", ["Serviço", "Comércio"])

        if st.button("Calcular IRPJ - Lucro Presumido"):
            irpj = calcular_irpj_lucro_presumido(
                faturamento, tipo="comercio" if atividade == "Comércio" else "servico"
            )
            st.success(f"💼 IRPJ (Lucro Presumido): R$ {irpj}")

    elif tipo == "Lucro Real":
        lucro = st.number_input("Lucro Real (R$)", min_value=0.0)

        if st.button("Calcular IRPJ - Lucro Real"):
            irpj = calcular_irpj_lucro_real(lucro)
            st.success(f"🏢 IRPJ (Lucro Real): R$ {irpj}")

st.sidebar.markdown("### 💱 Câmbio Atual (USD -> BRL)")
cambio = consultar_cambio()
if cambio:
    st.sidebar.success(f"US$ 1 = R$ {cambio}")
else:
    st.sidebar.error("Erro ao consultar câmbio.")
