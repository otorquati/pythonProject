# Exemplo de uso de While Loops
calculation_to_seconds = 24
units_name = "horas"

def days_to_units(num_dias):
        return f"{num_dias} dias tem { num_dias * calculation_to_seconds} {units_name}"

def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number >0:
            calculate_value = days_to_units(user_input_number)
            print(calculate_value)
        elif user_input_number == 0:
            print("Você digitou um zero, por favor digite um número positivo maior que zero!")
        else:
            print("Você digitou um número negativo, não há conversões para você!")
    except ValueError:
        print("O valor digitado não é válido! Programa parado ")

while True:
    user_input = input("Digite o número de dias a ser convertido para horas:\n")
    validate_and_execute()