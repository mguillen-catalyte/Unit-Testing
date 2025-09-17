def division(numerator, denominator):
    if denominator == 0:
        raise ValueError("You cannot divide by 0")
    else:
        return numerator / denominator


print(division(0, 7))
