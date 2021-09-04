import datetime


def water(age):
    return float(690.8 * age)


def toilet(age):
    return 78 * age


def earth(age):
    return age / (4.5 * (10 ** 9))


def f(m, d, y):
    dob = datetime.date(int(y), int(d), int(m))
    print(dob)
    today = datetime.date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    print("You are {}L of water.".format(water(age)))
    print("You are {} toilet hours.".format(toilet(age)))
    print("You are {} earths old.".format(earth(age)))


if __name__ == '__main__':
    f(input("Month: "), input("Day: "), input("Year: "))
