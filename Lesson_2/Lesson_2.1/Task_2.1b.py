def index_mass_of_body(weight, height):
    index = weight / (height * height)
    if index < 18.5:
        return "Недостаточная масса"
    elif index > 25:
        return "Избыточная масса"
    else:
        return "Оптимальная масса"


print(index_mass_of_body(float(input()), float(input())))
