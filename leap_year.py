"""A leap year calculator."""

def leap_it(input_year: int) -> bool:
    """Function determines whether a year is a leap year."""
    is_it_leap_year: bool = False
    if input_year % 4 == 0:
        is_it_leap_year = True
    return is_it_leap_year

print(leap_it(1999))
print(leap_it(2004))