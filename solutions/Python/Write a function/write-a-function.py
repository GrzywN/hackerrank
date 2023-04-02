def is_leap(year):
    leap = False

    divisible_by_400 = year % 400 == 0
    divisible_by_4 = year % 4 == 0
    divisible_by_100 = year % 100 == 0

    if divisible_by_400:
        leap = True
    elif divisible_by_4 and divisible_by_100:
        leap = False
    elif divisible_by_4:
        leap = True

    return leap


year = int(input())
print(is_leap(year))
