solved question solutions
def is_leap(year):
    if year % 400 == 0:
        leap=True
        return leap
    elif year % 100 == 0:
        leap=False
        return False
    elif year % 4 == 0:
        leap=True
        return leap
    return False

year = int(input())