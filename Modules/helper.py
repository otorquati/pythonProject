def days_to_units(num_of_days, convertion_unit):
    if convertion_unit == "horas":
        return f"{num_of_days} dias são iguais a {num_of_days * 24} {convertion_unit}"
    elif convertion_unit == "minutos":
        return f"{num_of_days} dias são iguais a {num_of_days * 24*60} {convertion_unit}"
    elif convertion_unit == "segundos":
        return f"{num_of_days} dias são iguais a {num_of_days * 24 * 60 * 60} {convertion_unit}"
    else:
        return "Unidade não suportada!"


def validate_and_execute(days_and_units_dict):
    try:
        user_input_number = int(days_and_units_dict["days"])
        if user_input_number > 0:
            calculate_value = days_to_units(
                user_input_number, days_and_units_dict["units"])
            print(calculate_value)
        elif user_input_number == 0:
            print(
                "Você digitou um zero, por favor digite um número positivo maior que zero!")
        else:
            print("Você digitou um número negativo, não há conversões para você!")
    except ValueError:
        print("O valor digitado não é válido! Programa parado ")


user_input_message = "Digite o num. de dias e a unidade de conversão separados por :\n"
