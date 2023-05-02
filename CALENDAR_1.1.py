import random
from datetime import datetime as DT
from datetime import timedelta


def get_random_date(start, end):
    delta = end - start
    return start + timedelta(random.randint(0, delta.days))


def main():
    count = 0
    while count != 1:
        try:
            date_1 = (input('\n\t\tВведите начальную дату в формате d.m.y (01.01.2010): '))
            date_2 = (input('\n\t\tВведите конечную дату в формате d.m.y (01.01.2018): '))
            start_dt = DT.strptime(date_1, '%d.%m.%Y')
            end_dt = DT.strptime(date_2, '%d.%m.%Y')
            randomizer = get_random_date(start_dt, end_dt)
            print('\n\t\t', str(randomizer)[:10], " ", random.randint(0, 5), random.randint(0, 9), ':',
                  random.randint(0, 5), random.randint(0, 9), ':', random.randint(0, 5), random.randint(0, 9), '.',
                  random.randint(0, 9), random.randint(0, 6), random.randint(0, 6), sep="")
            count += 1
        except ValueError:
            print("\n\n\t\t\t\tВведенные значения неверные. Попробуйте еще раз")


main()

input('\n\n\t\t\tНажмите ENTER чтобый выйти')