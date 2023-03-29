from datetime import datetime

""" Obtem os dados do usuário """
user_input = input("Entre seu objetivo com o prazo no formato dd.mm.aaaa separado por :\n")
input_list = user_input.split(":")

""" Armazena os valores em variáveis """
goal = input_list[0]
deadline = input_list[1]

"""Converte o prazo em data"""
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")

"""Armazena a data atual na variável """
today_date = datetime.today()

""" Calcula o número de dias para completar o prazo"""
time_till = deadline_date - today_date

""" Converte o prazo em horas e exibe o resultado na tela """
hours_till = int(time_till.total_seconds()/60/60)
print(f"Caro usuário! O prazo para atingir seu objetivo: {goal} é {hours_till} horas")