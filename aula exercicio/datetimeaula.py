# #datetime

# from datetime import datetime
# # from dateutil.relativedelta import relativedelta


# # data_str_data = '2023-04-29 07:39:00'
# # data_str_formato = '%Y-%m-%d %H:%M:%S'

# # data = datetime.strptime(data_str_data, data_str_formato)
# # data = datetime.now() Para saber a data de agora no meu computador

# #COMPARANDO DATAS
# # formato = '%d-%m-%Y %H:%M:%S'
# # data_inicio = datetime.strptime('29-04-2023 07:39:00', formato)
# # data_fim = datetime.strptime('29-04-2024 09:39:00', formato)
# # # delta = timedelta(days=10, hours=4)
# # delta = relativedelta(data_fim,data_inicio)
# # print(data_fim + relativedelta(seconds=60, minutes=40)) #acrescimo de segundos e minitos
# # print(delta.days, delta.years) #diferença de dias e anos entre as datas

# # print(data_fim - delta)
# # print(data_fim-data_inicio) #diferença entre datas
# # print(data_fim > data_inicio)
# # print(data_fim == data_inicio)

# # fmt = '%d-%m-%Y'
# data = datetime.strptime('2023-04-29 07:23:00', '%Y-%m-%d %H:%M:%S')
# print(data.strftime('%d/%m/%Y'))
# print(data.strftime('%d/%m/%Y %H:%M %S'))

#EXERCICIO
# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020,12,20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos
data_parcela = data_emprestimo

data_parcelas = []
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas= len(data_parcelas)
valor_parcela = valor_total / numero_parcelas

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R${valor_parcela:.2f}')
print()
print(
    f'Você pegou R${valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos'
    f'({numero_parcelas} meses) em parcelas de R$ {valor_parcela:,.2f}.'
)
