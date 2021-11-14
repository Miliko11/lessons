
prodolzit = "Y"

while prodolzit == "Y":

    valueX = float(input("Ведите первое число: "))
    valueY = float(input("Ведите второе число: "))

    operation = input("Ведите знак операции которую хотите произвести с числами(+, -, *, /): ")


    if operation == "+":
        result = valueX + valueY
        print("Результат: ", result)
    elif operation == "-":
        result = valueX - valueY
        print("Результат: ", result)
    elif operation == "*":
        result = valueX * valueY
        print("Результат: ", result)
    elif operation == "/":
        result = valueX / valueY
        print("Результат: ", result)
        if valueY == 0:
            print("0")
    prodolzit = input()
