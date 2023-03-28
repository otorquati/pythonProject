from helper import validate_and_execute, user_input_message
user_input = ""
# != significa não é igual
while user_input != "exit":
    user_input = input(user_input_message)
    # split function divide a lista string em números separados por :
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_units_dict = {
        "days": days_and_units[0], "units": days_and_units[1]}
    print(days_and_units_dict)
    validate_and_execute(days_and_units_dict)
