calculation_to_seconds = 24
units_name = "horas"

def days_to_units(num_dias):
    print(num_dias>0)
    # type verifica o tipo de variável e retorna sua classe
    print(type(num_dias))
    if num_dias >0:
        return f"{num_dias} dias tem { num_dias * calculation_to_seconds} {units_name}"
    elif num_dias == 0:
        return "Você digitou um zero, por favor digite um número positivo maior que zero!"
    else:
        return "Você digitou um número negativo e não é possível convertê-lo"
user_input = input("Digite o número de dias a ser convertido para horas:\n")
user_input_number = int(user_input)
calculate_value = days_to_units(user_input_number)
print(calculate_value)