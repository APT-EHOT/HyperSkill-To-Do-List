def final_deposit_amount(*interest, amount=1000.0):
    for i in interest:
        i = float(i) / 100.0 + 1.0
        amount *= i
    return round(amount,2)
