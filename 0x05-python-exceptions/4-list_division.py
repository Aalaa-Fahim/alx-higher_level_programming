#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quotients = []

    for i in range(list_length):
        try:
            quotients.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            quotients.append(0)
            print("wrong type")
            continue
        except ZeroDivisionError:
            quotients.append(0)
            print("division by 0")
            continue
        except IndexError:
            quotients.append(0)
            print("out of range")
            continue
        finally:
            pass

    return quotients
