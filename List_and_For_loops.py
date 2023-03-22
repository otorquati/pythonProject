# Exemplo de uso de dado do tipo list e uso de For Loops
calculation_to_seconds = 24
units_name = "horas"
user_input = ""

def days_to_units(num_dias):
        return f"{num_dias} dias tem { num_dias * calculation_to_seconds} {units_name}"

def validate_and_execute():
    try:
        user_input_number = int(num_of_days_elemnt)
        if user_input_number >0:
            calculate_value = days_to_units(user_input_number)
            print(calculate_value)
        elif user_input_number == 0:
            print("Você digitou um zero, por favor digite um número positivo maior que zero!")
        else:
            print("Você digitou um número negativo, não há conversões para você!")
    except ValueError:
        print("O valor digitado não é válido! Programa parado ")

# != significa não é igual
while user_input != "exit":
    user_input = input("Digite o número de dias separados por vírgula para ser convertido para horas:\n")
    # split function divide a lista string em números separados por vírgula
    print(type(user_input.split(",")))
    print(user_input.split(","))
    for num_of_days_elemnt in user_input.split(","):
        validate_and_execute()
