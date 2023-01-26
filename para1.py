FirstNumber = int(input("Введите число\n"))
SecondNumber = 1

while (FirstNumber != 0 and SecondNumber != 0):
    Sign = input("Какое действие нужно?\n1)+\n2)-\n3)/\n4)*\n5)Степень крч\n")
    
    SecondNumber = int(input("Введите число\n"))

    print("Ответ: ")

    if (Sign == "+" or Sign == "1"): 
        FirstNumber = FirstNumber+SecondNumber
        print(FirstNumber)    
    if (Sign == "-" or Sign == "2"): 
        FirstNumber = FirstNumber-SecondNumber
        print(FirstNumber)
    if (Sign == "/" or Sign == "3"): 
        FirstNumber = FirstNumber/SecondNumber
        print(FirstNumber)
    if (Sign == "*" or Sign == "4"): 
        FirstNumber = FirstNumber*SecondNumber
        print(FirstNumber)
    if (Sign == "**" or Sign == "5"): 
        FirstNumber = FirstNumber**SecondNumber
        print(FirstNumber)

    
