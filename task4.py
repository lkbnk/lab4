def f():
    ticket_number = input("Введите номер билета: ")
    index = len(ticket_number) // 2
    sum_1 = 0
    sum_2 = 0

    if len(ticket_number) % 2 == 0:
        print("Введенный номер: " + ticket_number)
        f_ticket_number = int(ticket_number[:index])
        s_ticket_number = int(ticket_number[index:])
        while f_ticket_number > 0:
            digit = f_ticket_number % 10
            sum_1 += digit
            f_ticket_number //= 10
        while s_ticket_number > 0:
            digit = s_ticket_number % 10
            sum_2 += digit
            s_ticket_number //= 10

        if sum_1 == sum_2:
            print("Номер счастливый")
        else:
            print("Номер несчастливый")
    else:
        print("Количество цифр в номере билета должно быть четным")

f()
