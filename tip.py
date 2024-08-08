
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_without=float(d.removeprefix("$"))
    return d_without


def percent_to_float(p):
    p_without=float(p.removesuffix("%"))*float(0.01)
    return p_without


main()
