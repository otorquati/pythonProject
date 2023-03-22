calculation_to_seconds = 24
units_name = "horas"

def days_to_units(num_dias):
    print(f"{num_dias} dias tem { num_dias * calculation_to_seconds} {units_name}")
    print("Tudo certo!")

days_to_units(90)

