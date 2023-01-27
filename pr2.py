SumInYear = 0

def Month(Name, Days):
    global SumInYear
    count = 0
    
    for i in range(int(Days+1)):
        for string in str(i):
            count += int(string)

    print(Name + " - " + str(count))
    SumInYear += count
    return count


Month("Январь",31)
# Visokosniy = bool(input("Високостный? (1 - да)"))
if(bool(input("Високостный? (1 - да)")) == True): Month("Февраль",29)
else: Month("Февраль",28)
# print(bool(Visokosniy))
Month("Март",31)
Month("Апрель",30)
Month("Май",31)
Month("Июнь",30)
Month("Июль",31)
Month("Август",31)
Month("Сентябрь",30)
Month("Октябрь",31)
Month("Ноябрь",30)
Month("Декабрь",31)

print(SumInYear)





# def Month (Days) :
#     # while (Count < Days):
#     Count = ""
#         for i in range(int(Days)):
#             for string in str(i):
#                 Count+=string
#                 #Count+=i
#     return Count


# IsVisokosniy = input("Високосный???\n")

# January = Month(31)

# if (IsVisokosniy): February = Month(29)
# else: February = Month(28)

# March = Month(31)
# April = Month(30)
# May = Month(31)
# June = Month(30)
# July = Month(31)
# August = Month(31)
# September = Month(30)
# October = Month(31)
# November = Month(30)
# December = Month(31)


#     # Январь - 31 день
#     # Февраль - 28 дней (29 в високосном)
#     # Март - 31 день
#     # Апрель - 30 дней
#     # Май - 31 день
#     # Июнь - 30 дней
#     # Июль - 31 день
#     # Август - 31 день
#     # Сентябрь - 30 дней
#     # Октябрь - 31 день
#     # Ноябрь - 30 дней
#     # Декабрь - 31 день
