def get_percentage(number, round_digits=-1):
    if round_digits == -1:
        return f'{round(number*100)}%'
    if round_digits == 0:
        return f'{round(number * 100)}.0%'
    return f'{round(number*100, round_digits)}%'