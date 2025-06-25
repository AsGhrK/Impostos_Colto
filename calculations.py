
def calcular_irpf(salario, dependentes=0, despesas_medicas=0, despesas_educacao=0, previdencia=0):
    desconto_dependentes = dependentes * 189.59
    base_calculo = salario - desconto_dependentes - despesas_medicas - despesas_educacao - previdencia

    if base_calculo <= 2259.20:
        aliquota = 0
        deducao = 0
    elif base_calculo <= 2826.65:
        aliquota = 0.075
        deducao = 169.44
    elif base_calculo <= 3751.05:
        aliquota = 0.15
        deducao = 381.44
    elif base_calculo <= 4664.68:
        aliquota = 0.225
        deducao = 662.77
    else:
        aliquota = 0.275
        deducao = 896.00

    imposto = max((base_calculo * aliquota) - deducao, 0)
    return round(imposto, 2)


def calcular_irpj_lucro_presumido(faturamento, tipo='servico'):
    if tipo == 'comercio':
        presuncao = 0.08
    else:
        presuncao = 0.32

    base = faturamento * presuncao
    irpj = base * 0.15

    adicional = 0
    if base > 20000:
        adicional = (base - 20000) * 0.10

    total_irpj = irpj + adicional
    return round(total_irpj, 2)


def calcular_irpj_lucro_real(lucro):
    irpj = lucro * 0.15
    adicional = 0
    if lucro > 20000:
        adicional = (lucro - 20000) * 0.10
    total = irpj + adicional
    return round(total, 2)
