# Exemplo de uso de dado do tipo Dicitonary
""" Dictionary é tum tipo de dado parecido com um list
["days":"units", "days":"units"]
pode ser acessado pelo índices igual um list. """

calculation_to_seconds = 24
units_name = "horas"
user_input = ""

def days_to_units(num_of_days, convertion_unit):
    if convertion_unit == "horas":
        return f"{num_of_days} dias são iguais a {num_of_days * 24} {convertion_unit}"
    elif convertion_unit == "minutos":
        return f"{num_of_days} dias são iguais a {num_of_days * 24*60} {convertion_unit}"
    elif convertion_unit == "segundos":
        return f"{num_of_days} dias são iguais a {num_of_days * 24 * 60 * 60} {convertion_unit}"
    else:
        return "Unidade não suportada!"


def validate_and_execute():
    try:
        user_input_number = int(days_and_units_dict["days"])
        if user_input_number >0:
            calculate_value = days_to_units(user_input_number, days_and_units_dict["units"])
            print(calculate_value)
        elif user_input_number == 0:
            print("Você digitou um zero, por favor digite um número positivo maior que zero!")
        else:
            print("Você digitou um número negativo, não há conversões para você!")
    except ValueError:
        print("O valor digitado não é válido! Programa parado ")



# != significa não é igual
while user_input != "exit":
    user_input = input("Digite o número de dias e a unidade de conversão separados por ':'\n")
    # split function divide a lista string em números separados por :
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_units_dict = {"days":days_and_units[0],"units":days_and_units[1]}
    print(days_and_units_dict)
    validate_and_execute()
    



