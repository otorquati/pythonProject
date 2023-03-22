calculation_to_seconds = 24
units_name = "horas"

def days_to_units(num_dias):
    return f"{num_dias} dias tem { num_dias * calculation_to_seconds} {units_name}"

user_input = input("Digite o número de dias a ser convertido para horas:\n")
user_input_number = int(user_input)
calculate_value = days_to_units(user_input_number)
print(calculate_value)
