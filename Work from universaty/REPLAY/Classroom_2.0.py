import time

time_now = time.localtime()
hours = time_now.tm_hour
minutes = time_now.tm_min
if minutes < 10:
    minutes = "0"+str(minutes)

print(hours, minutes)
if hours >= 9 and minutes >= 15 or hours <= 11 and minutes <= 50:
    print("Ты сегодня ел кашу?")
    answer_1 = input("да или нет?")
    if answer_1 == "да":
        answer_1_1 = input("Сладкая?")
        if answer_1_1 == "да":
            yogurt = input("Сколько грамм йогурта: ")
            breakfast_list = {"Лактония": yogurt}
            answer_1_2 = input("Какая каша?")
            if answer_1_2 == "овсяная":
                breakfast_list.update(

                )

            print(breakfast_list)